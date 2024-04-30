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
    parser.add_argument('-r', '--release', type=str, help='Course start time (YYYY-MM-DD).', required=True) # Maybe we should do a check on ths input to ensure its validity?
    parser.add_argument('-b', '--baseimage', type=str, help='base image', required=True, choices=['almalinux', 'alpine', 'centos', 'debian', 'ubuntu', 'conda', 'jupyterlab', 'rstudio', 'ubuntu-xfce', 'almalinux-xfce'])
    return parser.parse_args()

def check_release(release_str):
    return(re.fullmatch("^(20[2-3][4-9])(-)(0[1-9]|1[0-2])(-)(0[1-9]|1[0-9]|2[0-9]|3[0-1])$", release_str) is not None)


if __name__ == "__main__":
    args = parse_arguments()

    # Check if format for -r option is valid
    try: 
        if not check_release(args.release):
            raise ValueError("Invalid course start date given to the-r option. The format must be: YYYY-MM-DD.")
    except ValueError as e: 
        exit(str(e))

    cwd = get_cwd() # NB: It is (currently) the users responsibility that the working directory is correct. (Although if it is wrong, an error is likely in create_dir(.) below.)

    # Create the course folder structure 
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
