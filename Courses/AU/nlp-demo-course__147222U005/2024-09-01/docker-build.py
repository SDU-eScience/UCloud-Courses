#---- DO NOT CHANGE LINES BELOW ----------
import subprocess
import os
import git 

IMAGE_NAME = "dreg.cloud.sdu.dk/ucloud-courses/au_nlp-demo-course__147222u005:2024-09-01"
DOCKERFILE_DIR = "../Courses/AU/nlp-demo-course__147222U005/2024-09-01/Dockerfile"

script_dir = os.path.join(git.Repo('.', search_parent_directories=True).working_tree_dir, 'scripts')
os.chdir(script_dir)
subprocess.call(['python3', 'build-docker-image.py', '-n', IMAGE_NAME, '-d', DOCKERFILE_DIR])
#-----------------------------------------
