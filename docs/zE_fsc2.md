---
title: fastsimcoal2
theme: minima
---

# fastsimcoal2 input files

1. SFS

    The SFS used for fastsimcoal were generated as described [here](zC_sfs.md) and will be available in the Dryad repository for this project.

2. tpl files

    The tpl files used for fastsimcoal analyses under migration models are available here:

    * [low divergence](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/fsc2/Migration_1250.tpl)

    * [medium divergence](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/fsc2/Migration_5000.tpl)

    * [high divergence](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/fsc2/Migration_20000.tpl)


    The tpl files used for fastsimcoal analyses under divergence models are available here:

    * [low divergence](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/fsc2/Nomig_1250.tpl)

    * [medium divergence](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/fsc2/Nomig_5000.tpl)

    * [high divergence](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/fsc2/Nomig_20000.tpl)


3. est files

    The est files used for fastsimcoal analyses under migration models are available here:

    * [low divergence](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/fsc2/Migration_1250.est)

    * [medium divergence](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/fsc2/Migration_5000.est)

    * [high divergence](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/fsc2/Migration_20000.est)


    The est files used for fastsimcoal analyses under divergence models are available here:

    * [low divergence](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/fsc2/Nomig_1250.est)

    * [medium divergence](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/fsc2/Nomig_5000.est)

    * [high divergence](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/fsc2/Nomig_20000.est)


# SLURM scripts

All SLURM scripts used to run fsc2 IU HPC can be found [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slurm/fsc2).

# Output files

The results from fastsimcoal2 runs under migration models were summarized using the python script [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/fsc2/summarize_results.py) and results are available [here](https://github.com/meganlsmith/selectionandmigration/blob/main/results/fsc2/summary_results.csv).

The results from fastsimcoal2 runs under nomigration models were summarized using the python script [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/fsc2/summarize_results_nomig.py) and results are available [here](https://github.com/meganlsmith/selectionandmigration/blob/main/results/fsc2/summary_results_nomig.csv).


