# nlp-demo-course

This course is meant to be an example of how one can structure a course on UCloud.

It is based on the materials from the 2023 course _Natural Language Processing_ taken as part of the  [MSc in Cognitive Science](https://masters.au.dk/cognitivescience) at Aarhus University. 

## Making changes to the course materials during the semester
The `start_course.sh` script in this course will download class materials from an external GitHub repo that I manage myself: [demo-NLP-Course-AU](https://github.com/jeselginAU/demo-NLP-Course-AU). In this way, I can edit the course materials available to students without having to edit the UCloud-Courses repo, which would require review and approval from admins. 
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
