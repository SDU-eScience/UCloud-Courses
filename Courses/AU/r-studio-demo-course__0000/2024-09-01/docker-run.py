#---- CHANGE LINES BELOW IF NECESSARY -----

INTERACTIVE_MODE = "False"      # Set to True to run an interactive container. 
PORT = "8787"                   # Change if another port should be published. NB: Only one port can be published.
VOLUMES = ""                    # Absolute path(s) of folder(s) that should be available in `/work` inside the container. Separate volumes with a single whitespace. 
START_COMMAND = "start_course -c class_01 -a"  # Start command for Docker container. Only relevant if INTERACTIVE_MODE = "False". To not use a start command, leave the string empty.

#------------------------------------------


#---- DO NOT CHANGE LINES BELOW -----------
import git
import os 
import subprocess

IMAGE_NAME = "dreg.cloud.sdu.dk/ucloud-courses/au_r-studio-demo-course__0000:2024-09-01"

os.chdir(os.path.join(git.Repo('.', search_parent_directories=True).working_tree_dir, 'scripts'))
subprocess.call(['python3', 'run-docker-container.py', '-n', IMAGE_NAME, '-p', PORT, '-v', VOLUMES, '-i', INTERACTIVE_MODE, '-s', START_COMMAND])
#------------------------------------------