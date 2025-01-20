# RStudio Demo Course

This course is a demonstration of how to set up a simple UCloud course with `RStudio`.

## Submitting a UCloud Job

Follow these instructions to set up and submit a UCloud job for the course.
For more general instructions on how to submit a job, consult the [UCloud docs](https://docs.cloud.sdu.dk/guide/submitting.html).


### Select Course Module

Choose the relevant class (module) from the dropdown menu in the UCloud job submission page.
The course materials (instructions and datasets) are hosted in an external [GitHub](https://github.com/Rymik19/rStudioDemoCourse/tree/main/classes) repository.

The `analysis.R` script for `class_01` demonstrates data validation, group-wise summarization, and visualization using the `ggplot2` library.

The `example_with_new_packages.R` script for `class_02` uses `janitor` for data cleaning and `plotly` for creating interactive visualizations. These packages need to be installed in the `Dockerfile` to ensure they are pre-configured and readily available in RStudio without requiring manual installation by the user.

Once you start the course app, the course materials for the selected course module will be downloaded to the path `/work/class_<module#>`.

When the job is completed, the `class_<module#>` folder will be available in your UCloud drive inside the [Jobs](https://docs.cloud.sdu.dk/guide/monitoring.html#job-completed) folder.

### Re-download Course Files

By default, this parameter is set to `false` meaning the course materials are downloaded, except if a folder called `/work/class_[module#]` already exists.
In other words, if you select class 1 and you mount a folder called `class_01` by using the parameter _Select folders to use_,
files from the teachers GitHub repos won't be re-downloaded.

You can overwrite the existing folder by setting the option _Re-download course files_  to `true`. This will overwrite `/work/class_[module#]` inside the job and the mounted UCloud storage.

### Select folders to use (optional)

You can mount a UCloud folder/directory to the job by clicking the blue button 'Add folder' and selecting the folder you want to mount.
The selected folder will be available inside the running instance of the course on the path `/work/[name_of_selected_folder]`.


> [!NOTE]
> Only changes inside `/work` will be persisted between runs.

### Initialization

For information on how to use the _Initialization_ parameter, please refer to the [Initialization - Bash script](https://docs.cloud.sdu.dk/hands-on/init-sh.html), [Initialization - Conda packages](https://docs.cloud.sdu.dk/hands-on/init-conda.html), and [Initialization - pip packages](https://docs.cloud.sdu.dk/hands-on/init-pip.html) section of the documentation.
