# RStudio Demo Course

This demo course serves as a demonstration of how one can structure a course with R Studio materials on UCloud. 

The resources and software dependencies that needs to be shared across lectures / classes / sessions should be configured in this repository (repo).

The course materials for each class/session are placed in an external repo: [demo-r-studio-course](https://github.com/jeselginAU/demo-r-studio-course). Placing the course materials in an external repo makes it easier to edit the materials between sessions without requiring approval from UCloud admins. 
Changes to this repo (UCloud-Courses) requires admin approval.  

This demo course is based on Duke University's Statistical Science Introductory Data Science courses: [DukeStatSci/introds](https://github.com/DukeStatSci/introds)

## Making changes to the course materials during the semester
The `start_course.sh` script in this course will download class materials from an external GitHub repo that I manage myself: [demo-r-studio-course](https://github.com/jeselginAU/demo-r-studio-course).
The `start_course.sh` script expects the course materials to be structured as displayed below

```
└── 📁classes
    └── 📁class_01
        └── file
        └── file
        ...
    └── 📁class_02
        └── file
        └── file
        ...
    ...
    └── 📁class_n
        └── file
        └── file
        ...
```
The course materials are all placed inside the top-level folder `classes`, separated into a folder for each class. 

Whenever a user (/student) starts an instance of this course, all files currently present in the folder, corresponding to the selected class / course module, is downloaded from the external repo and made available in the user's container. 

## Creating courses

To create a new course, utilize the python script `create-new-course.py` in the */scripts* folder. 

The script requires the following arguments:
* `-n`: The name of the course 
* `-c`: Official course code (from university course description)
* `-r`: The release date of the course, in the format YYYY-MM-DD
* `-u`: The univerity the course is taught at. 
    * The options are  `aau`,`au`,`cbs`,`dtu`,`itu`,`ku`,`ruc`,`sdu`, and `other`. 
* `-b`: The base image that the course container is build upon. This controls the *FROM* statement in line 1 of the *Dockerfile*.
    * The options are: `almalinux`, `alpine`, `debian`, `ubuntu`, `conda`, `jupyterlab`, `rstudio`, `ubuntu-xfce`, and `almalinux-xfce`.

This file and folder structure for this course was created by navigating to the */scripts* folder and calling the script as below:

`python create-new-course.py -n r-studio-demo-course -c 0000 -r 2024-01-01 -b rstudio -u au`

The script creates the course folder that includes a *Dockerfile*, used for building the image, required to run a container, a start_course.sh script for launching course applications and *.yml* files for configuring options for the UCloud webpage interface.

## Building docker image

Building a docker image with the *Dockerfile* will enable containers to run with all installed prerequisites needed for the course. For example, this course includes */renv* and */slides* folders that are copied and added to the container's */work* folder using the *COPY* command in the *Dockerfile* which is always in the release date folder (here 2024-01-01).

In the */scripts* folder, a python script for building images (`build-docker-image.py`) is provided. The script requires that your python environment has the python docker package installed. This can be installed by running `pip install docker`. You will also need to have an installation of docker  When running the script, privide the following arguments:

* `-n`: The name of the course 
* `-c`: Official course code (from university course description)
* `-r`: The release date of the course, in the format YYYY-MM-DD
* `-u`: The univerity the course is taught at. 
    * The options are  `aau`,`au`,`cbs`,`dtu`,`itu`,`ku`,`ruc`,`sdu`, and `other`. 

The image for this course was built using the *build-docker-image.py* script with these arguments:

`python build-docker-image.py -n r-studio-demo-course -c 0000 -r 2024-01-01 -u au`

This to must be called inside the */scripts* folder.

## Test Docker image

To run the container with the built image, in Docker Desktop copy the ID of the image, which is just below it's name, and use `docker run` command in the terminal with these flags:

`--rm -it -d --name test_name <image_id> bash -c "sudo start_course -s req -c class_01"`

Paste the ID of the image in place of <image_id>, select to install requirements with the **-s** flag, and the class id with the **-c** flag from the start_course.sh.

Example commands used to test this demo can be found in /test/build_and_run

## YML files

Edit the course-name-app.yml file to include the options included in the start_course.sh to integrate them with the UCloud interface. 

- Add the options under **invocation** and **start_course** including its *type* (var or flag), *variable name* and *prefix* (same as in start_course.sh).

- Add parameters for the options under **parameters** including its *title* (seen on UCloud), *type* and *description*.

*enumeration* type is used for selecting an option from a dropdown menu, *flag* - for selecting true of false, *input_file* - for initialization.

## Initialization

For information on how to use the *Initialization* parameter, please refer to the [Initialization - Bash script](../../hands-on/init-sh.md), [Initialization - Conda packages](../../hands-on/init-conda.md), and [Initialization - pip packages](../../hands-on/init-pip.md) section of the documentation.
