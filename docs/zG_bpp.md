---
title: BPP
theme: minima
---

# Input files

1. Control file
    A [template control file](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/bpp/A00_variable_heredity_longer.bpp.ctl) is used by the python script for submitting BPP jobs.

# Create alignments
1. Create alignments using these four scripts:
    [Uniform](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slurm/bpp/create_alignments_slim.sh)
    [Uniform-adaptive](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slurm/bpp/create_alignments_adaptive_slim.sh)
    [Complex](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slurm/bpp/create_alignments_drosophila.sh)
    [Complex-adaptive](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slurm/bpp/create_alignments_adaptive_drosophila.sh)

# Python scripts


To submit BPP jobs use this [python script](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/bpp/run_bpp_heredity_longer_v1a.py). This script uses a template contro lfile available [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/bpp/A00_variable_heredity_longer.bpp.ctl).

Parameters:
```
"-a","--alignmentfolder", help="folder with phylip formatted alignments.", type="string"
"-o","--outputfolder", help="Destination of bpp input files.", type="string"
"-p","--outputfolder2", help="Destination of bpp output files.", type="string"
"--prefix", help="Prefix for naming output files.", type="string"
```

Example usage:  
```
python python_scripts/run_bpp_heredity_longer_v1a.py -a ./bpp_alignments/ --outputfolder ./bpp_ctl/ --outputfolder2 ./bpp_output/ --prefix nomig_neutral_scaled_1250
```

# Command

The python commands used to run BPP on datasets with a simple genomic architecture are available [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/bpp/submit_bpp_slim.sh).

The python commands used to run BPP on datasets with a complex genomic architecture are available [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/bpp/submit_bpp_drosophila.sh).

# Output files

All alignments are available on Figshare (DOI: 10.6084/m9.figshare.24354277).

The results from BPP runs were summarized using the python script [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/bpp/process_results_heredity_longer.py) and results are available [here](https://github.com/meganlsmith/selectionandmigration/blob/main/results/bpp/all_results_heredity_longer.csv).

