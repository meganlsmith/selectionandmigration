---
title: SLiM (Complex)
theme: minima
---

# Complex Models

## Programs
We used the following program versions:
1. SLiM v4.0.1
2. pyslim v1.0.3
3. tskit v0.5.5

## Demographic models
1. No migration (nomig)
2. Migration P1 -> P2 (p1_p2)
3. Migration P2 -> P1 (p2_p1)  

## Distributions of Fitness Effects
1. Neutral  
([neutral-nomig](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/nomig_neutral_drosophila.slim), [neutral-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/complex/slim/simple/p1_p2_neutral_drosophila.slim), [neutral-p2_p1](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/p2_p1_neutral_drosophila.slim))  
2. Background Selection  
([bgs-nomig](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/nomig_bgs_drosophila.slim), [bgs-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/p1_p2_bgs_drosophila.slim), [bgs-p2_p1](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/p2_p1_bgs_drosophila.slim))  
3. Selective Sweep in P1  
([linkedp1-nomig](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/nomig_linkedp1_drosophila.slim), [linkedp1-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/p1_p2_linkedp1_drosophila.slim), [linkedp1-p2_p1](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/p2_p1_linkedp1_drosophila.slim))  
4. Selective Sweep in the ancestor  
([linkedancestor-nomig](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/nomig_linkedancestor_drosophila.slim), [linkedancestor-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/p1_p2_linkedancestor_drosophila.slim), [linkedancestor-p2_p1](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/p2_p1_linkedancestor_drosophila.slim))  
5. Adaptive Introgression  
([adaptiveint-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/p1_p2_adaptiveint_drosophila.slim))  

## Simulating the data

### Step 1: Sample parameters

To sample parameters, use this [python script](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/slim/sample_parameters_slim.py).  
Parameters:

```
"-s","--slimfile", help="SLiM script to use for simulation", type="string"
"-r","--numreps", help="Number of replicates to simulate", default=1, type="int"
"-d","--divtime", help="Divergence time to use for simulations. Use scaled values.", type="int"
```
Example usage:  
```
python sample_parameters_slim.py -s p1_p2_neutral_drosophila.slim -r 10000 -d 5000
```

### Step 2: Simulate data

To simulate data, use this [python script](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/slim/tskit_Drosophilamaps_to_msout_v2.py).
Note: To run this, you must also have available the selRegionsFromAnnot_MLS.py script, along with the folder 'drosophilaAnnotations'.

Parameters:
```
"-s","--slimfile", help="SLiM script to use for simulation", type="string"
"-r","--numreps", help="Number of replicates to simulate", default=1, type="int"
"-p","--paramsfile", help="Migration model parameters, if relevant. Default is None for divergence only.", type="string"
"-d","--divtime", help="Divergence time to use for simulations. Use scaled values.", type="int"
"-x","--slimexecutable", help="Path to slim executable", default="slim", type="str"
"-c","--processors", help="Number of processors to use", default=1, type="int"
"-f","--dfe", help="What DFE was used? neutral, bgs, or sweep", type="string"
"-o","--previous", help="Number of replicates previously simulated", default=0, type="int"
"--prefix", help="Prefix for naming file", type="string"
```
Example usage for a migration model:  
```
python tskit_Drosophilamaps_to_msout_v2.py -d 5000 -r 10000 -s p1_p2_neutral_drosophila.slim --prefix p1_p2_neutral_drosophila -p p1_p2_neutral_drosophila_params_5000.txt -c 24 -f neutral -x slim
```
Example usage for a no migration model:
```
python tskit_Drosophilamaps_to_msout_v2.py -d 5000 -r 10000 -s nomig_neutral_drosophila.slim --prefix nomig_neutral_drosophila -p None -c 24 -f neutral -x slim
```

### SLURM scripts used to simulate data on the IU HPC

All SLURM scripts used to simulate data on the IU HPC can be found [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slurm/slim_complex).

### Output files (ms-style)

All simulated data, stored as ms-formatted output files, are available from Figshare (DOI: 10.6084/m9.figshare.24354277).
Parameters files are also available from Figshare (DOI: 10.6084/m9.figshare.24354277).
