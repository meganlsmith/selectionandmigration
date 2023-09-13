#!/bin/bash
#SBATCH -A general
#SBATCH -J sfs_bgs_drosophila
#SBATCH -p general
#SBATCH -o sfs_bgs_drosophila_%j.txt
#SBATCH -e sfs_bgs_drosophila_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mls16@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=96:00:00
#SBATCH --mem=250Gb

module load python

python ./python_scripts/makesfs.py --input ../DROSOPHILA-testing-redo/nomig_bgs_drosophila_1250/ --output1 DROSOPHILA-testing-redo/dadi/nomig_bgs_drosophila_1250/ --output2 DROSOPHILA-testing-redo/fsc/nomig_bgs_drosophila_1250/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
python ./python_scripts/makesfs.py --input ../DROSOPHILA-testing-redo/nomig_bgs_drosophila_5000/ --output1 DROSOPHILA-testing-redo/dadi/nomig_bgs_drosophila_5000/ --output2 DROSOPHILA-testing-redo/fsc/nomig_bgs_drosophila_5000/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
python ./python_scripts/makesfs.py --input ../DROSOPHILA-testing-redo/nomig_bgs_drosophila_20000/ --output1 DROSOPHILA-testing-redo/dadi/nomig_bgs_drosophila_20000/ --output2 DROSOPHILA-testing-redo/fsc/nomig_bgs_drosophila_20000/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000

python ./python_scripts/makesfs.py --input ../DROSOPHILA-testing-redo/p1_p2_bgs_drosophila_1250/ --output1 DROSOPHILA-testing-redo/dadi/p1_p2_bgs_drosophila_1250/ --output2 DROSOPHILA-testing-redo/fsc/p1_p2_bgs_drosophila_1250/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
python ./python_scripts/makesfs.py --input ../DROSOPHILA-testing-redo/p1_p2_bgs_drosophila_5000/ --output1 DROSOPHILA-testing-redo/dadi/p1_p2_bgs_drosophila_5000/ --output2 DROSOPHILA-testing-redo/fsc/p1_p2_bgs_drosophila_5000/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
python ./python_scripts/makesfs.py --input ../DROSOPHILA-testing-redo/p1_p2_bgs_drosophila_20000/ --output1 DROSOPHILA-testing-redo/dadi/p1_p2_bgs_drosophila_20000/ --output2 DROSOPHILA-testing-redo/fsc/p1_p2_bgs_drosophila_20000/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000

python ./python_scripts/makesfs.py --input ../DROSOPHILA-testing-redo/p2_p1_bgs_drosophila_1250/ --output1 DROSOPHILA-testing-redo/dadi/p2_p1_bgs_drosophila_1250/ --output2 DROSOPHILA-testing-redo/fsc/p2_p1_bgs_drosophila_1250/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
python ./python_scripts/makesfs.py --input ../DROSOPHILA-testing-redo/p2_p1_bgs_drosophila_5000/ --output1 DROSOPHILA-testing-redo/dadi/p2_p1_bgs_drosophila_5000/ --output2 DROSOPHILA-testing-redo/fsc/p2_p1_bgs_drosophila_5000/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
python ./python_scripts/makesfs.py --input ../DROSOPHILA-testing-redo/p2_p1_bgs_drosophila_20000/ --output1 DROSOPHILA-testing-redo/dadi/p2_p1_bgs_drosophila_20000/ --output2 DROSOPHILA-testing-redo/fsc/p2_p1_bgs_drosophila_20000/ --reps 100 --npop0 20 --npop1 20 --max 10000 --length 10000
