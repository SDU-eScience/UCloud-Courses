#----CHANGE LINES BELOW IF NECESSARY-----
BUILD_ARGS = ""         # Add any needed --build-args for docker build. Separate by a space if more than one. 
#---------------------------------------


#----DO NOT CHANGE LINES BELOW----------
import subprocess
import os
import git 

IMAGE_NAME = "_IMAGE_NAME"
DOCKERFILE_DIR = "_DOCKERFILE_DIR"

script_dir = os.path.join(git.Repo('.', search_parent_directories=True).working_tree_dir, 'scripts')
os.chdir(script_dir)
subprocess.call(['python3', 'build-docker-image.py', '-n', 'test', '-c', '1234', '-r', '2024-01-01', '-u', 'sdu'])
#---------------------------------------