---
title: FILET
theme: minima
---

# Testing Datasets

1. msmove

    To simulate data in msmove, we first draw parameters using a [python script](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/sample_parameters_msmove.py).  
    Parameters:
    ```
    -t theta
    -p rho
    -w window window_size
    -r replicates
    -m model nomig, mig12, mig21
    -i introgression (flag used when there is introgression)
    -d divergence time (in msmove units)
    ```
    Usage:  
    ```
    python sample_parameters_msmove.py -t theta -p rho -w window_size -r replicates -m model -i -d divergence_time
    ```  

    Then, we simulate the data in msmove. Examples for each model are provided below.  
    ```
    msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 -ev tbs 1 2 tbs < mig12_params_50_250_10000_0.25.txt > ./div25/trainingSims_neutral/mig12.msOut
    msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 -ev tbs 2 1 tbs < mig21_params_50_250_10000_0.25.txt > ./div25/trainingSims_neutral/mig21.msOut
    msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 < nomig_params_50_250_10000_0.25.txt > ./div25/trainingSims_neutral/noMig.msOut
    ```

2. FILET (Simple)

    All FILET datasets are simulated as described in the [FILET page](filet.md).  
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

To simulate data in ms matching $\pi$ in th training data, use this [python script](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/msmove_matchpi.py).  
Arguments:  

```
-t starting point for theta
-p starting point for rho
-w window size to use in simulation
-r replicates
-d divergence time (in msmove units)
-i path to slim feature vector (see below)
-o folder to store msmove output
-s suffix for naming files
-m path to msmove
-f path to FILET scripts
```  
Usage:  

```
python msmove_matchpi.py -t theta -p rho -w window_size -r replicates -d divergence_time -i feature_vector -o output_directory -s prefix -m path_to_msmove -f path_to_FILET
```

# Calculating summary statistics

First, create a directory that contains properly formatted ms-style data for each of the training models. There should be one file per model. To combine all simulations into a single, properly formatted file, follow the example below. You can find the msmovecommand.txt file [here](https://github.com/meganlsmith/selectionandmigration/blob/main/data/msmovecommand.txt).

```
# in this example, all *ms.out files for the p1_p2 background selection simulations with divergence time 1250 are stored in p1_p2_bgs_drosophila_1250.
cd ./p1_p2_bgs_drosophila_1250/ # change directories
cat p1_p2_bgs_drosophila_{1..10000}_overlaid_ms.out > pre_p1_p2_bgs.msOut # concatenate the relevant files
cat ../msmovecommand.txt pre_p1_p2_bgs.msOut > p1_p2_bgs.msOut # add the first line that would be output in msmove (FILET uses this information)
rm pre_p1_p2_bgs.msOut # remove the unecessary intermediate file
cp p1_p2_bgs.msOut ../testingSims_1250/ # copy to a new directory.
cd ../
```

Do this for all models, and store all results in testingSims_1250. If some models have different numbers of simulations, then you will need to change msmovecommand.txt to reflect that.  

Next, calculate the statistics using the following bash code:

```
n1=20 # population one size
n2=20 # population two size
windowSize=10000 # window size




# Calculate summary statistics

for inFile in `ls testingSims_1250/ | grep .msOut` ; do cat testingSims_1250/$inFile | ./FILET-master/twoPopnStats_forML $n1 $n2 | python ./FILET-master/normalizeTwoPopnStats.py None $windowSize > testingSimsStats_1250/$inFile; done
```
The statistics are now stored in testingSimsStats_1250. Do this for all divergence times and SLiM models.

# Classifiers
We constructed classifiers for each of the training datasets, using the following summary statistics and scripts from Schrider et al. (2018):
