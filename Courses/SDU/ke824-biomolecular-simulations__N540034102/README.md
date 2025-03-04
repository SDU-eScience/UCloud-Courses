# KE824: Biomolecular Simulations

This is the UCloud course app associated with the SDU course 'KE824: Biomolecular Simulations' (N540034102) taught by Himanshu Khandelia. 

This guides contains details about how to start the app on UCloud. The app is build on top of GROMACS v2024.4. See the [UCloud documentation](https://docs.cloud.sdu.dk/Apps/gromacs.html) for general guidance on how to use GROMACS. 

## Starting a Job on UCloud

In addition to the usual GROMACS parameters (`Batch mode`, `Shell`, and `Enable tmux`), the app has the following two parameters: 
- `Simulation` (mandatory): Select the desired simulation from the drop-down menu. When the job starts, the relevant course materials will be fetched from [this](https://github.com/HimanshuKhandelia/KE824-Biomolecular-simulations) external GitHub repository and saved inside the folder `/work/<simulation-name>`. This means that you DO NOT need to download the files from itslearning and upload them on UCloud. All the requisite files will automatically be downloaded when your job is allocated resources

- `Re-download simulation files` (optional): It is possible to mount a folder (created in a previous job) containing the simulation files for the chosen simulation. In this case, the simulation files are not fetched from the external GitHub repository per default. This can be changed by setting `Re-download simulation files` to `true` in which case a fresh version of the simulation files are fetched and written to the mounted folder. This option is important because it enables you to continue working on an existing simulation which was not completed in the previous UCloud job or class. 

> [!NOTE]
> When using the option `Re-download simulation files`, Simulation folders included in a mounted folder will be irrecoverably overwritten. Files added by the user (i.e., files that are not present in the external GitHub repository, and are not part of the selected Simulation) are not affected by the Re-download simulation files and will hence remain untouched.
