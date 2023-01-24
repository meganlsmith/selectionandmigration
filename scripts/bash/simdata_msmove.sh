#!/bin/bash
#PBS -k o
#PBS -l nodes=1:ppn=1,walltime=100:00:00
#PBS -M mls16@iu.edu
#PBS -N simmsdata

cd $PBS_O_WORKDIR
module load python
source activate filet
mkdir -p div25 div1 div4 div16

## divergence time: 0.25
mkdir ./div25/trainingSims_neutral

### Draw parameter values
python sample_parameters_msmove.py -t 50 -p 250 -w 10000 -r 10000 -m mig12 -i -d 0.25
python sample_parameters_msmove.py -t 50 -p 250 -w 10000 -r 10000 -m mig21 -i -d 0.25
python sample_parameters_msmove.py -t 50 -p 250 -w 10000 -r 10000 -m nomig -d 0.25

## Simulate Data
/N/u/mls16/Carbonate/Programs/msmove-master/gccRelease/msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 -ev tbs 1 2 tbs < mig12_params_50_250_10000_0.25.txt > ./div25/trainingSims_neutral/mig12.msOut
/N/u/mls16/Carbonate/Programs/msmove-master/gccRelease/msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 -ev tbs 2 1 tbs < mig21_params_50_250_10000_0.25.txt > ./div25/trainingSims_neutral/mig21.msOut
/N/u/mls16/Carbonate/Programs/msmove-master/gccRelease/msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 < nomig_params_50_250_10000_0.25.txt > ./div25/trainingSims_neutral/noMig.msOut

## divergence time:1

mkdir ./div1/trainingSims_neutral

### Draw parameter values
python sample_parameters_msmove.py -t 50 -p 250 -w 10000 -r 10000 -m mig12 -i -d 1.0
python sample_parameters_msmove.py -t 50 -p 250 -w 10000 -r 10000 -m mig21 -i -d 1.0
python sample_parameters_msmove.py -t 50 -p 250 -w 10000 -r 10000 -m nomig -d 1.0

## Simulate Data
/N/u/mls16/Carbonate/Programs/msmove-master/gccRelease/msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 -ev tbs 1 2 tbs < mig12_params_50_250_10000_1.0.txt > ./div1/trainingSims_neutral/mig12.msOut
/N/u/mls16/Carbonate/Programs/msmove-master/gccRelease/msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 -ev tbs 2 1 tbs < mig21_params_50_250_10000_1.0.txt > ./div1/trainingSims_neutral/mig21.msOut
/N/u/mls16/Carbonate/Programs/msmove-master/gccRelease/msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 < nomig_params_50_250_10000_1.0.txt > ./div1/trainingSims_neutral/noMig.msOut

## divergence time: 4

mkdir ./div4/trainingSims_neutral

### Draw parameter values
python sample_parameters_msmove.py -t 50 -p 250 -w 10000 -r 10000 -m mig12 -i -d 4.0
python sample_parameters_msmove.py -t 50 -p 250 -w 10000 -r 10000 -m mig21 -i -d 4.0
python sample_parameters_msmove.py -t 50 -p 250 -w 10000 -r 10000 -m nomig -d 4.0

## Simulate Data
/N/u/mls16/Carbonate/Programs/msmove-master/gccRelease/msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 -ev tbs 1 2 tbs < mig12_params_50_250_10000_4.0.txt > ./div4/trainingSims_neutral/mig12.msOut
/N/u/mls16/Carbonate/Programs/msmove-master/gccRelease/msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 -ev tbs 2 1 tbs < mig21_params_50_250_10000_4.0.txt > ./div4/trainingSims_neutral/mig21.msOut
/N/u/mls16/Carbonate/Programs/msmove-master/gccRelease/msmove 40 10000 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 < nomig_params_50_250_10000_4.0.txt > ./div4/trainingSims_neutral/noMig.msOut

