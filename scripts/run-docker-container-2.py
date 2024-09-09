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
    parser.add_argument('-p', '--port', type=int, help='Port number.', required=True)
    parser.add_argument('-v', '--volume_string', type=str, help="Volumes to be mounted to /work.", required=True)
    parser.add_argument('-i', '--interactive_mode', type=str, help="If True, run with -it flag.", required=True)
    return parser.parse_args()

def parse_n(arg_n):
    return(arg_n.startswith('dreg.cloud.sdu.dk/ucloud-courses/'))

def parse_p(arg_p):
    return(type(arg_p) == int)

def parse_v(arg_v):
    # Remove excess whitespace 
    arg_v = arg_v.strip()
    arg_v = re.sub('\s+', ' ',arg_v)
    
    # Split string at whitespace
    v_list = [v.strip() for v in arg_v.split(' ')]
    
    # Check that each dir in v_list exists 
    v_exists = [bool] * len(v_list)
    for i in range(0, len(v_list)):
        v_exists[i] = os.path.isdir(v_list[i])
    
    # Check and return results 
    if all(isinstance(v, bool) for v in v_exists) and all(v_exists):
        return(True, v_list)
    else:
        print("ERROR: The following directories specified in VOLUMES do not exist:")
        for i in range(0, len(v_exists)):
            if not v_exists[i]:
                print("* %s"%(v_list[i]))
        return(False, [])

def parse_i(arg_i):
    if arg_i == "True" or arg_i == "False":
        val = True if arg_i == "True" else False
        return(True, val)
    return(False, None)

if __name__ == "__main__":
    # Parse the arguments 
    args = parse_arguments()
    i_isvalid, i_value = parse_i(args.interactive_mode)
    v_list_bool, v_list_parsed = parse_v(args.volume_string)

    # Get results from parser functions
    res = {'image_name': parse_n(args.image_name), 'port': parse_p(args.port), 'volume_string': v_list_bool, 'interactive_mode': i_isvalid}

    # Error handling from parser functions
    if any(value == False for value in res.values()):
        if not res['image_name']: 
            print("ERROR: Invalid IMAGE_NAME.")
        if not res['port']:
            print("ERROR: Invalid PORT. Must be an integer.")
        if not res["volume_string"]:
            print("ERROR: Invalid VOLUMES.")
        if not res["interactive_mode"]:
            print("ERROR: Invalid value for INTERACTIVE_MODE. Must be 'True' or 'False'")
        exit(1)
    else: 
        # Create call string for `docker run` 
        call_string = "docker run --rm "
        call_string += "%s "%('-it' if i_value else '')
        call_string += "%s %s:%s "%('-p', args.port, args.port)
        
        for v in v_list_parsed:
            call_string += "%s %s:%s "%('-v', v, "/work/" + os.path.basename(v))
        
        call_string += " %s"%(args.image_name)
        
        try:
            # Start container 
            print("\nStarting docker container (in %s mode).\n"%("interactive" if i_value else "non-interactive"))
            os.system(call_string)
        except OSError as e:
            exit(e)