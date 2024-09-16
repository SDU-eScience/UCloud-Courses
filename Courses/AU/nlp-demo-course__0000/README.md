# NLP Demo Course

This course serves as an example of how to structure a course using Jupyter notebooks on UCloud.

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
* `-b`: The base image that the course container is build upon. This controls the _FROM_ statement in line 1 of the _Dockerfile_.
  * The options are: `almalinux`, `alpine`, `debian`, `ubuntu`, `conda`, `jupyterlab`, `rstudio`, `ubuntu-xfce`, and `almalinux-xfce`.

This script will create a folder in the `/Courses` directory under the specified university. It will include a `README.md`, a `Dockerfile`, two `.yml` files, and a `start_course.sh` script.

For example, the folder structure for this course was created by navigating to the `/scripts` folder and running the following command:

```bash
python3 create-new-course.py -n nlp-studio-demo-course -c 0000 -r 2024-01-01 -b jupyterlab -u au
```

---

### Files

* The `Dockerfile` is used to build a Docker image, which contains the software, dependencies, and static data necessary for running a container.

```
Note: Data included in the image at build time is immutable, meaning any changes made to files or configurations within the running container will not be saved permanently. To make permanent changes, you need to rebuild the Docker image with the updated data.
```

* The `start_course.sh` script is run inside the container whenever a user launches the application on UCloud. In this demo course, it fetches course materials from the external repository and launches the JupyterLab server.

* The `.yml` files include configuration settings for the UCloud web interface.

* The `docker-build.py` and `docker-run.py` scripts can be executed to build the Docker image with the `Dockerfile` and run the container for testing purposes.

## Building the Docker Image

Building a Docker image with the `Dockerfile` allows containers to run with all the necessary prerequisites for the course.

For example, this course includes `/data`, `/scripts`, `/src`, and `/syllabus` folders that are copied into the `/work` folder using the `COPY` command in the `Dockerfile`. These files will be available to users running the container, located in the `/work` folder.

### Prerequisites

Ensure your Python environment has the `docker` package installed. You can install it by running:

```bash
pip install docker
```

You will also need to have Docker or Docker Desktop installed on your machine. You can find the appropriate installation for your machine on [docker.com](https://www.docker.com/).

### Running docker-build.py

Ensure that you navigate to the course folder, which is named after the release date (e.g., 2024-01-01). Once inside this folder, you can build the Docker image by running:

```bash
python3 docker-build.py
```

## Testing the Docker Image

The Docker container can be tested using the `docker-run.py` script, which simplifies running the container with the necessary options.

Before executing the script, ensure the following configurations are set:

* **Interactive mode**: Enables interaction with the container through a shell session (like _bash_ or _sh_), allowing you to run commands as if you were inside the container’s terminal.

* **Port**: Specifies which ports to map between the host and the container. This allows access to services running inside the container from the host machine.

```
Note: The default host port is `8080`, but if another service or container is using that port, you must choose a different port to avoid conflicts.
```

* **Volumes**: Defines how to mount directories from the host system into the container, allowing shared access to files. This is useful for persisting data, sharing configurations, or accessing files dynamically.

```
Note: If using a Windows directory, paths must be referenced with `/mnt` and use forward slashes. For example, `C:\mydata` would be referenced as `/mnt/c/mydata`. Multiple directories can be mounted by separating paths with a space.
```

### Running docker-run.py

Once the setup is complete, you can simply execute the script using:

```bash
python3 docker-run.py
```

## Editing YML files

To integrate course options with the UCloud interface, you'll need to edit the `course-name-app.yml` file.

### Steps to Edit the YML File

1. **Invocation Options**:
    * Under the **invocation** section, add the options found in `start_course.sh`.
    * Specify the _type_ (e.g., var or flag), _variable name_, and _prefix_ (matching those in `start_course.sh`).
2. **Parameter Configuration**:
    * Under the **parameters** section, define the parameters for these options, including:
        * _title_: The name displayed in the UCloud interface.
        * _type_: The data type (e.g., enumeration, flag, input\_file).
        * _description_: A brief description of the parameter.

### Example Configurations

* **Enumeration Type**: Used for selecting an option from a dropdown menu. For example, the `class` option, which allows users to select from a list of available classes, includes:
  * _defaultValue_: The default selected class.
  * _options_: The available choices.
* **Flag Type**: Used for options that are either true or false. For example, the `redownload` option allows the user to decide whether to redownload all course materials from the remote repository.

* **Input File Type**: Used for specifying files required for initialization. The `initialization` option, for example, allows users to upload a script or package to be executed upon container startup.
* **Optional Field**: Indicates whether an option can be skipped when launching a job.

By configuring these settings, you can ensure that all necessary options are seamlessly integrated into the UCloud interface for your course.

## Initialization

For information on how to use the _Initialization_ parameter, please refer to the [Initialization - Bash script](../../hands-on/init-sh.md), [Initialization - Conda packages](../../hands-on/init-conda.md), and [Initialization - pip packages](../../hands-on/init-pip.md) section of the documentation.
