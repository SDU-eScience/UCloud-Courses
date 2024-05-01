### Script for teachers to set up the development environment for new courses in UCloud.
### The script is portable across operating systems. 

import os # For portable handling of paths 
import argparse # For passing command line arguments
import shutil # For a portable way of copying files  
import re 

def join_paths(abspath_head, tail):
    """
    Joins and creats absolute path /abspath_head/tail.

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

def create_dir(dir):
    """
    Creates a directory.

    @param parent_dir: The absolute path for the directory to be created.
    """
    os.mkdir(dir)

def copy_file(source, dest):
    """
    Used to populate the directories in the app's file tree with templates. 

    @param: The absolute path of the source file to be copied.
    @param: The absolute path to where the source file should be copied to. 
    """
    shutil.copyfile(source, dest)

def parse_arguments():
    """
    Parses command line arguments for the script.

    @return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Create a new course in UCloud.")
    parser.add_argument('-n', '--name', type=str, help='Course name', required=True)
    parser.add_argument('-r', '--release', type=str, help='Course start date (YYYY-MM-DD).', required=True) 
    parser.add_argument('-b', '--baseimage', type=str, help='Base image', required=True, choices=['almalinux', 'alpine', 'centos', 'debian', 'ubuntu', 'conda', 'jupyterlab', 'rstudio', 'ubuntu-xfce', 'almalinux-xfce'])
    return parser.parse_args()

def check_release_format(release_str):
    """
    Checks if the release date follows the format dddd-dd-dd (where d denoates a digit)

    @param release_str A string
    @return: True if release_str has the format dddd-dd-dd. False otherwise.
    """
    return(re.fullmatch("^\d{4}(-)\d{2}(-)\d{2}$", release_str) is not None)

def check_release_values(release_str):
    """
    Checks the validity of the values of the provided course start date. Requires that release check_release_format(release_str) == True.

    @param release_str A string
    @return A tuple of length 2: (True iff. all the values are valid, list of length 3 which indicates which values are valid)
    """
    year = int(release_str[:4]) 
    month = int(release_str[5:7])
    day = int(release_str[8:10])
    res = []
    res.append(year >= 2024)
    res.append(month in range(1,13))
    res.append(day in range(1,32))
    invalid = []
    return (all(res) is True, res)

def get_invalid_release_values(res_list):
    """
    Procudes a string showing which values of the provided course start date are invalid

    @param res_list A boolean list of length 3. Intended to be the second element of the tuple returned from check_release_values()
    @return A string
    """
    invalid = ""
    if res_list[0] is False:
        invalid += "\n* YEAR (must be 2024 or later)."
    if res_list[1] is False:
        invalid += "\n* MONTH (must be in the range 01-12)."
    if res_list[2] is False:
        invalid += "\n* DAY (must be in the range 01-31)."
    return invalid

if __name__ == "__main__":
    args = parse_arguments()

    # Check if format for input for -r is valid
    try: 
        if not check_release_format(args.release):
            raise ValueError("The format of the provided course start date ({}) is invalid. \n The format must be: YYYY-MM-DD.".format(args.release))
        if not check_release_values(args.release)[0]:
            raise ValueError("Some values of the provided start date ({}) are invalid.\nThe following values for the course start date were invalid: {}".format(args.release, get_invalid_release_values(check_release_values(args.release)[1])))
    except ValueError as e: 
        exit(str(e))

    # Get the working directory
    # # NB: It is the user's responsibility that the working directory is correct. (Although if it is wrong, an error is likely in create_dir(.) below.)
    cwd = get_cwd() 

    # Create the course folder structure 
    # UCloud-Courses/
    #  |- Courses/
    #    |- <course name>/
    #      |- <course start date>/
    #         |- Dockerfile 
    #         |- README.md 
    #         |- *.yml 
    #         |- start_app.sh

    course_root_dir = os.path.abspath(os.path.join(os.path.split(cwd)[0], 'Courses', args.name))
    course_release_dir = join_paths(course_root_dir, args.release)
    
    dir_list = [course_root_dir, course_release_dir]

    for dir in dir_list:
        create_dir(dir)

    # Insert the proper information (course name, release etc.) into the template files before copying them into the course folders
    # TODO: When the templates are finalized

    # Populate the course folders
    templates_dir = join_paths(cwd, 'templates')

    copy_file(join_paths(templates_dir, 'README.md.template'), join_paths(course_release_dir, 'README.md'))
    copy_file(join_paths(templates_dir, 'Dockerfile.%s_template'%(args.baseimage)), join_paths(course_release_dir, 'Dockerfile'))
    copy_file(join_paths(templates_dir, 'template-app.yml'), join_paths(course_release_dir, '%s-app.yml'%(args.name)))
    copy_file(join_paths(templates_dir, 'template-tool.yml'), join_paths(course_release_dir, '%s-tool.yml'%(args.name)))
    copy_file(join_paths(templates_dir, 'start_app.template'), join_paths(course_release_dir, 'start_app.sh'))

    # To remove the course file tree use: rm -r ../Courses/<course name>
