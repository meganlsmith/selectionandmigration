#!/bin/bash
#SBATCH -A general
#SBATCH -J dadi_linkedancestor_drosophila
#SBATCH -p general
#SBATCH -o dadi_linkedancestor_drosophila_%j.txt
#SBATCH -e dadi_linkedancestor_drosophila_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mls16@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=96:00:00
module load python

#python ./python_scripts/run_dadi.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_linkedancestor_drosophila_1250_5percent/ --output DROSOPHILA-testing-redo/ --prefix nomig_linkedancestor_drosophila_1250_5percent
#python ./python_scripts/run_dadi.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_linkedancestor_drosophila_1250_10percent/ --output DROSOPHILA-testing-redo/ --prefix nomig_linkedancestor_drosophila_1250_10percent
#python ./python_scripts/run_dadi.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_linkedancestor_drosophila_1250_15percent/ --output DROSOPHILA-testing-redo/ --prefix nomig_linkedancestor_drosophila_1250_15percent

#python ./python_scripts/run_dadi_5k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_linkedancestor_drosophila_5000_5percent/ --output DROSOPHILA-testing-redo/ --prefix nomig_linkedancestor_drosophila_5000_5percent
#python ./python_scripts/run_dadi_5k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_linkedancestor_drosophila_5000_10percent/ --output DROSOPHILA-testing-redo/ --prefix nomig_linkedancestor_drosophila_5000_10percent
#python ./python_scripts/run_dadi_5k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_linkedancestor_drosophila_5000_15percent/ --output DROSOPHILA-testing-redo/ --prefix nomig_linkedancestor_drosophila_5000_15percent

#python ./python_scripts/run_dadi_20k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_linkedancestor_drosophila_20000_5percent/ --output DROSOPHILA-testing-redo/ --prefix nomig_linkedancestor_drosophila_20000_5percent
#python ./python_scripts/run_dadi_20k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_linkedancestor_drosophila_20000_10percent/ --output DROSOPHILA-testing-redo/ --prefix nomig_linkedancestor_drosophila_20000_10percent
python ./python_scripts/run_dadi_20k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_linkedancestor_drosophila_20000_15percent/ --output DROSOPHILA-testing-redo/ --prefix nomig_linkedancestor_drosophila_20000_15percent

python ./python_scripts/run_dadi.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p1_p2_linkedancestor_drosophila_1250_5percent/ --output DROSOPHILA-testing-redo/ --prefix p1_p2_linkedancestor_drosophila_1250_5percent
python ./python_scripts/run_dadi.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p1_p2_linkedancestor_drosophila_1250_10percent/ --output DROSOPHILA-testing-redo/ --prefix p1_p2_linkedancestor_drosophila_1250_10percent
python ./python_scripts/run_dadi.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p1_p2_linkedancestor_drosophila_1250_15percent/ --output DROSOPHILA-testing-redo/ --prefix p1_p2_linkedancestor_drosophila_1250_15percent

python ./python_scripts/run_dadi_5k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p1_p2_linkedancestor_drosophila_5000_5percent/ --output DROSOPHILA-testing-redo/ --prefix p1_p2_linkedancestor_drosophila_5000_5percent
python ./python_scripts/run_dadi_5k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p1_p2_linkedancestor_drosophila_5000_10percent/ --output DROSOPHILA-testing-redo/ --prefix p1_p2_linkedancestor_drosophila_5000_10percent
python ./python_scripts/run_dadi_5k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p1_p2_linkedancestor_drosophila_5000_15percent/ --output DROSOPHILA-testing-redo/ --prefix p1_p2_linkedancestor_drosophila_5000_15percent

python ./python_scripts/run_dadi_20k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p1_p2_linkedancestor_drosophila_20000_5percent/ --output DROSOPHILA-testing-redo/ --prefix p1_p2_linkedancestor_drosophila_20000_5percent
python ./python_scripts/run_dadi_20k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p1_p2_linkedancestor_drosophila_20000_10percent/ --output DROSOPHILA-testing-redo/ --prefix p1_p2_linkedancestor_drosophila_20000_10percent
python ./python_scripts/run_dadi_20k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p1_p2_linkedancestor_drosophila_20000_15percent/ --output DROSOPHILA-testing-redo/ --prefix p1_p2_linkedancestor_drosophila_20000_15percent

python ./python_scripts/run_dadi.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p2_p1_linkedancestor_drosophila_1250_5percent/ --output DROSOPHILA-testing-redo/ --prefix p2_p1_linkedancestor_drosophila_1250_5percent
python ./python_scripts/run_dadi.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p2_p1_linkedancestor_drosophila_1250_10percent/ --output DROSOPHILA-testing-redo/ --prefix p2_p1_linkedancestor_drosophila_1250_10percent
python ./python_scripts/run_dadi.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p2_p1_linkedancestor_drosophila_1250_15percent/ --output DROSOPHILA-testing-redo/ --prefix p2_p1_linkedancestor_drosophila_1250_15percent

python ./python_scripts/run_dadi_5k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p2_p1_linkedancestor_drosophila_5000_5percent/ --output DROSOPHILA-testing-redo/ --prefix p2_p1_linkedancestor_drosophila_5000_5percent
python ./python_scripts/run_dadi_5k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p2_p1_linkedancestor_drosophila_5000_10percent/ --output DROSOPHILA-testing-redo/ --prefix p2_p1_linkedancestor_drosophila_5000_10percent
python ./python_scripts/run_dadi_5k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p2_p1_linkedancestor_drosophila_5000_15percent/ --output DROSOPHILA-testing-redo/ --prefix p2_p1_linkedancestor_drosophila_5000_15percent

python ./python_scripts/run_dadi_20k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p2_p1_linkedancestor_drosophila_20000_5percent/ --output DROSOPHILA-testing-redo/ --prefix p2_p1_linkedancestor_drosophila_20000_5percent
python ./python_scripts/run_dadi_20k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p2_p1_linkedancestor_drosophila_20000_10percent/ --output DROSOPHILA-testing-redo/ --prefix p2_p1_linkedancestor_drosophila_20000_10percent
python ./python_scripts/run_dadi_20k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p2_p1_linkedancestor_drosophila_20000_15percent/ --output DROSOPHILA-testing-redo/ --prefix p2_p1_linkedancestor_drosophila_20000_15percent
