# Courses on UCloud 

This repository contains all the necessary information about how teachers at Danish universitites can request, create, and develop a course to be deployed on UCloud. 

Please read this document in full before requesting a UCloud course.

Below, the term <ins>university course</ins> refers to the university-approved course while <ins>UCloud course</ins> refers to the course deployment on UCloud.

**Table of contents**

1. [What are UCloud Courses?](./README.md#what-are-ucloud-courses)
2. [Requirements and General Considerations](./README.md#requirements-and-general-considerations)
    1. [Course- and teacher requirements](./README.md#course--and-teacher-requirements)
    2. [Course materials on GitHub are public](./README.md#course-materials-on-github-are-public)
    3. [The teacher is the developer](./README.md#the-teacher-is-the-developer)
    4. [UCloud courses are updated bi-annually](./README.md#ucloud-courses-are-updated-bi-annually)
    5. [After a UCloud course is completed](./README.md#after-a-ucloud-course-is-completed) 
3. [Outline of Services Offered](./README.md#outline-of-services-offered)
    1. [How to request a UCloud Course](./README.md#how-to-request-a-ucloud-course)
    2. [The Financial Model](./README.md#the-financial-model)


## What are UCloud Courses?

The idea behind UCloud courses is to wrap all the relevant course material - software packages, notebooks, scripts etc. - for a given university course in a stand-alone UCloud app. This allows for quick and seamless access to the material to the students. 

UCloud courses are built as [Docker](https://www.docker.com/) images on top of a relevant, existing UCloud base image such as JupyterLab, RStudio, Conda, Ubuntu, Linux virtual desktops etc. 

Once a UCloud course has been deployed it will be available under the *Courses* category card in the UCloud [app store](https://docs.cloud.sdu.dk/guide/browsing.html). Behind this card is one Course card per university. To select a course from, say, AU, a UCloud user clicks the AU Course card and selects the given course. 

## Requirements and General Considerations

Before requesting  a new UCloud course there are some requirements that the course and teacher must meet and some general considerations to keep in mind.

### Course- and teacher requirements  

The following requirements must be met: 

1. The UCloud course is associated with a university course, which is already existing, or planned and approved to take place in the foreseeable future.  
2. The course is for students enrolled at a Danish university.
3. The teacher is employed at a post-PhD level (i.e., postdoc, assistant/associate/full professor, or equivalant).

### Course materials on GitHub are public

UCloud courses are developed in this GitHub repository which is [public](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories#about-repository-visibility). This entails that:

1. The UCloud course will be public.
2. Teachers must consent to their material being, and remaining, publicly available in the repository.  
3. Teachers should **never** include datasets and other potentially sensitive information in the GitHub repository. 
    - Datasets etc., must always be handled seperately, for example in a decicated [UCloud Project](https://docs.cloud.sdu.dk/guide/project-intro.html).
4. UCloud courses can be used by other teachers, beside the developers.

### The teacher is the developer 

The development of UCloud courses should be done by the teacher using the pre-made scripts available in this repository. Once a UCloud course has been deployed, it will be avaible to all Danish universities. 

The teacher is responsible also for providing a short guide on how-to-use the UCloud course (for students) and to the update of the UCloud course when necessary. 

### UCloud courses are updated bi-annually 

As a general rule, UCloud courses are only updated before the beginning of each spring- and fall semesters. Potential bugs are fixed continuously. 

### After a UCloud course is completed 

When the university course is completed, the corresponding UCloud course will remain available on UCloud by default. This will allow the teacher to update and reuse the material in later semesters, and make it possible for other teachers to use the material as well. 

The teacher who developed the course can request to have the UCloud course removed from UCloud. When the request for removal has been approved, the UCloud course in question will be scheduled for removal and will be marked as such. The removal will only take place in the next [bi-annual update](./README.md#ucloud-courses-are-updated-bi-annually) to ensure that any ongoing use of the UCloud course by others can be completed before the removal.

> It is never possible to remove materials from this GitHub repository. Thus, the removal of a UCloud course will *not* be followed by a removal of the corresponding material from the GitHub repository. 

## Outline of Services Offered 

The relevant UCloud support staff will assist the teachers in the development of the UCloud course. This support includes:

- Support during development of the UCloud course.
- Review of the final material produced by teachers.
- Deploying the UCloud course on the UCloud platform.

When a teacher requests a UCloud course (see below), a meeting will be scheduled to discuss, among other things, the specific needs that the teacher has regarding support in the development process.  

### How to request a UCloud Course

A teacher can request a UCloud course by sending an e-mail to [escience@sdu.dk](mailto:escience@sdu.dk) where they write that they are requesting a UCloud course. The e-mail will be forwarded to the teacher's university where is will be processed by relevant support staff. 

When the request for a UCloud course has been received, a meeting will be organized between the teacher and the relevant support staff. The purpose of this meeting is to discuss the following:

- The software requirements for the UCloud course.
- The resource (compute/storage) requirements for the course and how to get them. 
- The support requirements of the teacher.
- The estimated cost (see [below](./README.md#the-financial-model)).

Other topics will be discussed as needed. 

### The Financial Model

The teacher's department (or similar) must pay for the work done by the support staff in supporting the teacher with the UCloud course development, maintenance, update etc. 

Pricing examples will be added here later. 





## Teacher Agreement 

As a teacher and course responsible for [insert course title], I hereby declare that I have read, understood, and consent to the information (terms and conditions?) provided above. In particular, I am aware that that it is my responsibility to ensure that data is shared with students in compliance with the rules specified in [GDPR, internal guidelines etc.]. 

[TO BE CONTINUED ...]
Repository for the development and collection of UCloud courses


