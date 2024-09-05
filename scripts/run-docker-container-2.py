import os
import argparse

def parse_arguments():
    """
    Parses command line arguments for the script.

    @return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Run course Docker container.')
    parser.add_argument('-n', '--image_name', type=str, help='Docker image.', required=True)
    parser.add_argument('-c', '--container_name', type=str, help="Docker container name.", required=True)
    parser.add_argument('-p', '--port', type=int, help='Port number.', required=True)
    parser.add_argument('-v', '--volume_string', type=str, help="Volumes to be mounted to /work.", required=True)
    parser.add_argument('-i', '--interactive_mode', type=bool, help="If True, run with -it flag.")
    return parser.parse_args()


if __name__ == "__main__":

    args = parse_arguments()
    
    # Parts the args to form an argument string for `docker run`
    os.system('docker run --rm -it dreg.cloud.sdu.dk/ucloud-courses/sdu-test__1234:2024-01-01')