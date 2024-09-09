#----CHANGE LINES BELOW IF NECESSARY-----

INTERACTIVE_MODE = "False"      # Set to True to run an interactive container. 
PORT = "8080"                   # Change if another port should be published. NB: Only one port can be published.
VOLUMES = ""                    # Absolute path(s) of folder(s) that should be available in `/work` inside the container. Separate volumes with a single whitespace. 

#---------------------------------------




#----DO NOT CHANGE LINES BELOW----------
import git
import os 
import subprocess

IMAGE_NAME = "_IMAGE_NAME"

os.chdir(os.path.join(git.Repo('.', search_parent_directories=True).working_tree_dir, 'scripts'))
subprocess.call(['python3', 'run-docker-container-2.py', '-n', IMAGE_NAME, '-p', PORT, '-v', VOLUMES, '-i', INTERACTIVE_MODE],)
#---------------------------------------