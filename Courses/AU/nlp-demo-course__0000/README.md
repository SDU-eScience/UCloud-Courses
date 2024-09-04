# NLP Demo Course

This course serves as an example of how to structure a course on UCloud.

It is based on the materials from the 2023 _Natural Language Processing_ course, part of the  [MSc in Cognitive Science](https://masters.au.dk/cognitivescience) at Aarhus University. 

## Making changes to the course materials during the semester

The `start_course.sh` script in this course downloads class materials from an external GitHub repository that I manage: [demo-NLP-Course-AU](https://github.com/jeselginAU/demo-NLP-Course-AU). 

This setup allows me to update the course materials available to students **without** needing to modify the UCloud-Courses repository, which would require **review** and **approval** from admins.

The `start_course.sh` script expects the course materials to be organized as follows:

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
All course materials should be placed inside the top-level `classes` folder, with separate subfolders for each class.

Whenever a user (student) starts an instance of this course, the files in the folder corresponding to the selected class or course module are downloaded from the external repository and made available in the user's container.

## Creating New Courses

To create a new course, use the `create-new-course.py` script located in the `/scripts` folder.

The script requires the following arguments:
* `-n`: The name of the course 
* `-c`: The official course code (from the university's course description)
* `-r`: The release date of the course, in the format YYYY-MM-DD
* `-u`: The university the course is taught at. 
    * The options are  `aau`,`au`,`cbs`,`dtu`,`itu`,`ku`,`ruc`,`sdu`, and `other`. 
* `-b`: The base image that the course container is build upon. This controls the *FROM* statement in line 1 of the *Dockerfile*.
    * The options are: `almalinux`, `alpine`, `debian`, `ubuntu`, `conda`, `jupyterlab`, `rstudio`, `ubuntu-xfce`, and `almalinux-xfce`.

This script will create a folder in the `/Courses` directory under the specified university. It will include a `README.md`, a `Dockerfile`, two `.yml` files, and a `start_course.sh` script.

For example, the folder structure for this course was created by navigating to the `/scripts` folder and running the following command:

```bash
python create-new-course.py -n nlp-studio-demo-course -c 0000 -r 2024-01-01 -b jupyterlab -u au
```

---
### Files
- The `Dockerfile` is used for building a Docker image, which is necessary to run a container. 
- The `start_course.sh` script is run inside the container whenever a user launches the application on UCloud. In this demo course, it fetches course materials from the external repository and launches the JupyterLab server.
- The `.yml` files include configuration settings for the UCloud web interface.

## Building the Docker Image

Building a Docker image with the `Dockerfile` allows containers to run with all the necessary prerequisites for the course.

For example, this course includes `/data`, `/scripts`, `/src`, and `/syllabus` folders that are copied into the `/work` folder using the `COPY` command in the `Dockerfile`. These files will be available to users running the container, located in the `/work` folder.

In the `/scripts` folder, a Python script (`build-docker-image.py`) is provided for building Docker images.

### Prerequisites

Ensure your Python environment has the `docker` package installed. You can install it by running:

```bash
pip install docker
```


You will also need to have Docker or Docker Desktop installed on your machine. You can find the appropriate installation for your machine on [docker.com](https://www.docker.com/).
### Running the Script

When running the script, provide the following arguments:

* `-n`: The name of the course 
* `-c`: The official course code (from university course description)
* `-r`: The release date of the course, in the format YYYY-MM-DD
* `-u`: The univerity the course is taught at. 
    * The options are  `aau`,`au`,`cbs`,`dtu`,`itu`,`ku`,`ruc`,`sdu`, and `other`. 
---
For example, the image for this course was built using the `build-docker-image.py` script with the following command:

```bash
python build-docker-image.py -n nlp-studio-demo-course -c 0000 -r 2024-01-01 -u au`
```
##### **Note**: The script must be called from inside the */scripts* folder.

## Testing the Docker Image

<!-- # TODO: Update these build/run/test instructions after we have agreed on a structure of the build and run scripts -->

Alternatively, you can create and test the Docker image using the `build-and-run-course.py` script.

This script contains two key functions:
- **build**: Calls `build-docker-image.py` as a subprocess to create the Docker image.
- **run**: Configures and runs the Docker container, specifying the container name, starting command, and port mapping.

### Pre-Execution Setup

Before executing the script, ensure the following configurations are set:
- **Container Name**: Assign a name for the container.
- **Port Mapping**: Configure the port mapping (note that this might not always be necessary).
- **Starting Command**: Edit the command to include any required options, such as class selection and initialization files.

### Running the Script

Once the setup is complete, you can simply execute the script using:

```bash
python build-and-run-course.py
```

## Editing YML files

To integrate course options with the UCloud interface, you'll need to edit the `course-name-app.yml` file. 

### Steps to Edit the YML File: 
1. **Invocation Options**:
    * Under the **invocation** section, add the options found in `start_course.sh`. 
    * Specify the _type_ (e.g., var or flag), _variable name_, and _prefix_ (matching those in `start_course.sh`).
2. **Parameter Configuration**: 
    * Under the **parameters** section, define the parameters for these options, including: 
        * _title_: The name displayed in the UCloud interface.
        * _type_: The data type (e.g., enumeration, flag, input\_file).
        * _description_: A brief description of the parameter.

### Example Configurations:

* **Enumeration Type**: Used for selecting an option from a dropdown menu. For example, the `class` option, which allows users to select from a list of available classes, includes: 
    * _defaultValue_: The default selected class.
    * _options_: The available choices.
* **Flag Type**: Used for options that are either true or false. For example, the `redownload` option allows the user to decide whether to redownload all course materials from the remote repository.

* **Input File Type**: Used for specifying files required for initialization. The `initialization` option, for example, allows users to upload a script or package to be executed upon container startup.
* **Optional Field**: Indicates whether an option can be skipped when launching a job. 

By configuring these settings, you can ensure that all necessary options are seamlessly integrated into the UCloud interface for your course.

## Initialization

For information on how to use the *Initialization* parameter, please refer to the [Initialization - Bash script](../../hands-on/init-sh.md), [Initialization - Conda packages](../../hands-on/init-conda.md), and [Initialization - pip packages](../../hands-on/init-pip.md) section of the documentation.
