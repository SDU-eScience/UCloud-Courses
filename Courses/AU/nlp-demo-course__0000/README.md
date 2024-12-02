# NLP Demo Course

This course contains all of the code and data related to the module Natural Language Processing taken as part of the [MSc in Cognitive Science](https://masters.au.dk/cognitivescience) at Aarhus University.

This guide will help you use the UCloud system to access course materials.

## Submitting a UCloud Job

Follow these instructions to set up and submit a UCloud job for the course.

### Machine Type

Choose a machine type that meets the computational requirements for your class:

* Classes 1 to 5: Use machines with only vCPU resources, such as `u1-standard-1`.
* Classes 7 to 9: Use machines with GPU resources for more computationally intensive tasks.

You can select the machine type from the dropdown menu when configuring your UCloud job.

### Select Course Module

Choose the relevant class (module) from the dropdown menu in the UCloud job configuration interface.

Ensure you select the correct module to access the corresponding materials.

## Optional Parameters

### Re-download Course Files

The course materials are hosted in a [GitHub](https://api.github.com/repos/jeselginAU/demo-NLP-Course-AU) repository.

* Set this option to `true` **if updates have been made to the repository** and you need the latest materials.

> [!NOTE]
> If true, existing files in your class folder will be overwritten.

* By default, this is set to `false`, meaning the course materials are downloaded only once when a new job is created.

### Initialization

For information on how to use the _Initialization_ parameter, please refer to the [Initialization - Bash script](https://docs.cloud.sdu.dk/hands-on/init-sh.html), [Initialization - Conda packages](https://docs.cloud.sdu.dk/hands-on/init-conda.html), and [Initialization - pip packages](https://docs.cloud.sdu.dk/hands-on/init-pip.html) section of the documentation.
