# MPI Handle Usage analysis

This repository contains the python scripts used in [TODO Link Publication] to analyze the MPI usage of applications.

## prerequisites

All python packages required are contained in the `environment.yml`.
additionally we need git and clang-format to be installed for our analysis.

## usage example

Run the analysis on all repositories:

```
mkdir repositories
./mpi_usage_analysis.py --code_locations code_locations.csv --repo_path repositories --output output.csv
``` 

Create Plots, visualizing the results:

```
mkdir visualization
./generate_plots.py --input output.csv --output_dir visualization
```

Both scripts offer ``--help`` for additional information.



For scripts in the `otherScripts` directory, one has to specify the correct python path (`export PYTHONPATH=$PYTHONPATH:$(pwd)`) or execute
them in the top level directroy.
These additional scripts have no command line parameters and are configured with
variables inside the script insetad



Some regular expressions used for analzing MPI and Hybrid MPI usage originated from https://github.com/LLNL/MPI-Usage
