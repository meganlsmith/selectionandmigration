#!/bin/bash
#SBATCH -A r00279
#SBATCH -J dadi_linkedp1_scaled
#SBATCH -p general
#SBATCH -o dadi_linkedp1_scaled_%j.txt
#SBATCH -e dadi_linkedp1_scaled_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mls16@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=96:00:00
module load python

python ./python_scripts/run_dadi.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/nomig_linkedp1_scaled_1250_5percent/ --output SLiM-testing-redo-revisions/ --prefix nomig_linkedp1_scaled_1250_5percent
python ./python_scripts/run_dadi.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/nomig_linkedp1_scaled_1250_10percent/ --output SLiM-testing-redo-revisions/ --prefix nomig_linkedp1_scaled_1250_10percent
python ./python_scripts/run_dadi.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/nomig_linkedp1_scaled_1250_15percent/ --output SLiM-testing-redo-revisions/ --prefix nomig_linkedp1_scaled_1250_15percent

python ./python_scripts/run_dadi_5k.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/nomig_linkedp1_scaled_5000_5percent/ --output SLiM-testing-redo-revisions/ --prefix nomig_linkedp1_scaled_5000_5percent
python ./python_scripts/run_dadi_5k.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/nomig_linkedp1_scaled_5000_10percent/ --output SLiM-testing-redo-revisions/ --prefix nomig_linkedp1_scaled_5000_10percent
python ./python_scripts/run_dadi_5k.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/nomig_linkedp1_scaled_5000_15percent/ --output SLiM-testing-redo-revisions/ --prefix nomig_linkedp1_scaled_5000_15percent

python ./python_scripts/run_dadi_20k.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/nomig_linkedp1_scaled_20000_5percent/ --output SLiM-testing-redo-revisions/ --prefix nomig_linkedp1_scaled_20000_5percent
python ./python_scripts/run_dadi_20k.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/nomig_linkedp1_scaled_20000_10percent/ --output SLiM-testing-redo-revisions/ --prefix nomig_linkedp1_scaled_20000_10percent
python ./python_scripts/run_dadi_20k.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/nomig_linkedp1_scaled_20000_15percent/ --output SLiM-testing-redo-revisions/ --prefix nomig_linkedp1_scaled_20000_15percent

python ./python_scripts/run_dadi.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/p1_p2_linkedp1_scaled_1250_5percent/ --output SLiM-testing-redo-revisions/ --prefix p1_p2_linkedp1_scaled_1250_5percent
python ./python_scripts/run_dadi.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/p1_p2_linkedp1_scaled_1250_10percent/ --output SLiM-testing-redo-revisions/ --prefix p1_p2_linkedp1_scaled_1250_10percent
python ./python_scripts/run_dadi.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/p1_p2_linkedp1_scaled_1250_15percent/ --output SLiM-testing-redo-revisions/ --prefix p1_p2_linkedp1_scaled_1250_15percent

python ./python_scripts/run_dadi_5k.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/p1_p2_linkedp1_scaled_5000_5percent/ --output SLiM-testing-redo-revisions/ --prefix p1_p2_linkedp1_scaled_5000_5percent
python ./python_scripts/run_dadi_5k.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/p1_p2_linkedp1_scaled_5000_10percent/ --output SLiM-testing-redo-revisions/ --prefix p1_p2_linkedp1_scaled_5000_10percent
python ./python_scripts/run_dadi_5k.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/p1_p2_linkedp1_scaled_5000_15percent/ --output SLiM-testing-redo-revisions/ --prefix p1_p2_linkedp1_scaled_5000_15percent

python ./python_scripts/run_dadi_20k.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/p1_p2_linkedp1_scaled_20000_5percent/ --output SLiM-testing-redo-revisions/ --prefix p1_p2_linkedp1_scaled_20000_5percent
python ./python_scripts/run_dadi_20k.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/p1_p2_linkedp1_scaled_20000_10percent/ --output SLiM-testing-redo-revisions/ --prefix p1_p2_linkedp1_scaled_20000_10percent
python ./python_scripts/run_dadi_20k.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/p1_p2_linkedp1_scaled_20000_15percent/ --output SLiM-testing-redo-revisions/ --prefix p1_p2_linkedp1_scaled_20000_15percent

python ./python_scripts/run_dadi.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/p2_p1_linkedp1_scaled_1250_5percent/ --output SLiM-testing-redo-revisions/ --prefix p2_p1_linkedp1_scaled_1250_5percent
python ./python_scripts/run_dadi.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/p2_p1_linkedp1_scaled_1250_10percent/ --output SLiM-testing-redo-revisions/ --prefix p2_p1_linkedp1_scaled_1250_10percent
python ./python_scripts/run_dadi.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/p2_p1_linkedp1_scaled_1250_15percent/ --output SLiM-testing-redo-revisions/ --prefix p2_p1_linkedp1_scaled_1250_15percent

python ./python_scripts/run_dadi_5k.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/p2_p1_linkedp1_scaled_5000_5percent/ --output SLiM-testing-redo-revisions/ --prefix p2_p1_linkedp1_scaled_5000_5percent
python ./python_scripts/run_dadi_5k.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/p2_p1_linkedp1_scaled_5000_10percent/ --output SLiM-testing-redo-revisions/ --prefix p2_p1_linkedp1_scaled_5000_10percent
python ./python_scripts/run_dadi_5k.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/p2_p1_linkedp1_scaled_5000_15percent/ --output SLiM-testing-redo-revisions/ --prefix p2_p1_linkedp1_scaled_5000_15percent

python ./python_scripts/run_dadi_20k.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/p2_p1_linkedp1_scaled_20000_5percent/ --output SLiM-testing-redo-revisions/ --prefix p2_p1_linkedp1_scaled_20000_5percent
python ./python_scripts/run_dadi_20k.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/p2_p1_linkedp1_scaled_20000_10percent/ --output SLiM-testing-redo-revisions/ --prefix p2_p1_linkedp1_scaled_20000_10percent
python ./python_scripts/run_dadi_20k.py --input ../SFS-redo-revision/SLiM-testing-redo-revisions/dadi/p2_p1_linkedp1_scaled_20000_15percent/ --output SLiM-testing-redo-revisions/ --prefix p2_p1_linkedp1_scaled_20000_15percent

