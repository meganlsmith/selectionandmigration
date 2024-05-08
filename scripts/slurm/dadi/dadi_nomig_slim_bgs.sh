#!/bin/bash
#SBATCH -A r00279
#SBATCH -J nomig_dadi_bgs_scaled
#SBATCH -p general
#SBATCH -o nomig_dadi_bgs_scaled_%j.txt
#SBATCH -e nomig_dadi_bgs_scaled_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mls16@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=96:00:00
module load python

python ./python_scripts/run_dadi_nomig.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/nomig_bgs_scaled_1250/ --output SLiM-testing-redo-revisions/ --prefix nomig_bgs_scaled_1250_nomigmodel
python ./python_scripts/run_dadi_5k_nomig.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/nomig_bgs_scaled_5000/ --output SLiM-testing-redo-revisions/ --prefix nomig_bgs_scaled_5000_nomigmodel
python ./python_scripts/run_dadi_20k_nomig.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/nomig_bgs_scaled_20000/ --output SLiM-testing-redo-revisions/ --prefix nomig_bgs_scaled_20000_nomigmodel

