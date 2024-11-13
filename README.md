# Courses on UCloud 

This repository contains all the necessary information about how teachers at Danish universitites can request, create, and develop a course to be deployed on UCloud. 

Please read this document in full before requesting a UCloud course.

> [!NOTE]
> Below, the term <ins>university course</ins> refers to the university-approved course while <ins>UCloud course</ins> refers to the course deployment on UCloud.

**Table of contents**

- [What is UCloud Courses?](./README.md#what-are-ucloud-courses)
- [Requirements and General Considerations](./README.md#requirements-and-general-considerations)
    - [Basic requirements](./README.md#basic-requirements)
    - [Course development requirements](./README.md#course-development-requirements)
    - [Course maintainance and update](./README.md#course-maintainance-and-update)
    - [Removing a course from UCloud](./README.md#after-a-ucloud-course-is-completed) 
- [Outline of Services Offered](./README.md#outline-of-services-offered)
    - [How to request a UCloud Course](./README.md#how-to-request-a-ucloud-course)
    - [The Financial Model](./README.md#the-financial-model)


## What is a UCloud Course?

The idea behind UCloud courses is to wrap all the relevant course material - software packages, notebooks, scripts etc. - for a given university course in a stand-alone UCloud app. This allows students to access the full material quickly and seamlessly without having to install any software themselves.

UCloud courses are built as [Docker](https://www.docker.com/) images, starting from pre-existing UCloud base images such as JupyterLab, RStudio, Conda, Ubuntu, Linux virtual desktops etc. 

Once a UCloud course has been deployed it will be available under the *Courses* category card in the UCloud [app store](https://docs.cloud.sdu.dk/guide/browsing.html). The courses are then divided by university. To select a course which run e.g. in Aarhus (AU), a UCloud user needs to click the AU Course card and selects the given course and version from the drow-down menus. 

## Requirements and General Considerations

Before requesting  a new UCloud course there are some requirements that the course and teacher must meet and some general considerations to keep in mind.

### Basic requirements  

The following requirements must be met: 

1. The UCloud course is associated with a university course, which is already existing, or planned and approved to take place in the foreseeable future.  
2. The course is for students enrolled at a Danish university.
3. The teacher is employed at a post-PhD level (i.e., postdoc, assistant/associate/full professor, or equivalant).

### Course development requirements

The development of UCloud courses should be done by the teacher using the pre-made scripts available in the [public](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories#about-repository-visibility).

This entails that:

1. All material in this repositiry will be publicly available.
2. Teachers must consent to their material being, and remaining, publicly available in the repository.  
3. Teachers should **never** include datasets and other potentially sensitive information in the GitHub repository. 
    - Datasets etc., must always be handled seperately, for example in a decicated [UCloud Project](https://docs.cloud.sdu.dk/guide/project-intro.html).
4. UCloud courses can be used by other teachers, beside the developers.

Once a UCloud course has been deployed, it will be avaible to all Danish universities.

### Course maintainance and update

The teacher is responsible for providing a short guide on how to use the UCloud course (for students) and to update the UCloud course when necessary. 
As a general rule, UCloud courses are only updated before the beginning of each spring- and fall semesters. Potential bugs are fixed continuously. 

When the university course is completed, the corresponding UCloud course will remain available on UCloud by default. This will allow the teacher to update and reuse the material in later semesters, and make it possible for other teachers to use the material as well. 

### Removing a course from UCloud

The teacher who developed the course can request to have the UCloud course removed from UCloud. When the request for removal has been approved, the UCloud course in question will be scheduled for removal and will be marked as such. The removal will only take place in the next [bi-annual update](#ucloud-courses-are-updated-bi-annually) to ensure that any ongoing use of the UCloud course by others can be completed before the removal.

>[!IMPORTANT] 
> It is never possible to remove materials from this GitHub repository. Thus, the removal of a UCloud course from UCloud will *not* be followed by a removal of the corresponding material from this GitHub repository. 

## Outline of Services Offered 

The relevant UCloud support staff will assist the teachers in the development of the UCloud course. This support includes:

- Support during development of the UCloud course (course design, docker container preparation).
- Review of the final material produced by teachers (mandatory).
- Deployment of the UCloud course on the UCloud platform (mandatory).

### How to request a UCloud Course

A teacher can request a UCloud course by sending an e-mail to [escience@sdu.dk](mailto:escience@sdu.dk) where they write that they are requesting a UCloud course. The e-mail will be forwarded to the teacher's university where it will be processed by relevant support staff. 

When the request for a UCloud course has been received, a meeting will be organized between the teacher and the relevant support staff. The purpose of this meeting is to discuss the following:

- The software requirements for the UCloud course.
- The resource (compute/storage) requirements for the course and how to get them. 
- The support requirements of the teacher.
- The estimated cost (see [below](#the-financial-model)).

Other topics will be discussed as needed. 

### The Financial Model

The teacher's department/university must pay for the work done by the support staff in supporting the teacher with the UCloud course development, maintenance, update etc. 

Pricing examples will be added here later. 
