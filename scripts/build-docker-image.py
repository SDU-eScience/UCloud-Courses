__maintainer__ = "SDU eScience Center"
__email__ = "support@escience.sdu.dk"

import os
import platform
import argparse 
import docker 
import re 
import sys

def parse_arguments():
    """
    Parses command line arguments for the script.

    @return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Build course Docker image.')
    parser.add_argument('-n', '--image_name', type=str, help='Course name.', required=True)
    parser.add_argument('-d', '--dockerfile_path', type=str, help='Directory of Dockerfile.', required=True)
    return parser.parse_args()

if __name__ == "__main__":
    try:
        client = docker.from_env()
    except Exception as e:
        print(f"Error initializing Docker client: {e}")
        sys.exit(1)  # Exit the script if Docker client cannot be initialized

    args = parse_arguments()
     
    print("[INFO] Starting build of %s."%(args.dockerfile_path))
    print('[INFO] BE PATIENT ... Building the image may take a while.')
    
    # If running on a Windows machine, changing the args.dockerfile_path is necessary
    if platform.system() == 'Windows':
        args.dockerfile_path = repr(args.dockerfile_path)
    client.images.build(path = os.path.dirname(args.dockerfile_path), rm = True, tag = args.image_name)
    
    print("[INFO] Building complete. The image '%s' and available under 'Images' in Docker Desktop."%(args.image_name))
    print("[INFO] Use 'python3 docker-run.py' to start a container.")
