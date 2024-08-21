# RStudio Demo Course

This demo course serves as a demonstration of how one can structure a course with R Studio materials on UCloud. 

The resources and software dependencies that needs to be shared across lectures / classes / sessions should be configured in this repo.

The course materials for each class/session are placed in an external repo: [demo-r-studio-course](https://github.com/jeselginAU/demo-r-studio-course). Placing the course materials in an external repo makes it easier to edit the materials between sessions without requiring approval from UCloud admins. 
Changes to the UCloud Courses repo (this repo) reqires admin approval.  

This demo course is based on Duke University's Statistical Science Introductory Data Science courses: [DukeStatSci/introds](https://github.com/DukeStatSci/introds)

## Making changes to the course materials during the semester
The `start_course.sh` script in this course will download class materials from an external GitHub repo that I manage myself: [demo-r-studio-course](https://github.com/jeselginAU/demo-r-studio-course). In this way, I can edit the course materials available to students without having to edit the UCloud-Courses repo, which would require review and approval from admins. 
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

Whenever a user (/student) starts an instance of this course, all files in currently present in the folder corresponding to the selected class / course module is downloaded from the external repo and made available in the user's container. 

## Initialization

For information on how to use the *Initialization* parameter, please refer to the [Initialization - Bash script](../../hands-on/init-sh.md), [Initialization - Conda packages](../../hands-on/init-conda.md), and [Initialization - pip packages](../../hands-on/init-pip.md) section of the documentation.
