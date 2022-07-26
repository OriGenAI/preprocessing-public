# Summary
This library handles preprocessing for training and simulation datasets. Currently only training datasets (completed eclipse cases) are supported. The **deck** and **modular** directories contain all the processing functionality built so far, including some extensions of the OriClipse library which will be used for simulation processing.
# Installation
```
poetry env use `which python3.8`
poetry shell
poetry install
```

# Training Dataset Processing

## Output
This section details the file output format.

### Globally
- common.p : contains global information about the dataset such as min and max pressure values

### Per Case
- grid_props.h5 : contains grid-specific properties such as dimensions and the active cell logic
- init_props.h5 : contains initial keyword properties like transmissibility, porosity, permeability, etc
- smry.p : contains well information and schedules, including well types (injector vs producer, etc)
- runspec.p : contains runspec keyword information, such as phases
- [X####.h5] : a series of files which contain timestep information for swat and pressure values


### File Breakdown
Details about each file in the global and per case sections

#### common.p
a pickle/serialized dictionary object containing the following
- max_pressure : float - the largest pressure value among all cases
- min_pressure : float - the smallest pressure value among all cases

#### grid_props.h5
an h5 file containing the following datasets
- logic : numpy.array - active cell matrix
- dims : numpy.array - reservoir dimensions

#### init_props.h5
an h5 file containing the following datasets
- depth : numpy.array - static depth
- permx : numpy.array - permeability in the X dimension
- permy : numpy.array - permeability in the Y dimension
- permz : numpy.array - permeability in the Z dimension
- tranx : numpy.array - transmissibility in the X dimension
- trany : numpy.array - transmissibility in the Y dimension
- tranz : numpy.array - transmissibility in the Z dimension
- poro : numpy.array - porosity values
- porv : numpy.array - pore volume values
- ntg : numpy.array - net to gross values
- dx : numpy.array - grid block size definition in X dimension
- dy : numpy.array - grid block size definition in the Y dimension
- dz : numpy.array - grid block size definition in the Z dimension

#### smry.p
a pickle/serialized dictionary object containing the following
- well_names : list - a list of strings containing all well names in the entire reservoir
- well_types : dictionary - each key is a wellname, whose value corresponds to a supported well type:
  - ECL_WELL_PRODUCER
  - ECL_WELL_WATER_INJECTOR
  - ECL_WELL_GAS_INJECTOR
- well_controls : dictionary - each key is a wellname, whose value corresponds to another dictionary with keys depending on the well's type
  - ECL_WELL_PRODUCER
    - WBHPH : borehole pressure (historical)
    - WPRH : water production rate (historical)
    - WOPRH : oil production rate (historical)
    - WGPRH : gas production rate (historical)
    - WBHP : borehole pressure
    - WOPR : oil production rate
    - WWPR : water production rate
    - WGPR : gas production rate
  - ECL_WELL_GAS_INJECTOR
    - WBHPH : borehole pressure (historical)
    - WBHP : borehole pressure
  - ECL_WELL_WATER_INJECTOR
    - WWIRH : water injection rate (historical)
    - WWIR : water injection rate 
#### X####.h5
an h5 file of a specific timestep with the following datasets
- pressure : numpy.array - the pressure value matrix
- swat : numpy.array - the swat value matrix


### Publishing

In order to publish a package to PyPi, the following steps must be followed:

- The project status that wants to be published needs to be on the private repository dev branch.
    - The project version on pyproject should be updated, or the following steps will not work.
- Push the dev branch to the dev-deploy branch
    - This will trigger a GitHub action that checks the new version, and creates an squashed commit.
    - The action will then push the squashed commit to the branch dev-release.
    - The action will also push to the dev branch on the public repository.
- On the public repository, on release creation, a new version of the repository will be pushed to PyPi.
    - The release creation will trigger a GitHub action that does this process automatically.

This process depends on having the following secrets on GitHub:
#### On the private repository:
- PUBLIC_REPO_TOKEN: Personal Access Token from GitHub. Necessary to publish to the public repository.
#### On the public repository:
- PYPI_API_TOKEN: PyPi token. Necessary to publish to PyPi.