---
title: Alignments
theme: minima
---

# Python script

To construct the alignments from the ms-style output files, use this [python script](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/bpp/msout_to_phylip.py).


Parameters:
```
"-m","--msout", help=".msOut file in msformat including position information in decimal format.", type="string"
"-l","--length", help="Length of sequences to output.", type="int"
"-n", "--number", help="Number of simulated loci to process.", type="int"
"-o","--outputphylip", help="Destination of output phylip files.", type="string"
```

Example usage:  
```
python msout_to_phylip.py -m p1_p2_adaptiveint.msOut -l 500 -n 1500 -o ./alignments/SLiM-testing-redo/p1_p2_adaptiveint_1250_phy
```


# SLURM scripts

All SLURM scripts used to build alignments on the IU HPC can be found [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slurm/alignments).

# Output files

All alignments will be deposited into the Dryad repository for this project.
 