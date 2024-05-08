#!/bin/bash
#SBATCH -A r00279
#SBATCH -J sumstats_20000
#SBATCH -p general
#SBATCH -o sumstats_20000_%j.txt
#SBATCH -e sumstats_20000_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=10:00:00

module load python/3.9.8

python python_scripts/calc_sumstats.py ../DROSOPHILA-testing-redo-revisions-v2/nomig_neutral_drosophila_20000/ nomig_neutral_drosophila_20000_sumstats.csv
python python_scripts/calc_sumstats.py ../DROSOPHILA-testing-redo-revisions-v2/nomig_bgs_drosophila_20000/ nomig_bgs_drosophila_20000_sumstats.csv
python python_scripts/calc_sumstats.py ../DROSOPHILA-testing-redo-revisions-v2/nomig_balancing_drosophila_20000/ nomig_balancing_drosophila_20000_sumstats.csv
python python_scripts/calc_sumstats.py ../DROSOPHILA-testing-redo-revisions-v2/nomig_linkedp1_drosophila_20000/ nomig_linkedp1_drosophila_20000_sumstats.csv
python python_scripts/calc_sumstats.py ../DROSOPHILA-testing-redo-revisions-v2/nomig_linkedancestor_drosophila_20000/ nomig_linkedancestor_drosophila_20000_sumstats.csv

python python_scripts/calc_sumstats.py ../DROSOPHILA-testing-redo-revisions-v2/p1_p2_neutral_drosophila_20000/ p1_p2_neutral_drosophila_20000_sumstats.csv
python python_scripts/calc_sumstats.py ../DROSOPHILA-testing-redo-revisions-v2/p1_p2_bgs_drosophila_20000/ p1_p2_bgs_drosophila_20000_sumstats.csv
python python_scripts/calc_sumstats.py ../DROSOPHILA-testing-redo-revisions-v2/p1_p2_balancing_drosophila_20000/ p1_p2_balancing_drosophila_20000_sumstats.csv
python python_scripts/calc_sumstats.py ../DROSOPHILA-testing-redo-revisions-v2/p1_p2_linkedp1_drosophila_20000/ p1_p2_linkedp1_drosophila_20000_sumstats.csv
python python_scripts/calc_sumstats.py ../DROSOPHILA-testing-redo-revisions-v2/p1_p2_linkedancestor_drosophila_20000/ p1_p2_linkedancestor_drosophila_20000_sumstats.csv
python python_scripts/calc_sumstats.py ../DROSOPHILA-testing-redo-revisions-v2/p1_p2_adaptiveint_drosophila_20000/ p1_p2_adaptiveint_drosophila_20000_sumstats.csv

python python_scripts/calc_sumstats.py ../DROSOPHILA-testing-redo-revisions-v2/nomig_bgsh5_drosophila_20000/ nomig_bgsh5_drosophila_20000_sumstats.csv

