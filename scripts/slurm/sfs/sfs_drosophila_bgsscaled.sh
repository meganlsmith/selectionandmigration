#!/bin/bash
#SBATCH -A r00279 
#SBATCH -J sfs_bgsscaled_drosophila
#SBATCH -p general
#SBATCH -o sfs_bgsscaled_drosophila_%j.txt
#SBATCH -e sfs_bgsscaled_drosophila_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mls16@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=5:00:00

module load python
python ./python_scripts/makesfs.py --input ../DROSOPHILA-testing-redo-revisions-v2/nomig_bgs_drosophila_200000/ --output1 DROSOPHILA-testing-redo-revisions-v2/dadi/nomig_bgs_drosophila_200000/ --output2 DROSOPHILA-testing-redo-revisions-v2/fsc/nomig_bgs_drosophila_200000/ --reps 100 --npop0 20 --npop1 20 --max 1000 --length 10000
