"""
Script for teachers to set up the development environment for new courses in UCloud.
The script is portable across operating systems. 

Usage: python3 create-new-course.py -n <course name> -r <course start date> -b <base image>

The script was build using the Python 3.10.14 interpreter and standard library. 
For module requirements outside the Python standard library, see requirements.txt.
"""
__maintainer__ = "SDU eScience Center"
__email__ = "support@escience.sdu.dk"

import os # For portable handling of paths. Part of the standard library. 
import argparse # For passing command line arguments. Part of the standard library. 
import shutil # For a portable way of copying files  
import re # For string manipulation. Part of the standard library. 
import datetime as dt # For fetching the current month and year. Part of the standard library. 
import requests # Portable library for making HTTP requests. Part of the standard library. 

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

def create_dir(dir):
    """
    Creates a directory.

    @param parent_dir: The absolute path for the directory to be created.
    """
    os.mkdir(dir)

def parse_arguments():
    """
    Parses command line arguments for the script.

    @return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Create a new course in UCloud.")
    parser.add_argument('-n', '--name', type=str, help='Course name.', required=True)
    parser.add_argument('-r', '--release', type=str, help='Course start date (YYYY-MM-DD).', required=True) 
    parser.add_argument('-b', '--baseimage', type=str, help='Base image', required=True, choices=['almalinux', 'alpine', 'debian', 'ubuntu', 'conda', 'jupyterlab', 'rstudio', 'ubuntu-xfce', 'almalinux-xfce'])
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
    return (all(res) is True, res)

def get_invalid_release_values(res_list):
    """
    Produces a string showing which values of the provided course start date are invalid

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

def replace_whitespace(str):
    """
    If the user provides a course name containing whitespace, these are replaced with dashes.
    
    :param str 
    :return str with whitespaces replaced with dashes
    """
    # Remove excess/leading/trailing whitespace, and replace remaining whitespaces with a dash. 
    return(re.sub(' +', '-', str.strip()))

def get_month_year():
    """
    :return String with month-year base image tag.
    """
    d = dt.datetime.now()
    return(d.strftime("%B")[0:3] + str(d.year))

def get_baseimage_newest_tag(baseimage):
    """
    Fetches newest release for baseimage.

    :param baseimage A base image from {jupyterlab, conda, rstudio}
    :return The newest release of the software
    """
    if(baseimage in ["ubuntu", "almalinux", "debian", "alpine", "almalinux-xfce", "ubuntu-xfce"]):
        return(get_month_year())
    if(baseimage == "conda"):
        ret = requests.get("https://api.github.com/repos/conda-forge/miniforge/releases/latest").json()
        ret = ret["tag_name"]
        ret = re.sub("-", ".", ret) # Replace '-' with '.'
        return(ret)
    if(baseimage == "jupyterlab"):
        ret = requests.get("https://api.github.com/repos/jupyterlab/jupyterlab/releases/latest").json()
        ret = ret["tag_name"]
        ret = re.sub("v", "", ret) # Replace 'v' with ''
        return(ret)
    if(baseimage == "rstudio"):
        ret = requests.get("https://svn.r-project.org/R/tags/").text
        sion_list = re.findall("R[-]\d+[-]\d+[-]\d+", ret)
        sion_list = [re.sub("R-", "", e) for e in sion_list] 
        sion_list = [re.sub("-", ".", e) for e in sion_list]
        return(max(sion_list)) 
    
def get_baseimage_name(baseimage):
    """
    Maps the base image string given in args.baseimage to the name of the baseimage in the Docker registry

    :param A base image name from the valid names in args.baseimage 
    :return The base image name from the Docker registry
    """
    if(baseimage in ["almalinux", "alpine", "debian", "ubuntu", "ubuntu-xfce", "almalinux-xfce"]):
        return("base-" + baseimage)
    if(baseimage == "conda"):
        return("conda")
    if(baseimage == "rstudio"):
        return("rstudio")
    if(baseimage == "jupyterlab"):
        return("jupyter-all-spark")

if __name__ == "__main__":
    try:
        # Parse and clean the user input
        args = parse_arguments()
        args.name = replace_whitespace(args.name).lower()

        # Check that format and values for input for -r are valid
        try: 
            if not check_release_format(args.release):
                raise ValueError("ERROR ...\nThe format of the provided course start date ({}) is invalid.\nThe format must be: YYYY-MM-DD.".format(args.release))
            if not check_release_values(args.release)[0]:
                raise ValueError("ERROR ...\nSome values of the provided start date ({}) are invalid.\nThe following values for the course start date were invalid: {}".format(args.release, get_invalid_release_values(check_release_values(args.release)[1])))
        except ValueError as e: 
            exit(str(e))

        # Get the working directory
        cwd = get_cwd() 

        # Check if cwd is correct. 
        # NB: This error check does not guarantee the correct cwd, but for all practical purposes it should suffice. 
        try:
            files_in_cwd = os.listdir(cwd)
            path_split = os.path.split(cwd)
            path_tail = path_split[1]
            path_tail_of_head = os.path.split(path_split[0])[1] 
            if (not "create-new-course.py" in files_in_cwd) or (not "templates" in files_in_cwd):
                raise OSError("ERROR ...\nCurrent working directory ({}) is incorrect.\nYou must be in UCloud-Courses/scripts.".format(cwd))
            if (not path_tail == "scripts") or (not path_tail_of_head == "UCloud-Courses"):
                raise OSError("ERROR ...\nCurrent working directory ({}) is incorrect.\nYou must be in UCloud-Courses/scripts.".format(cwd))
        except OSError as e:
                exit(str(e))
    

        # Create the course file tree
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
        course_logo_dir = join_paths(course_root_dir, 'logo')
        course_test_dir = join_paths(course_root_dir, 'test')

        # Check if course name is available
        courses_list = list()
        for root, dirs, files in os.walk(os.path.split(course_root_dir)[0]):
            for course in dirs:
                courses_list.append(course)

        try: 
            if args.name in courses_list:
                raise OSError("Error ...\nA course with the the title '{}' already exists.".format(args.name))
        except OSError as e:
            exit(str(e)) 
        
        dir_list = [course_root_dir, course_release_dir, course_logo_dir, course_test_dir]

        for dir in dir_list:
            create_dir(dir)

        # Populate the course folders
        templates_dir = join_paths(cwd, 'templates')

        template_readme = join_paths(templates_dir, 'README.md.template') 
        template_dockerfile = join_paths(templates_dir, 'Dockerfile.%s_template'%(args.baseimage))
        template_appyml = join_paths(templates_dir, 'template-app.yml')
        template_toolyml = join_paths(templates_dir, 'template-tool.yml')
        template_startcourse = join_paths(templates_dir, 'start_course.template')

        # Get name and tag for args.baseimage
        baseimage_name = get_baseimage_name(args.baseimage)
        baseimage_tag = get_baseimage_newest_tag(args.baseimage)

        with (
        open(template_readme, 'r') as f1,
        open(template_dockerfile, 'r') as f2,
        open(template_appyml, 'r') as f3,
        open(template_toolyml, 'r') as f4,
        open(template_startcourse, 'r') as f5

        ):
            readme = f1.read()
            f1.close()
            dockerfile = f2.read()
            f2.close()
            appyml = f3.read()
            f3.close()
            toolyml = f4.read()
            f4.close()
            startcourse = f5.read()
            f5.close()

        # Edit the contents of the templates based on input from user

        # Edit README
        readme = re.sub("COURSE_NAME", args.name, readme)

        # Edit Dockerfile
        dockerfile = re.sub("TAG", baseimage_tag, dockerfile)

        # Edit template-app.yml
        appyml = re.sub("COURSE_NAME", args.name, appyml)
        appyml = re.sub("COURSE_TAG", args.release, appyml)

        # Edit template-tool.yml
        toolyml = re.sub("COURSE_NAME", args.name, toolyml)
        toolyml = re.sub("COURSE_TAG", args.release, toolyml)        
        
        # Write to edited contents from the tempate files to the course folder
        with (
            open(join_paths(course_root_dir, 'README.md'), 'w') as f1,
            open(join_paths(course_release_dir, 'Dockerfile'), 'w') as f2,
            open(join_paths(course_release_dir, '%s-app.yml'%(args.name)), 'w') as f3,
            open(join_paths(course_release_dir, '%s-tool.yml'%(args.name)), 'w') as f4,
            open(join_paths(course_release_dir, 'start_course.sh'), 'w') as f5
        ):
            f1.write(readme)
            f1.close()
            f2.write(dockerfile)
            f2.close()
            f3.write(appyml)
            f3.close()
            f4.write(toolyml)
            f4.close()
            f5.write(startcourse)
            f5.close()
    
    # Clean up in case of error after the creating of the course file tree. Prompt the user before cleanup.
    except Exception as e:
        exit(str(e))

