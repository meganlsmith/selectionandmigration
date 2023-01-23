---
title: FILET
theme: minima
---

# Testing Datasets

1. msmove

2. FILET (Simple)
    * Neutral
    * Background Selection
    * Selective Sweep in P1 (in 5, 10, 15% of loci)
    * Selective Sweep in the ancestor (in 5, 10, 15% of loci)
    * Adaptive Introgression (in 5, 10, 15% of loci)

2. FILET (Complex)
    * Neutral
    * Background Selection
    * Selective Sweep in P1 (in 5, 10, 15% of loci)
    * Selective Sweep in the ancestor (in 5, 10, 15% of loci)
    * Adaptive Introgression (in 5, 10, 15% of loci)

# Training Datasets

1. msmove

2. FILET (Simple)
    * Neutral
    * Background Selection
    * Selective Sweep in P1 (in 5, 10, 15% of loci)
    * Selective Sweep in the ancestor (in 5, 10, 15% of loci)
    * Adaptive Introgression (in 5, 10, 15% of loci)

3. FILET (Complex)
    * Neutral
    * Background Selection
    * Selective Sweep in P1 (in 5, 10, 15% of loci)
    * Selective Sweep in the ancestor (in 5, 10, 15% of loci)
    * Adaptive Introgression (in 5, 10, 15% of loci)

4. msmove (match $\pi$)
    ```
        -t starting point for theta
        -p starting point for rho
        -w window size to use in simulation
        -r number of replicates
        -d divergence time (in msmove units)
        -i path to slim feature vector (see below)
        -o folder to store msmove output
        -s suffix for naming files
        -m path to msmove
        -f path to FILET scripts
    ```
    ```
    python msmove_matchpi.py -t theta -p rho -w window_size -r replicates -d divergence_time -i feature_vector -o output_directory -s prefix -m path_to_msmove -f path_to_FILET
    ```

# Calculating summary statistics

```
bash testingstats_SLiM_drosophila_1250.sh
```


# Classifiers
We constructed classifiers for each of the training datasets, using the following summary statistics and scripts from Schrider et al. (2018):
