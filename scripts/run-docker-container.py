"""
Script for teachers to run the docker containers.

Before using the script, the teacher should ensure that the Docker image has been built
using the build-docker-image.py script and that the app.yml file is correctly set up.

The script requires that a Docker daemon is running. Otherwise, it will
exit with an error. The Docker daemon can be started e.g., by opening (and
keeping open) Docker Desktop.

Usage: python3 run-docker-container.py -n <course name> -c <course code> -r <course start date> -u <university> 

The script was built using the Python 3.10.14 interpreter and standard library.
For module requirements outside the Python standard library, see requirements.txt.
"""
__maintainer__ = "SDU eScience Center"
__email__ = "support@escience.sdu.dk"

import os
import json
import argparse
import re
import docker
import yaml
from docker.errors import NotFound, APIError, ContainerError

def parse_arguments():
    """
    Parses command line arguments for the script.

    @return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Build course Docker image.')
    parser.add_argument('-n', '--name', type=str, help='Course name.', required=True)
    parser.add_argument('-c', '--coursecode', type=str, help="Official course code (from university course description)", required=True)
    parser.add_argument('-r', '--release', type=str, help='Release.', required=True)
    parser.add_argument('-u', '--university', type=str, help="University where the course will be taught", required=True, choices=['aau', 'au', 'cbs', 'dtu', 'itu', 'ku', 'ruc', 'sdu', 'other']) 
    return parser.parse_args()

def join_paths(abspath_head, tail):
    """
    Joins and creates absolute path /abspath_head/tail.

    @param abspath_head: The absolute path include parent folder of tail.
    @param tail: The folder/file name to be appended to abspath_head.
    @return: The absolute path /abspath_head/tail.
    """
    return os.path.abspath(os.path.join(abspath_head, tail))

def get_cwd():
    """
    Get the absolute path of the current working directory. 

    @return: Absolute path of the current working directory.
    """
    return os.path.abspath(os.getcwd())

def replace_whitespace(str):
    """
    If the user provides a course name containing whitespace, these are replaced with dashes.
    
    :param str 
    :return str with whitespaces replaced with dashes
    """
    # Remove excess/leading/trailing whitespace, and replace remaining whitespaces with a dash. 
    return(re.sub(' +', '-', str.strip()))

def uniname_fix(uniname):
    if uniname == 'other':
        return 'Other'
    return uniname.upper()


def load_yml(appyml_path):
    """
    Load the container configuration from a YAML file.

    @param config_path: The path to the configuration file.
    @return: The configuration as a dictionary.
    """
    try:
        with open(appyml_path, 'r') as appyml_file:
            return yaml.safe_load(appyml_file)
    except Exception as e:
        print(f"Error loading configuration file: {e}")
        exit(1)

if __name__ == "__main__":

    # Initialize the Docker client to interact with Docker from Python
    try:
        client = docker.from_env()
    except Exception as e:
        print(f"Error initializing Docker client: {e}")
        sys.exit(1)  # Exit the script if Docker client cannot be initialized

    args = parse_arguments()
    university = uniname_fix(args.university)
    coursename = replace_whitespace(args.name)

    # Get and check the current working directory
    cwd = get_cwd() 

    try: 
        if (not os.path.split(cwd)[1] == "scripts"): 
            raise OSError("ERROR ...\nCurrent working directory ({}) is incorrect.\nYou must be in UCloud-Courses/scripts.".format(cwd))
    except OSError as e:
        exit(str(e))
    
    # Extract the courses app.yml file path
    appyml_path = join_paths(os.path.split(cwd)[0], 'Courses')
    appyml_path = join_paths(appyml_path, university)
    appyml_path = join_paths(appyml_path, '{}__{}'.format(coursename, args.coursecode))
    appyml_path = join_paths(appyml_path, args.release)

    course_appyml_name = "{}__{}-app.yml".format(args.name, args.coursecode)
    course_appyml_path = join_paths(appyml_path, course_appyml_name)

    # Check that the courses app.yml file exists 
    try:
        if (os.path.isfile(join_paths(appyml_path, course_appyml_name))):
            print("{}/{} exists.".format(appyml_path, course_appyml_name))
        else:
            raise OSError("ERROR ...\nThe file ({}/{}) does not exist. \nExiting.".format(appyml_path, course_appyml_name))
    except OSError as e: 
        exit(str(e))

    # Construct the Docker image tag using university, course name, course code, and release date.
    IMAGE_TAG = 'dreg.cloud.sdu.dk/ucloud-courses/{}-{}__{}:{}'.format(args.university, coursename, args.coursecode, args.release) 

    try:
        # Load the YAML configuration
        appyml = load_yml(course_appyml_path)
    except Exception as e:
        print(f"Failed to load YAML configuration: {e}")
        exit(1)

    # Access the container name
    CONTAINER_NAME = appyml.get("name")
    if not CONTAINER_NAME:
        raise ValueError("Container name is missing in the {} configuration.".format(course_appyml_name))

    # Access the 'port' under 'web'
    web_key = appyml.get("web", {})
    PORT = web_key.get("port")
    if not PORT:
        raise ValueError("Port is missing in the {} configuration.".format(course_appyml_name))

    # Access the start command
    START_COMMAND = appyml.get("startCommand")
    if not START_COMMAND:
        raise ValueError("Start command is missing in the {} configuration.".format(course_appyml_name))

    # Remove existing container if it exists
    try:
        existing_container = client.containers.get(CONTAINER_NAME)
        existing_container.stop()
        existing_container.remove()
        print(f"Removed existing container: {CONTAINER_NAME}")
    except NotFound:
        print(f"No existing container named '{CONTAINER_NAME}' found.")
    except APIError as e:
        print(f"Error stopping/removing container: {e}")
        exit(1)

    # Run the Docker container
    try:
        print(f"Running the Docker container '{CONTAINER_NAME}' from the image '{IMAGE_TAG}'...")
        container = client.containers.run(
            image=IMAGE_TAG,
            name=CONTAINER_NAME,
            ports={"{}/tcp".format(PORT): PORT},
            detach=True,
            stdin_open=True,
            tty=True,
            command=f"bash -c '{START_COMMAND}'"
        )
        print(f"Container '{CONTAINER_NAME}' is running. You can access it via port {PORT if PORT else 'N/A'}.")
    except ContainerError as e:
        print(f"Error running container: {e}")
        exit(1)
    except APIError as e:
        print(f"Docker API error: {e}")
        exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        exit(1)