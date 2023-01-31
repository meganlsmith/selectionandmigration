---
title: Simulations
theme: minima
---

NOTE TO SELF: DO I NEED TO REDO SOME THINGS WITH THE ORIGNAL SLIM MODELS SINCE DATASETS WERE DIFFERENT SIZES, AND I SIMULATED MORE DATA TO FIX THIS ISSUE?

# msmove  (DONE and in Organized)

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

    We used bash scripts to simulate the [training](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/bash/simdata_msmove.sh) and [testing](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/bash/simdata_msmove_testing.sh) data using the above commands.

    Output:
        ./div25/testingSims_neutral
        ./div25/trainingSims_neutral
        ./div1/testingSims_neutral
        ./div1/trainingSims_neutral
        ./div4/testingSims_neutral
        ./div4/terainingSims_neutral

# FILET (Simple) 

NOTES: Is there an issue with the neutral 1250 simulations when continued? (maybe didn't use correct params file?)
        Running 1000 more simulations for adaptive introgression scenarios.

    To simulate data in FILET, we first draw parameters using a [python script](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/sample_parameters_slim.py).
    Parameters:
    ```
    -s slim script to use in simulations
    -r replicates
    -d divergence time (in msmove units)
    ```
    Usage:  
    ```
    python sample_parameters_slim.py -s p1_p2_bgs_scaled.slim -r 10000 -d 1250
    ```  

    Then, we simulate data in msmove using this [python script](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/python/neutral_tskit_to_msout_v2.py). 
    Parameters:
    ```
    -s SLiM script to use for simulation.
    -r Number of replicates to simulate.
    -p File with migration model parameters, if relevant. Default is None for divergence only.
    -d Divergence time to use for simulations.
    -x Path to slim executable.
    -c Number of processors to use.
    -f What DFE was used? neutral, bgs, or sweep.
    ```
    Example usages for each migration model with BGS and divergence time = 1250:  
    ```
    python neutral_tskit_to_msout_v2.py -d 1250 -r 2000 -s p1_p2_bgs_scaled.slim -p p1_p2_bgs_scaled_params_1250.txt -c 12 -f bgs -x /N/u/mls16/Carbonate/Programs/SLiM-build/slim
    python neutral_tskit_to_msout_v2.py -d 1250 -r 2500 -s p2_p1_bgs_scaled.slim -p p2_p1_bgs_scaled_params_1250.txt -c 12 -f bgs -x /N/u/mls16/Carbonate/Programs/SLiM-build/slim
    python neutral_tskit_to_msout_v2.py -d 1250 -r 2500 -s nomig_bgs_scaled.slim -p None -c 12 -f bgs -x /N/u/mls16/Carbonate/Programs/SLiM-build/slim
    ```  
    
    All slim scripts can be found in this [directory](https://github.com/meganlsmith/selectionandmigration/blob/main/scripts/slim/simple/).

    1. Training Data
    * Neutral (10000 nomig, 10000 p1_p2, 10000 p2_p1 per divergence time)
    * Background Selection (10000 nomig, 10000 p1_p2, 10000 p2_p1 per divergence time)
    * Selective Sweep in P1 (2500 nomig, 2000 p1_p2, 2500 p2_p1)
    * Selective Sweep in the ancestor (2500 nomig, 2000 p1_p2, 2500 p2_p1)
    * Adaptive Introgression (2000 p1_p2 *SIMULATE 1000 MORE DATASETS)

    2. Testing Data


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

# Calculating summary statistics (training and testing SLiM datasets)

First, you should  have a directory that contains properly formatted ms-style data for each of the training models. There should be one file per model. To combine all simulations into a single, properly formatted file, follow the example below. You can find the msmovecommand.txt file [here](https://github.com/meganlsmith/selectionandmigration/blob/main/data/msmovecommand.txt).

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
The statistics are now stored in testingSimsStats_1250. Do this for all divergence times, and for both training and testing datasets.  

# Create datasets with selection (training and testing SLiM datasets)

Create datasets with 5, 10, 15% of loci experiencing sweeps or adaptive introgression. The input folder is the output folder from calculating summary statistics. Do this for all divergence times and for training and testing datasets.
```
python createdatasets_adaptive.py -i input_folder
```

# Prepare feature fectors (training and testing SLiM datasets)

Finally, prepare the feature vectors. The input folder is the folder with the summary statistics.

Testing datasets:
```
python prepTesting_drosophila.py input_folder output_folder
```
Training datasets:
```
python prepTraining_drosophila.py input_folder output_folder
```

# Calculate summary statistics and prepare feature fector (msmove)

The following bash script illustrates how to calculate summary statistics for the simulations in th efolder trainingSims_neutral in the div_25 folder. Do this for all divergence times.

```
n1=20 # population one size
n2=20 # population two size
windowSize=10000 # window size

cd div25

mkdir -p trainingSimsStats trainingSets

## Calculate summary statistics
for inFile in `ls trainingSims_neutral/ | grep .msOut` ; do cat trainingSims_neutral/$inFile | ./FILET-master/twoPopnStats_forML $n1 $n2 | python./FILET-master/normalizeTwoPopnStats.py None $windowSize > trainingSimsStats/$inFile; done

## Step 3 Aggregate training data
python ./FILET-master/buildThreeClassTrainingSet.py trainingSimsStats/ trainingSets/threeClass.fvec

cd ../
```


# Calculate summary statistics and prepare feature vector (msmove match $/pi$)

Summary statistics are calculated when msmove_matchpi.py is run, so we need only to prepare the feature vectors.
```
python prepTraining_msmove_drosophila.py input_folder output_folder
```

# Classifiers
We constructed classifiers for each of the training datasets, using the following summary statistics and scripts from Schrider et al. (2018):
