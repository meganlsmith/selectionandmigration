---
title: ∂a∂i
theme: minima
---

# ∂a∂i input files

1. SFS

    The SFS used for ∂a∂i were generated as described [here](https://github.com/meganlsmith/selectionandmigration/blob/main/docs/zC_sfs.md) and will be available in the Dryad repository for this project.

# python scripts

To run ∂a∂i, use the appropriate python script:

1. Migration models
* For the low divergence case use the python script [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/dadi/run_dadi.py)
* For the medium divergence case use the python script [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/dadi/run_dadi_5k.py)
* For the high divergence case use the python script [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/dadi/run_dadi_20k.py)

2. No migration models
* For the low divergence case use the python script [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/dadi/run_dadi_nomig.py)
* For the medium divergence case use the python script [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/dadi/run_dadi_5k_nomig.py)
* For the high divergence case use the python script [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/dadi/run_dadi_20k_nomig.py)

Parameters:
```
"--input", help="an input folder with sfs files", type="string"
"--output", help="an output folder", type="string"
"--prefix", help="a prefix for naming output", type="string"
```
Example usage:  
```
python run_dadi.py --input nomig_neutral_scaled_1250/ --output dadi_results/ --prefix nomig_neutral_scaled_1250
```


# SLURM scripts

All SLURM scripts used to run ∂a∂i IU HPC can be found [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slurm/dadi).

# Output files

The results from ∂a∂i runs under migration models were summarized using the python script [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/dadi/summarize_dadi.py) and results are available [here](https://github.com/meganlsmith/selectionandmigration/blob/main/results/dadi/results_summary.csv).

The results from ∂a∂i runs under nomigration models were summarized using the python script [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/dadi/compare_models.py) and results are available [here](https://github.com/meganlsmith/selectionandmigration/blob/main/results/dadi/dadi_LRT_results.csv).


