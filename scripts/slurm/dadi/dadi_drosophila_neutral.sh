#!/bin/bash
#SBATCH -A general
#SBATCH -J dadi_neutral_drosophila
#SBATCH -p general
#SBATCH -o dadi_neutral_drosophila_%j.txt
#SBATCH -e dadi_neutral_drosophila_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mls16@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=96:00:00
module load python

python ./python_scripts/run_dadi.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_neutral_drosophila_1250/ --output DROSOPHILA-testing-redo/ --prefix nomig_neutral_drosophila_1250
python ./python_scripts/run_dadi_5k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_neutral_drosophila_5000/ --output DROSOPHILA-testing-redo/ --prefix nomig_neutral_drosophila_5000
python ./python_scripts/run_dadi_20k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/nomig_neutral_drosophila_20000/ --output DROSOPHILA-testing-redo/ --prefix nomig_neutral_drosophila_20000

python ./python_scripts/run_dadi.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p1_p2_neutral_drosophila_1250/ --output DROSOPHILA-testing-redo/ --prefix p1_p2_neutral_drosophila_1250
python ./python_scripts/run_dadi_5k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p1_p2_neutral_drosophila_5000/ --output DROSOPHILA-testing-redo/ --prefix p1_p2_neutral_drosophila_5000
python ./python_scripts/run_dadi_20k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p1_p2_neutral_drosophila_20000/ --output DROSOPHILA-testing-redo/ --prefix p1_p2_neutral_drosophila_20000

python ./python_scripts/run_dadi.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p2_p1_neutral_drosophila_1250/ --output DROSOPHILA-testing-redo/ --prefix p2_p1_neutral_drosophila_1250
python ./python_scripts/run_dadi_5k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p2_p1_neutral_drosophila_5000/ --output DROSOPHILA-testing-redo/ --prefix p2_p1_neutral_drosophila_5000
python ./python_scripts/run_dadi_20k.py --input ../SFS-redo/DROSOPHILA-testing-redo/dadi/p2_p1_neutral_drosophila_20000/ --output DROSOPHILA-testing-redo/ --prefix p2_p1_neutral_drosophila_20000
