#!/bin/bash
#SBATCH -A r00279 
#SBATCH -J sfs_neutral_scaled
#SBATCH -p general
#SBATCH -o sfs_neutral_scaled_%j.txt
#SBATCH -e sfs_neutral_scaled_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mls16@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=18:00:00

module load python
python ./python_scripts/makesfs.py --input ../SLiM-testing-redo-revisions/nomig_neutral_scaled_1250/ --output1 SLiM-testing-redo-revisions/dadi/nomig_neutral_scaled_1250/ --output2 SLiM-testing-redo-revisions/fsc/nomig_neutral_scaled_1250/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
python ./python_scripts/makesfs.py --input ../SLiM-testing-redo-revisions/nomig_neutral_scaled_5000/ --output1 SLiM-testing-redo-revisions/dadi/nomig_neutral_scaled_5000/ --output2 SLiM-testing-redo-revisions/fsc/nomig_neutral_scaled_5000/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
python ./python_scripts/makesfs.py --input ../SLiM-testing-redo-revisions/nomig_neutral_scaled_20000/ --output1 SLiM-testing-redo-revisions/dadi/nomig_neutral_scaled_20000/ --output2 SLiM-testing-redo-revisions/fsc/nomig_neutral_scaled_20000/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000

python ./python_scripts/makesfs.py --input ../SLiM-testing-redo-revisions/p1_p2_neutral_scaled_1250/ --output1 SLiM-testing-redo-revisions/dadi/p1_p2_neutral_scaled_1250/ --output2 SLiM-testing-redo-revisions/fsc/p1_p2_neutral_scaled_1250/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
python ./python_scripts/makesfs.py --input ../SLiM-testing-redo-revisions/p1_p2_neutral_scaled_5000/ --output1 SLiM-testing-redo-revisions/dadi/p1_p2_neutral_scaled_5000/ --output2 SLiM-testing-redo-revisions/fsc/p1_p2_neutral_scaled_5000/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
python ./python_scripts/makesfs.py --input ../SLiM-testing-redo-revisions/p1_p2_neutral_scaled_20000/ --output1 SLiM-testing-redo-revisions/dadi/p1_p2_neutral_scaled_20000/ --output2 SLiM-testing-redo-revisions/fsc/p1_p2_neutral_scaled_20000/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
