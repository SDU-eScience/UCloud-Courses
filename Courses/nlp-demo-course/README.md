# nlp-demo-course

This course is meant to be an example of how one can structure a course on UCloud.

It is based on the materials from the 2023 course _Natural Language Processing_ taken as part of the  [MSc in Cognitive Science](https://masters.au.dk/cognitivescience) at Aarhus University. 

## Making changes to the course materials during the semester
The `start_course.sh` script in this course will download class materials from an external GitHub repo that I manage myself [](https://github.com/jeselginAU/demo-NLP-Course-AU). In this way, I can edit the course materials available to students without having to edit the UCloud-Courses repo, which would require review and approval from admins. 
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


This repository contains all of the code and data related to the module _Natural Language Processing_ taken as part of the  [MSc in Cognitive Science](https://masters.au.dk/cognitivescience) at Aarhus University.

This repository is in active development, with new material being pushed on a weekly basis. Slides will be uploaded to Brightspace.

<!-- ## Initialization

For information on how to use the *Initialization* parameter, please refer to the [Initialization - Bash script](../hands-on/init-sh.md), [Initialization - Conda packages](../hands-on/init-conda.md), and [Initialization - pip packages](../hands-on/init-pip.md) section of the documentation. -->

## Technicalities

For the sake of convenience, I advise that everyone uses [UCloud](https://cloud.sdu.dk) for development purposes. You can then fork this repo and pull any changes that are made on a weekly basis.

For those of you who do not wish to use UCloud, you are of course welcome to use your own machine. However, due to time constraints, we will not be providing any technical support if you choose to go this way. 

If you _still_ want to use your own machine, make sure to have _at least_ Python 3.7 installed. Some of the code developed in the classroom will not be backwards compatible with earlier versions of Python.

## Repo structure

This repository has been initialised with the following directory structure:

| Column | Description|
|--------|:-----------|
```classes``` | Instructions for each of the classrooms.
```src``` | A folder for Python scripts developed in class.
```syllabus```| Containing a markdown file with the course syllabus and readings, as well as a file listing additional resources.
```nbs```| Will contain the solutions to assignments and classes.
```data```| Will contain data we will use for some of the exercises.

## Classroom instruction
The general structure for classroom instruction is the following: I will present you with a few exercises, which you can work on solving in class and at home. The week after, I will provide my solution to the exercise, and briefly guide you through it. We can discuss your own solutions in class too, but I will not be able to provide individualized feedback (and assignments will not be graded).


## Class times

Lectures take place on Tuesdays from 08-10; classroom instruction is on Wednesday from 10-12. For security reasons, I'm not going to post the room numbers to Github - you can find this via your [AU Timetable](https://timetable.au.dk).
**NOTE**: the location for October 25th is _different_ from all other weeks!

## Course overview and readings

A detailed breakdown of the course structure and the associated readings can be found in the [syllabus](syllabus/readme.md). Also, be sure to familiarize yourself with the [_studieordning_](https://eddiprod.au.dk/EDDI/webservices/DokOrdningService.cfc?method=visGodkendtOrdning&dokOrdningId=17274&sprog=en) for the course, especially in relation to examination and academic regulations. 

Make sure to read the studieording first if you have any questions relating to the course organisation, exam format, and so forth.

## Contact details

Your lecturer for this course will be [Roberta](https://pure.au.dk/portal/en/persons/roberta-rocca(079b23a2-46f6-4a00-9cd6-9a1339101208)/persons/roberta-rocca(079b23a2-46f6-4a00-9cd6-9a1339101208).html). 
If you have any problems with the course or questions that you want to ask, just get in touch.

All communication to you will be sent via Brightspace.


