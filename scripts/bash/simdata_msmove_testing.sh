#!/bin/bash
#PBS -k o
#PBS -l nodes=1:ppn=1,walltime=100:00:00
#PBS -M mls16@iu.edu
#PBS -N simmsdata
#PBS -m e

cd $PBS_O_WORKDIR
module load python
source activate filet
mkdir -p div25 div1 div4 div16

# divergence time 0.25
mkdir ./div25/testingSims_neutral

## Draw parameter values
python sample_parameters_msmove.py -t 50 -p 250 -w 10000 -r 10000 -m testing_mig12 -i -d 0.25
python sample_parameters_msmove.py -t 50 -p 250 -w 10000 -r 10000 -m testing_mig21 -i -d 0.25
python sample_parameters_msmove.py -t 50 -p 250 -w 10000 -r 10000 -m testing_nomig -d 0.25

# Simulate Data
/N/u/mls16/Carbonate/Programs/msmove-master/gccRelease/msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 -ev tbs 1 2 tbs < testing_mig12_params_50_250_10000_0.25.txt > ./div25/testingSims_neutral/mig12.msOut
/N/u/mls16/Carbonate/Programs/msmove-master/gccRelease/msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 -ev tbs 2 1 tbs < testing_mig21_params_50_250_10000_0.25.txt > ./div25/testingSims_neutral/mig21.msOut
/N/u/mls16/Carbonate/Programs/msmove-master/gccRelease/msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 < testing_nomig_params_50_250_10000_0.25.txt > ./div25/testingSims_neutral/noMig.msOut


# divergence time 1

mkdir ./div1/testingSims_neutral

## Draw parameter values
python sample_parameters_msmove.py -t 50 -p 250 -w 10000 -r 10000 -m testing_mig12 -i -d 1.0
python sample_parameters_msmove.py -t 50 -p 250 -w 10000 -r 10000 -m testing_mig21 -i -d 1.0
python sample_parameters_msmove.py -t 50 -p 250 -w 10000 -r 10000 -m testing_nomig -d 1.0

# Simulate Data
/N/u/mls16/Carbonate/Programs/msmove-master/gccRelease/msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 -ev tbs 1 2 tbs < testing_mig12_params_50_250_10000_1.0.txt > ./div1/testingSims_neutral/mig12.msOut
/N/u/mls16/Carbonate/Programs/msmove-master/gccRelease/msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 -ev tbs 2 1 tbs < testing_mig21_params_50_250_10000_1.0.txt > ./div1/testingSims_neutral/mig21.msOut
/N/u/mls16/Carbonate/Programs/msmove-master/gccRelease/msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 < testing_nomig_params_50_250_10000_1.0.txt > ./div1/testingSims_neutral/noMig.msOut

# divergence time 4

mkdir ./div4/testingSims_neutral

## Draw parameter values
python sample_parameters_msmove.py -t 50 -p 250 -w 10000 -r 10000 -m testing_mig12 -i -d 4.0
python sample_parameters_msmove.py -t 50 -p 250 -w 10000 -r 10000 -m testing_mig21 -i -d 4.0
python sample_parameters_msmove.py -t 50 -p 250 -w 10000 -r 10000 -m testing_nomig -d 4.0

# Simulate Data
/N/u/mls16/Carbonate/Programs/msmove-master/gccRelease/msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 -ev tbs 1 2 tbs < testing_mig12_params_50_250_10000_4.0.txt > ./div4/testingSims_neutral/mig12.msOut
/N/u/mls16/Carbonate/Programs/msmove-master/gccRelease/msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 -ev tbs 2 1 tbs < testing_mig21_params_50_250_10000_4.0.txt > ./div4/testingSims_neutral/mig21.msOut
/N/u/mls16/Carbonate/Programs/msmove-master/gccRelease/msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 < testing_nomig_params_50_250_10000_4.0.txt > ./div4/testingSims_neutral/noMig.msOut
