# RStudio Demo Course

This course is a demonstration of how to set up a simple UCloud course with `RStudio`.

## Submitting a UCloud Job

Follow these instructions to set up and submit a UCloud job for the course app.

For more general instructions on how to submit a job, consult the [UCloud docs](https://docs.cloud.sdu.dk/guide/submitting.html).


### Select Course Module

Choose the relevant class (module) from the dropdown menu in the UCloud job submission page.
The course materials (instructions, datasets etc.) are hosted in an external [GitHub](https://github.com/Rymik19/rStudioDemoCourse/tree/main/classes) repository.

The `analysis.R` script for `class_01` demonstrates data validation, group-wise summarization, and visualization using the `ggplot2` library.

The `example_with_new_packages.R` script for `class_02` uses `janitor` for data cleaning and `plotly` for creating interactive visualizations. These packages need to be installed in the `Dockerfile` to ensure they are pre-configured and readily available in RStudio without requiring manual installation by the user.

Once you start the course app, the course materials for the selected course module will be downloaded to the path `/work/class_<module#>`.

When the job is completed, the `class_<module#>` folder will be available in the [Jobs](https://docs.cloud.sdu.dk/guide/monitoring.html#job-completed) folder.

### Re-download Course Files

By default, this parameter is set to `false` meaning the course materials are downloaded from the external GitHub repository, except if a folder called `/work/class_[module#]` already exists.
In other words, if you select class 1 and you mount a folder called `class_01` by using the parameter _Select folders to use_, files from the external GitHub repository won't be re-downloaded.

You can overwrite the existing folder by setting the option _Re-download course files_  to `true`. This will overwrite the course material files in `/work/class_<module#>` with their newest version from the external GitHub repository. 

>[!NOTE] 
>If the mounted course folder contains other files than those being downloaded from the external GitHub repository, these will remain in the folder - even if _Re-download course files_ is set to `true`. 

### Select folders to use (optional)

You can mount a UCloud folder to the job by clicking the 'Add folder' button and selecting the folder you want to mount. The mounted folder will be available in `/work`.

Note that only changes inside `/work` will be persisted after the job is stopped.

### Initialization

For information on how to use the _Initialization_ parameter, please refer to the [Initialization - Bash script](https://docs.cloud.sdu.dk/hands-on/init-sh.html), [Initialization - Conda packages](https://docs.cloud.sdu.dk/hands-on/init-conda.html), and [Initialization - pip packages](https://docs.cloud.sdu.dk/hands-on/init-pip.html) section of the documentation.
