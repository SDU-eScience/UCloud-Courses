import os
import argparse
import re

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

def parse_n(arg_n):
    return(arg_n.startswith('dreg.cloud.sdu.dk/ucloud-courses/'))

def parse_c(arg_c):
    # TODO
    pass

def parse_p(arg_p):
    return(type(arg_p) == int)

def parse_v(arg_v):
    # Remove excess whitespace 
    arg_v = re.sub('\s+', ' ',arg_v)
    
    # Split string at whitespace
    v_list = [v.strip() for v in arg_v.split(' ')]
    
    # Check that each dir in v_list exists 
    v_exists = [bool] * len(v_list)
    for i in range(0, len(v_list)):
        v_exists[i] = os.path.isdir(v_list[i])
    
    # Check and return results 
    if all(isinstance(v, bool) for v in v_exists) and all(v_exists):
        return(True)
    else:
        print("ERROR: The following directories specified in VOLUMES do not exist:")
        for i in range(0, len(v_exists)):
            if not v_exists[i]:
                print("* %s"%(v_list[i]))
        return(False)

def parse_i(arg_i):
    return(type(arg_i) == bool)

if __name__ == "__main__":

    args = parse_arguments()
    print(parse_n(args.image_name))
    print(parse_p(args.port))
    print(parse_i(args.interactive_mode))
    print(parse_v(args.volume_string))

    call_string = "docker run --rm "
    call_string = call_string + "%s"%('-it ' if parse_i(args.interactive_mode) else '')
    # TODO: Finalize call_string

    
    # Parts the args to form an argument string for `docker run`
    os.system('docker run --rm dreg.cloud.sdu.dk/ucloud-courses/sdu-test__1234:2024-01-01')