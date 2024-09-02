# RStudio Demo Course

This demo course serves as a demonstration of how one can structure a course with R Studio materials on UCloud. 

The resources and software dependencies that needs to be shared across lectures / classes / sessions should be configured in this repository (repo).

The course materials for each class/session are placed in an external repo: [demo-r-studio-course](https://github.com/jeselginAU/demo-r-studio-course). Placing the course materials in an external repo makes it easier to edit the materials between sessions without requiring approval from UCloud admins. 
Changes to this repo (UCloud-Courses) requires admin approval.  

This demo course is based on Duke University's Statistical Science Introductory Data Science courses: [DukeStatSci/introds](https://github.com/DukeStatSci/introds)

## Making changes to the course materials during the semester
The `start_course.sh` script in this course will download class materials from an external GitHub repo that I manage myself: [demo-r-studio-course](https://github.com/jeselginAU/demo-r-studio-course).
The `start_course.sh` script expects the course materials to be structured as displayed below:

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
* `-u`: The university the course is taught at. 
    * The options are  `aau`,`au`,`cbs`,`dtu`,`itu`,`ku`,`ruc`,`sdu`, and `other`. 
* `-b`: The base image that the course container is build upon. This controls the *FROM* statement in line 1 of the *Dockerfile*.
    * The options are: `almalinux`, `alpine`, `debian`, `ubuntu`, `conda`, `jupyterlab`, `rstudio`, `ubuntu-xfce`, and `almalinux-xfce`.

This will create a folder with a name of the release date in the */Courses* directory under the specified university. It will include the *README.md*, *Dockerfile*, two *.yml* files and *start_course.sh*.

The folder structure for this course was created by navigating to the */scripts* folder and calling the script as below:

`python create-new-course.py -n r-studio-demo-course -c 0000 -r 2024-01-01 -b rstudio -u au`

---
###### **Note**: The *Dockerfile* is used for building a docker image which required to run a container. The *start_course.sh* script is required for launching course applications and *.yml* files for are neccessary for configuring course options for the UCloud webpage interface.

## Building docker image

Building a docker image with the *Dockerfile* will enable containers to run with all installed prerequisites needed for the course. 

For example, this course includes */renv* and */slides* folders that are copied and added to the container's */work* folder using the *COPY* command in the *Dockerfile*. 

In the */scripts* folder, a python script for building images (`build-docker-image.py`) is provided. 

The script requires that your python environment has the python docker package installed. This can be installed by running `pip install docker`. 

You will also need to have an installation of Docker or Docker Desktop.

When running the script, privide the following arguments:

* `-n`: The name of the course 
* `-c`: Official course code (from university course description)
* `-r`: The release date of the course, in the format YYYY-MM-DD
* `-u`: The univerity the course is taught at. 
    * The options are  `aau`,`au`,`cbs`,`dtu`,`itu`,`ku`,`ruc`,`sdu`, and `other`. 
---
The image for this course was built using the *build-docker-image.py* script with these arguments:

`python build-docker-image.py -n r-studio-demo-course -c 0000 -r 2024-01-01 -u au`

This script must be called inside the */scripts* folder.

## Test Docker image

Alternatively, the Docker image can be created and tested using the `build-and-run-course.py` script. 

It includes the **build** function, which calls the `build-docker-image.py` as a subprocess, and the **run** function where the **container name** and **starting command** is specified and **port mapping** is configured. 

Generally, before executing the script:
- set a name for the container
- configure the port mapping (in some cases may not be neccessary)
- edit the starting command to include a value for class selection option and an initialization file if required.

In this example, this is completed and the script can be simply executed by:
`python build-and-run-course.py`

## YML files

Edit the course-name-app.yml file to include the options included in the start_course.sh to integrate them with the UCloud interface. 

- Add the options under **invocation** and **start_course** including its *type* (var or flag), *variable name* and *prefix* (same as in start_course.sh).

- Add parameters for the options under **parameters** including its *title* (seen on UCloud), *type* and *description*.

*enumeration* type is used for selecting an option from a dropdown menu, *flag* - for selecting true of false, *input_file* - for initialization.

In this example, under the parameters, the `class` option has the *enumeration* type which includes the *defaultValue* and *options* fields, that define the selection of the classes. The `force_download` option is of a *flag* type, meaning that the selection for it can be either true of false. `initialization` option is used for installing packages or executing a script based on the *input_file*. The *optional* field determines if the option can be ignored when launching a job.

## Initialization

For information on how to use the *Initialization* parameter, please refer to the [Initialization - Bash script](../../hands-on/init-sh.md), [Initialization - Conda packages](../../hands-on/init-conda.md), and [Initialization - pip packages](../../hands-on/init-pip.md) section of the documentation.
