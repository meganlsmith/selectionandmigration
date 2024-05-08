#!/bin/bash
#SBATCH -A r00279
#SBATCH -J nomig_dadi_neutral_drosophila
#SBATCH -p general
#SBATCH -o nomig_dadi_neutral_drosophila_%j.txt
#SBATCH -e nomig_dadi_neutral_drosophila_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mls16@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=96:00:00
module load python

python ./python_scripts/run_dadi_nomig.py --input ../SFS-redo-revision/DROSOPHILA-testing-redo-revisions-v2/dadi/nomig_neutral_drosophila_1250/ --output DROSOPHILA-testing-redo-revisions-v2/ --prefix nomig_neutral_drosophila_1250_nomigmodel
python ./python_scripts/run_dadi_5k_nomig.py --input ../SFS-redo-revision/DROSOPHILA-testing-redo-revisions-v2/dadi/nomig_neutral_drosophila_5000/ --output DROSOPHILA-testing-redo-revisions-v2/ --prefix nomig_neutral_drosophila_5000_nomigmodel
python ./python_scripts/run_dadi_20k_nomig.py --input ../SFS-redo-revision/DROSOPHILA-testing-redo-revisions-v2/dadi/nomig_neutral_drosophila_20000/ --output DROSOPHILA-testing-redo-revisions-v2/ --prefix nomig_neutral_drosophila_20000_nomigmodel

