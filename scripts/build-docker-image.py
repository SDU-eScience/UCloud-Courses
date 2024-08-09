"""
Script for teachers to build the docker images.

Before using the script, the teacher should create a course using 
create-new-course.py, complete the Dockerfile and startingscript etc.

The script requires that a Docker daemon is running. Otherwise it will
exit with a error. The Docker daemon can be started e.g., by opening (and
keeping open) Docker Desktop.  

Once the image has been built, the teacher can interact with it
using Docker Desktop. 

Usage: python3 build-docker-image.py -n <course name> -c <course code> -r <course start date> -u <university> 

The script was build using the Python 3.10.14 interpreter and standard library. 
For module requirements outside the Python standard library, see requirements.txt.
"""
__maintainer__ = "SDU eScience Center"
__email__ = "support@escience.sdu.dk"

import os 
import argparse 
import docker 

def parse_arguments():
    """
    Parses command line arguments for the script.

    @return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Build course Docker image.')
    parser.add_argument('-n', '--name', type=str, help='Course name.', required=True)
    parser.add_argument('-c', '--coursecode', type=str, help="Official course code (from university course description)", required=True)
    parser.add_argument('-r', '--release', type=str, help='Release.', required=True)
    parser.add_argument('-u', '--university', type=str, help="University where the course will be taught", required=True, choices=['sdu', 'au', 'aau']) # Do we need to add more universities?
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


if __name__ == "__main__":
    client = docker.from_env()

    args = parse_arguments()

    # Get and check the current working directory
    cwd = get_cwd() 

    try: 
        if (not os.path.split(cwd)[1] == "scripts"): 
            raise OSError("ERROR ...\nCurrent working directory ({}) is incorrect.\nYou must be in UCloud-Courses/scripts.".format(cwd))
    except OSError as e:
        exit(str(e))
    
    # Check that file exists 
    dockerfile_path = join_paths(os.path.split(cwd)[0], 'Courses')
    dockerfile_path = join_paths(dockerfile_path, args.university)
    dockerfile_path = join_paths(dockerfile_path, '{}__{}'.format(args.name, args.coursecode))
    dockerfile_path = join_paths(dockerfile_path, args.release)

    # Check that Dockerfile exists 
    try:
        if (os.path.isfile(join_paths(dockerfile_path, 'Dockerfile'))):
            print("Dockerfile exists.".format(dockerfile_path))
        else:
            raise OSError("ERROR ...\nThe file ({}) does not exist. \nExiting.".format(dockerfile_path))
    except OSError as e: 
        exit(str(e))

    # Build the Docker image from the Dockerfile 
    image_tag = 'dreg.cloud.sdu.dk/ucloud-courses/{}-{}-{}:{}'.format(args.university, args.name, args.coursecode, args.release) # Or should it be dreg.cloud.sdu.dk/ucloud-apps/ instead?
    
    print("Starting build of {}.".format(join_paths(dockerfile_path, 'Dockerfile')))
    print('BE PATIENT ... Building the image may take a while.')
    client.images.build(path = dockerfile_path, rm = True, tag = image_tag)
    print("Building complete. The image is called '{}' and available under 'Images' in Docker Desktop.".format(image_tag))
