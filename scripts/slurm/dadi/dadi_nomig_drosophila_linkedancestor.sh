#!/bin/bash
#SBATCH -A general
#SBATCH -J nomig_dadi_linkedancestor_drosophila
#SBATCH -p general
#SBATCH -o nomig_dadi_linkedancestor_drosophila_%j.txt
#SBATCH -e nomig_dadi_linkedancestor_drosophila_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mls16@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=96:00:00
module load python

#python ./python_scripts/run_dadi_nomig.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_linkedancestor_drosophila_1250_5percent/ --output DROSOPHILA-testing-redo/ --prefix nomig_linkedancestor_drosophila_1250_5percent_nomigmodel
#python ./python_scripts/run_dadi_nomig.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_linkedancestor_drosophila_1250_10percent/ --output DROSOPHILA-testing-redo/ --prefix nomig_linkedancestor_drosophila_1250_10percent_nomigmodel
#python ./python_scripts/run_dadi_nomig.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_linkedancestor_drosophila_1250_15percent/ --output DROSOPHILA-testing-redo/ --prefix nomig_linkedancestor_drosophila_1250_15percent_nomigmodel

#python ./python_scripts/run_dadi_5k_nomig.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_linkedancestor_drosophila_5000_5percent/ --output DROSOPHILA-testing-redo/ --prefix nomig_linkedancestor_drosophila_5000_5percent_nomigmodel
#python ./python_scripts/run_dadi_5k_nomig.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_linkedancestor_drosophila_5000_10percent/ --output DROSOPHILA-testing-redo/ --prefix nomig_linkedancestor_drosophila_5000_10percent_nomigmodel
#python ./python_scripts/run_dadi_5k_nomig.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_linkedancestor_drosophila_5000_15percent/ --output DROSOPHILA-testing-redo/ --prefix nomig_linkedancestor_drosophila_5000_15percent_nomigmodel

#python ./python_scripts/run_dadi_20k_nomig.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_linkedancestor_drosophila_20000_5percent/ --output DROSOPHILA-testing-redo/ --prefix nomig_linkedancestor_drosophila_20000_5percent_nomigmodel
#python ./python_scripts/run_dadi_20k_nomig.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_linkedancestor_drosophila_20000_10percent/ --output DROSOPHILA-testing-redo/ --prefix nomig_linkedancestor_drosophila_20000_10percent_nomigmodel
python ./python_scripts/run_dadi_20k_nomig.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_linkedancestor_drosophila_20000_15percent/ --output DROSOPHILA-testing-redo/ --prefix nomig_linkedancestor_drosophila_20000_15percent_nomigmodel

