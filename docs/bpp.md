---
title: BPP
theme: minima
---

# Input files

1. Alignments 
    The alignments used for BPP were generated as described [here](https://github.com/meganlsmith/selectionandmigration/blob/main/docs/alignments.md) and will be available in the Dryad repository for this project.

2. Control file
    A [template control file](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/bpp/A00_variable.bpp.ctl) is used by the python script for submitting BPP jobs.


# Python scripts


To submit BPP jobs under BGS and neutral models use this [python script](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/bpp/run_bpp_v1a.py).

Parameters:
```
"-a","--alignmentfolder", help="folder with phylip formatted alignments.", type="string"
"-o","--outputfolder", help="Destination of bpp input files.", type="string"
"-p","--outputfolder2", help="Destination of bpp output files.", type="string"
"--prefix", help="Prefix for naming output files.", type="string"
```

Example usage:  
```
python run_bpp_v1a.py -a nomig_bgs_1250_500bp_phy/ -o ./bpp_input/ -p ./bpp_output/ --prefix nomig_bgs_scaled_1250
```

To submit BPP jobs under sweep models use this [python script](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/bpp/run_bpp_adaptive_v1a.py).

Parameters:
```
"-a","--alignmentfolder", help="folder with phylip formatted alignments.", type="string"
"-b","--backgroundfolder", help="folder with phylip formatted background alignments.", type="string"
"-o","--outputfolder", help="Destination of bpp input files.", type="string"
"-p","--outputfolder2", help="Destination of bpp output files.", type="string"
"--prefix", help="Prefix for naming output files.", type="string
"--percent", help="Percent adaptive to sample.", type="string"
```

Example usage:  
```
python run_bpp_adaptive_v1a.py  -a nomig_linkedp1_1250_phy/ -b nomig_bgs_1250_500bp_phy/ -o bpp_input/SLiM-testing-redo/ -p bpp_output/SLiM-testing-redo/ --prefix nomig_linkedp1_1250_5percent --percent 5
```

# Command

The python commands used to run BPP on datasets with a simple genomic architecture are available [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/bash/bpp/simple_bpp.sh).

The python commands used to run BPP on datasets with a complex genomic architecture are available [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/bash/bpp/complex_bpp.sh).

# Output files

To summarize BPP results, use this [python script](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/bpp/process_results.py).

The results from BPP runs under nomigration models were summarized using the python script [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/bpp/process_results.py) and results are available [here](https://github.com/meganlsmith/selectionandmigration/blob/main/results/BPP/all_results.csv).

