---
title: SFS
theme: minima
---

# Python script

To construct the SFS for neutral and bgs cases, use this [python script](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/makesfs.py).

To construct the SFS for sweep cases, use this [python script](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/makesfs_adaptive.py).

Parameters for neutral/bgs cases:
```
'--input', dest="input", type=str, help='an input folder with msout files.'
'--output1', dest="output1", type=str, help='an output folder for dadi formatted files.'
'--output2', dest="output2", type=str, help='an output folder for fsc formatted files.'
'--reps', dest="reps", type=int, help='Number of replicates to perform.'
'--npop0', dest="npop0", type=int, help='Number of samples from population 0.'
'--npop1', dest="npop1", type=int, help='Number of samples from population 1.'
'--max', dest="max", type=int, default=math.inf, help="Maximum number of simulated fragments to include (will include first n fragments"
'--length', dest="length", type=int, help="Length of simulated fragments."
```
Example usage for neutral/bgs cases:  
```
python makesfs.py --input nomig_neutral_scaled_1250/ --output1 dadi/nomig_neutral_scaled_1250/ --output2 fsc/nomig_neutral_scaled_1250/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
```

Parameters for adaptive cases:
```
'--input', dest="input", type=str, help='an input folder with msout files.')
'--output1', dest="output1", type=str, help='an output folder for dadi formatted files.')
'--output2', dest="output2", type=str, help='an output folder for fsc formatted files.')
'--reps', dest="reps", type=int, help='Number of replicates to perform.')
'--npop0', dest="npop0", type=int, help='Number of samples from population 0.')
'--npop1', dest="npop1", type=int, help='Number of samples from population 1.')
'--max', dest="max", type=int, default=math.inf, help="Maximum number of simulated fragments to include (will include first n fragments")
'--maxadapt', dest="maxadapt", type=int, default=math.inf, help="Maximum number of simulated adaptive fragments to include (will include first n fragments")
'--percent', dest="percent", type=int, help="The percent of SNPs drawn from the input file. The remaining up to max will be drawn from the background file.")
'--background', dest="background", type=str, help="Background file for drawing 100 minus percent of the SNPs.")
'--length', dest="length", type=int, help="Length of simulated fragments.")

```
Example usage for adaptive cases:  
```
python makesfs_adaptive.py --input nomig_linkedp1_scaled_1250/ --output1 dadi/nomig_linkedp1_scaled_1250_5percent/ --output2 fsc/nomig_linkedp1_scaled_1250_5percent/ --reps 100 --npop0 20 --npop1 20 --max 10000 --maxadapt 1500 --percent 5 --background nomig_bgs_scaled_1250/ --length 10000
```

# SLURM scripts

All SLURM scripts used to simulate data on the IU HPC can be found [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slurm/sfs).

# Output files

All SFS will be deposited into the Dryad repository for this project.
 