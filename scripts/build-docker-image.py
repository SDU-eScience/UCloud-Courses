"""
Script for teachers to build the docker images.

Before using the script, the teacher should create a course using 
create-new-course.py, complete the Dockerfile and startingscript etc.

The script requires that a Docker daemon is running. Otherwise it will
exit with a error. The Docker daemon can be started e.g., by opening (and
keeping open) Docker Desktop.  

Once the image has been built, the teacher can interact with it
using Docker Desktop. 

Usage: python3 build-docker-image.py -n <course name> -r <course start date> 

The script was build using the Python 3.10.14 interpreter and standard library. 
For module requirements outside the Python standard library, see requirements.txt.
"""

import os 
import argparse 
import docker 

def parse_arguments():
    """
    Parses command line arguments for the script.

    @return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Create a new course in UCloud.')
    parser.add_argument('-n', '--name', type=str, help='Course name.', required=True)
    parser.add_argument('-r', '--release', type=str, help='Release.', required=True)
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
    dockerfile_path = join_paths(dockerfile_path, args.name)
    dockerfile_path = join_paths(dockerfile_path, args.release)

    # Check that Dockerfile exists 
    try:
        if (not os.path.isfile(join_paths(dockerfile_path, 'Dockerfile'))):
            raise OSError("ERROR ...\nThe file ({}) does not exist.".format(dockerfile_path))
    except OSError as e: 
        exit(str(e))

    # Build the Docker image from the Dockerfile 
    image_tag = 'dreg.cloud.sdu.dk/ucloud-courses/' + args.name + ':' + args.release # Or should it be dreg.cloud.sdu.dk/ucloud-apps/ instead?
    
    print("Starting build of {}.".format(join_paths(dockerfile_path, 'Dockerfile')))
    client.images.build(path = dockerfile_path, rm = True, tag = image_tag)
    print("Building complete. The image is called '{}' and available under 'Images' in Docker Desktop.".format(image_tag))
