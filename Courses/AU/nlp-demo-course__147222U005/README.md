# NLP Demo Course

This course contains all of the code and data related to the module [Natural Language Processing](https://kursuskatalog.au.dk/en/course/107427/Natural-language-processing) taken as part of the [MSc in Cognitive Science](https://masters.au.dk/cognitivescience) at Aarhus University.

This guide will help you use the UCloud system to access course materials.

## Submitting a UCloud Job

Follow these instructions to set up and submit a UCloud job for the course.

### Machine Type

Choose a machine type that meets the computational requirements for your class:

* Classes 1 to 5: Use machines with only vCPU resources, such as `u1-standard-h` and `uc1-gc1-h`. 2-4 cores should suffice.
* Classes 7 to 9: Use machines with GPU resources for more computationally intensive tasks.

You can select the machine type from the dropdown menu when configuring your UCloud job.
### Select folders to use
The course materials (instructions and datasets) are hosted in a [GitHub](https://github.com/jeselginAU/demo-NLP-Course-AU) repository managed by the teacher. Once you start the course app, the course materials for the selected course module will be downloaded to the path `/work/class_[module#]`.

To persist your changes between job runs, you need to mount a folder/directory in your UCloud storage to the job. 
Click 'Add folder' and select the folder you want to mount. 
The selected folder will be available inside the running instance of the course on the path `/work/[name_of_selected_folder]`.
Only changes inside this folder will be persisted between runs. 

**Note that if you need to save changes to the course materials, you should copy/move the `class_[module#]` into your mounted folder.**

Mount the same folder in a later run to access your data.

### Select Course Module

Choose the relevant class (module) from the dropdown menu in the UCloud job configuration interface. 

Ensure you select the correct module to access the corresponding materials.

### Re-download Course Files
If you mount a folder to the job called `class_[module#]` with module# corresponding to the selected module (e.g., you select class 1 and you mount a folder called `class_01`), files from the teachers GitHub repos won't be downloaded unless you set this optional parameter to `true`.

* Set this option to `true` **if updates have been made to the repository** and you need the latest materials. This will overwrite your files at `/work/class_[module#]` inside the job 

* By default, this is set to `false`, meaning the course materials are downloaded only if no folder exists at `/work/class_[module#]`.

### Initialization

For information on how to use the _Initialization_ parameter, please refer to the [Initialization - Bash script](https://docs.cloud.sdu.dk/hands-on/init-sh.html), [Initialization - Conda packages](https://docs.cloud.sdu.dk/hands-on/init-conda.html), and [Initialization - pip packages](https://docs.cloud.sdu.dk/hands-on/init-pip.html) section of the documentation.
