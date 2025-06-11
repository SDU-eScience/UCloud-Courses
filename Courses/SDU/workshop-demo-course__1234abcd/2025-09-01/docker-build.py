#---- DO NOT CHANGE LINES BELOW ----------
import subprocess
import os
import git 

IMAGE_NAME = "dreg.cloud.sdu.dk/ucloud-courses/sdu_workshop-demo-course__1234abcd:2025-09-01"
DOCKERFILE_DIR = os.path.normpath("../Courses/SDU/workshop-demo-course__1234abcd/2025-09-01/Dockerfile")

script_dir = os.path.join(git.Repo('.', search_parent_directories=True).working_tree_dir, 'scripts')
os.chdir(script_dir)
subprocess.call(['python', 'build-docker-image.py', '-n', IMAGE_NAME, '-d', DOCKERFILE_DIR])
#-----------------------------------------
