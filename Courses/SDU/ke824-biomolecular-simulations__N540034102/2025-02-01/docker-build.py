#---- DO NOT CHANGE LINES BELOW ----------
import subprocess
import os
import git 

IMAGE_NAME = "dreg.cloud.sdu.dk/ucloud-courses/sdu_ke824-biomolecular-simulations__n540034102:2025-02-01"
DOCKERFILE_DIR = "../Courses/SDU/ke824-biomolecular-simulations__N540034102/2025-02-01/Dockerfile"

script_dir = os.path.join(git.Repo('.', search_parent_directories=True).working_tree_dir, 'scripts')
os.chdir(script_dir)
subprocess.call(['python3', 'build-docker-image.py', '-n', IMAGE_NAME, '-d', DOCKERFILE_DIR])
#-----------------------------------------
