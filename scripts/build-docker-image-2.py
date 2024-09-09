import os 
import argparse 
import docker 
import re 

def parse_arguments():
    """
    Parses command line arguments for the script.

    @return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Build course Docker image.')
    parser.add_argument('-n', '--image_name', type=str, help='Course name.', required=True)
    parser.add_argument('-d', '--dockerfile_path', type=str, help='Directory of Dockerfile.', required=True)
    return parser.parse_args()

def parse_n(arg_n):
    return(arg_n.startswith('dreg.cloud.sdu.dk/ucloud-courses/'))

def parse_d(arg_d):
    return(os.path.exists(arg_d) and os.path.basename(arg_d) == "Dockerfile")

if __name__ == "__main__":
    try:
        client = docker.from_env()
    except Exception as e:
        print(f"Error initializing Docker client: {e}")
        sys.exit(1)  # Exit the script if Docker client cannot be initialized

    args = parse_arguments()
    arg_b_parsed = parse_b(args.build_args)
     
    print("Starting build of %s%s."%(args.dockerfile_path, " with the provided BUILD_ARGS" if len(arg_b_parsed) > 0 else ''))
    print('BE PATIENT ... Building the image may take a while.')
    client.images.build(path = os.path.dirname(args.dockerfile_path), rm = True, tag = args.image_name)
    print("Building complete. The image '%s' and available under 'Images' in Docker Desktop."%(args.image_name))
    print("Use 'python3 run.py' to start the container.")
