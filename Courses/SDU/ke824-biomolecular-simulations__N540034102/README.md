# KE824: Biomolecular Simulations

This is the UCloud course app associated with the SDU course 'KE824: Biomolecular Simulations' ((N540034102)) taught by Himanshu Khandelia. 

This guides contains details about how to start the app on UCloud. The app is build on top of GROACS v2024.4. See the [UCloud documentation](https://docs.cloud.sdu.dk/Apps/gromacs.html) for general guidance on how to use GROMACS. 

## Starting a Job 

This app can be found in the UCloud app store by going to *Browse by category* > *Courses* > *SDU Courses* and selecting *KE824: Biomolecular Simulations* from the flavour drop-down. 

The course app is started like any other UCloud app so users should specify job name, machine type, job hours etc., like they would do for other apps. 

Like with other apps, folders from one's UCloud drives can be mounted using the *Add folder* button. Mounted folders will be available in `/work`. 

In addition to the usual GROMACS parameters (`Batch mode`, `Shell`, and `Enable tmux`), the app has the following two parameters: 
- `Simulation` (mandatory): Select the desired simulation from the drop-down menu. When the job starts, the relevant course materials will be fetched from [this](https://github.com/HimanshuKhandelia/KE824-Biomolecular-simulations) external GitHub repository and saved inside the folder `/work/<simulation-name>`.
- `Re-download simulation files` (optional): It is possible to mount a folder (created in a previous job) containing the simulation files for the chosen simulation. In this case, the simulation files are not fetched from the external GitHub repository per default. This can be changed by setting `Re-download simulation files` to `true` in which case a fresh version of the simulation files are fetched and written to the mounted folder. 

> [!NOTE]
> Using `Re-download simulation files` when a folder is mounted will irrecoverably overwrite the simulation files in the mounted folder. Files added by the user (i.e., files that are not present in the external GitHub repository) are not affected by the `Re-download simulation files` and will hence remain untouched.
