#!/bin/bash
#SBATCH -A general
#SBATCH -J sfs_bgs_scaled
#SBATCH -p general
#SBATCH -o sfs_bgs_scaled_%j.txt
#SBATCH -e sfs_bgs_scaled_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mls16@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=18:00:00

module load python
python ./python_scripts/makesfs.py --input ../SLiM-testing-redo/nomig_bgs_scaled_1250/ --output1 SLiM-testing-redo/dadi/nomig_bgs_scaled_1250/ --output2 SLiM-testing-redo/fsc/nomig_bgs_scaled_1250/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
python ./python_scripts/makesfs.py --input ../SLiM-testing-redo/nomig_bgs_scaled_5000/ --output1 SLiM-testing-redo/dadi/nomig_bgs_scaled_5000/ --output2 SLiM-testing-redo/fsc/nomig_bgs_scaled_5000/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
python ./python_scripts/makesfs.py --input ../SLiM-testing-redo/nomig_bgs_scaled_20000/ --output1 SLiM-testing-redo/dadi/nomig_bgs_scaled_20000/ --output2 SLiM-testing-redo/fsc/nomig_bgs_scaled_20000/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000

python ./python_scripts/makesfs.py --input ../SLiM-testing-redo/p1_p2_bgs_scaled_1250/ --output1 SLiM-testing-redo/dadi/p1_p2_bgs_scaled_1250/ --output2 SLiM-testing-redo/fsc/p1_p2_bgs_scaled_1250/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
python ./python_scripts/makesfs.py --input ../SLiM-testing-redo/p1_p2_bgs_scaled_5000/ --output1 SLiM-testing-redo/dadi/p1_p2_bgs_scaled_5000/ --output2 SLiM-testing-redo/fsc/p1_p2_bgs_scaled_5000/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
python ./python_scripts/makesfs.py --input ../SLiM-testing-redo/p1_p2_bgs_scaled_20000/ --output1 SLiM-testing-redo/dadi/p1_p2_bgs_scaled_20000/ --output2 SLiM-testing-redo/fsc/p1_p2_bgs_scaled_20000/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000

python ./python_scripts/makesfs.py --input ../SLiM-testing-redo/p2_p1_bgs_scaled_1250/ --output1 SLiM-testing-redo/dadi/p2_p1_bgs_scaled_1250/ --output2 SLiM-testing-redo/fsc/p2_p1_bgs_scaled_1250/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
python ./python_scripts/makesfs.py --input ../SLiM-testing-redo/p2_p1_bgs_scaled_5000/ --output1 SLiM-testing-redo/dadi/p2_p1_bgs_scaled_5000/ --output2 SLiM-testing-redo/fsc/p2_p1_bgs_scaled_5000/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
python ./python_scripts/makesfs.py --input ../SLiM-testing-redo/p2_p1_bgs_scaled_20000/ --output1 SLiM-testing-redo/dadi/p2_p1_bgs_scaled_20000/ --output2 SLiM-testing-redo/fsc/p2_p1_bgs_scaled_20000/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
