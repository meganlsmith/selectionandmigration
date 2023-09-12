---
title: SLiM
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
First we consider a set of models with constant mutation rates, constant recombination rates, and relatively simple DFEs.  
1. Neutral  
([neutral-nomig](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/nomig_neutral_scaled.slim), [neutral-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/p1_p2_neutral_scaled.slim), [neutral-p2_p1](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/p2_p1_neutral_scaled.slim))  
2. Background Selection  
([bgs-nomig](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/nomig_bgs_scaled.slim), [bgs-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/p1_p2_bgs_scaled.slim), [bgs-p2_p1](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/p2_p1_bgs_scaled.slim))  
3. Selective Sweep in P1  
([linkedp1-nomig](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/nomig_linkedp1_scaled.slim), [linkedp1-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/p1_p2_linkedp1_scaled.slim), [linkedp1-p2_p1](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/p2_p1_linkedp1_scaled.slim))  
4. Selective Sweep in the ancestor  
([linkedancestor-nomig](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/nomig_linkedancestor_scaled.slim), [linkedancestor-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/p1_p2_linkedancestor_scaled.slim), [linkedancestor-p2_p1](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/p2_p1_linkedancestor_scaled.slim))  
5. Adaptive Introgression  
([adaptiveint-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/p1_p2_adaptiveint_scaled.slim))  

## Simulating the data

### Step 1: Sample parameters

To sample parameters, use this [python script](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/sample_parameters_slim.py).  
Parameters:

```
"-s","--slimfile", help="SLiM script to use for simulation", type="string"
"-r","--numreps", help="Number of replicates to simulate", default=1, type="int"
"-d","--divtime", help="Divergence time to use for simulations. Use scaled values.", type="int"
```
Example usage:  
```
python sample_parameters_slim.py -s p1_p2_neutral_scaled.slim -r 10000 -d 5000
```

### Step 2: Simulate data

To simulate data, use this [python script](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/neutral_tskit_to_msout_v3.py).

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
python neutral_tskit_to_msout_v3.py -d 5000 -r 10000 -s p1_p2_neutral_scaled.slim --prefix p1_p2_neutral_scaled -p p1_p2_neutral_scaled_params_5000.txt -c 24 -f neutral -x slim
```
Example usage for a no migration model:
```
python neutral_tskit_to_msout_v3.py -d 5000 -r 10000 -s nomig_neutral_scaled.slim --prefix nomig_neutral_scaled -p None -c 24 -f neutral -x slim
```

### SLURM scripts used to simulate data on the IU HPC

All SLURM scripts used to simulate data on the IU HPC can be found [here](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slurm/slim_simple))

### Output files (ms-style)

All simulated data, stored as ms-formatted output files, can be found [here](https://github.com/meganlsmith/selectionandmigration/blob/main/data/simulations/simple/)






## Distributions of Fitness Effects (Complex Models)

Next, we considered models with more realistic DFEs, variable recombination rates, and variable mutation rates. Specifically, we used the real BGS-weak CNE model from Schrider (2020). In this model, mutation rates are drawn from a range for each simlated regions. Recombination rates are based on the recombination map from the **D. melanogaster** genome and vary across simulated regions. Background selection acts in coding regions, and weaker BGS acts in constrained noncoding elements.

1. Neutral  
([neutral-nomig](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/nomig_neutral_drosophila.slim), [neutral-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/p1_p2_neutral_drosophila.slim), [neutral-p2_p1](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/p2_p1_neutral_drosophila.slim))  
2. Background Selection  
([bgs-nomig](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/nomig_bgs_drosophila.slim), [bgs-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/p1_p2_bgs_drosophila.slim), [bgs-p2_p1](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/p2_p1_bgs_drosophila.slim))  
3. Selective Sweep in P1  
([linkedp1-nomig](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/nomig_linkedp1_drosophila.slim), [linkedp1-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/p1_p2_linkedp1_drosophila.slim), [linkedp1-p2_p1](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/p2_p1_linkedp1_drosophila.slim))  
4. Selective Sweep in the ancestor  
([linkedancestor-nomig](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/nomig_linkedancestor_drosophila.slim), [linkedancestor-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/p1_p2_linkedancestor_drosophila.slim), [linkedancestor-p2_p1](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/p2_p1_linkedancestor_drosophila.slim))  
5. Adaptive Introgression  
[adaptiveint-p1_p2](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/complex/p1_p2_adaptiveint_drosophila.slim))  

## Simulating the data (Complex Models)

### Step 1: Sample parameters

To sample parameters, use this [python script](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/sample_parameters_slim.py).  
Example usage:  

```
python sample_parameters_slim.py -s slim_script -r replicates -d divergence_time
```
### Step 2: Simulate data

To simulate data, use this [python script](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/tskit_Drosophilamaps_to_msout_v2.py).  
The following files also need to be in the directory:  
* [python script for annotations](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/selRegionsFromAnno_MLS.py)  
* [drosophilaAnnotations directory](https://github.com/meganlsmith/selectionandmigration/blob/main/data/drosophilaAnnotations)  
```
-f specifies the DFE and can be neutral, sweep, or bgs.  
```
Usage for migration model:  
```
python tskit_Drosophilamaps_to_msout_v2.py -d divergence_time -r replicates -s slim_script -p parameters_file -c cores -f DFE -x slim_executable
```
Usage for no migration model:
```
python tskit_Drosophilamaps_to_msout_v2.py -d divergence_time -r replicates -s slim_script -p None -c 12 -f DFE -x slim_executable
```
