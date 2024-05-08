#!/bin/bash
#SBATCH -A r00279
#SBATCH -J nomig_dadi_bgs_drosophila
#SBATCH -p general
#SBATCH -o nomig_dadi_bgs_drosophila_%j.txt
#SBATCH -e nomig_dadi_bgs_drosophila_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mls16@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=96:00:00
module load python

python ./python_scripts/run_dadi_20k_nomig.py --input ../SFS-redo-revision/DROSOPHILA-testing-redo-revisions-v2/dadi/nomig_bgs_drosophila_200000/ --output DROSOPHILA-testing-redo-revisions-v2/ --prefix nomig_bgs_drosophila_200000_nomigmodel

