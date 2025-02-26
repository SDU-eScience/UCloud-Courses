# KE824: Biomolecular Simulations

This is the UCloud course app associated with the SDU course 'KE824: Biomolecular Simulations' ((N540034102)) taught by Himanshu Khandelia. 

This guides contains details about how to start the app on UCloud. The app is build on top of GROACS v2024.4. See the [UCloud documentation](https://docs.cloud.sdu.dk/Apps/gromacs.html) for general guidance on how to use GROMACS. 

## Start a Job 

This app can be found in the UCloud app store by going to *Browse by category* > *Courses* > *SDU Courses* and selecting *KE824: Biomolecular Simulations* from the flavour drop-down. 

As always, folders from one's UCloud drives can be mounted using the *Add folder* button. Mounted folders will be available in `/work`. 

In addition to the usual GROMACS parameters (`Batch mode`, `Shell`, and `Enable tmux`), the app has the following parameters: 
- `Simulation`: Select the desired simulation from the drop-down menu. When the job starts, the relevant course materials will be fetched from [this](https://github.com/HimanshuKhandelia/KE824-Biomolecular-simulations) external GitHub repository and saved in `/work/<simulation-name>`.
- `Re-download simulation files`: It is possible to mount a folder (created in a previous job) containing the simulation files for the chosen simulation. In this case, the simulation files are not fetched from the external GitHub repository per default. This can be changed by setting `Re-download simulation files` to `true` in which case a fresh version of the simulation files are fetched and written to the mounted folder. 

```{note}
Using `Re-download simulation files` when a folder is mounted will overwrite the simulation files in the mounted folder. Files added by the user (i.e., files that are not present in the external GitHub repository) are not affected by the `Re-download simulation files`.
```
