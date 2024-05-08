#!/bin/bash
#SBATCH -A r00279
#SBATCH -J dadi_bgs_drosophila
#SBATCH -p general
#SBATCH -o dadi_bgs_drosophila_%j.txt
#SBATCH -e dadi_bgs_drosophila_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mls16@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=96:00:00
module load python

python ./python_scripts/run_dadi.py --input ../SFS-redo-revision/DROSOPHILA-testing-redo-revisions-v2/dadi/nomig_bgs_drosophila_1250/ --output DROSOPHILA-testing-redo-revisions-v2/ --prefix nomig_bgs_drosophila_1250
python ./python_scripts/run_dadi_5k.py --input ../SFS-redo-revision/DROSOPHILA-testing-redo-revisions-v2/dadi/nomig_bgs_drosophila_5000/ --output DROSOPHILA-testing-redo-revisions-v2/ --prefix nomig_bgs_drosophila_5000
python ./python_scripts/run_dadi_20k.py --input ../SFS-redo-revision/DROSOPHILA-testing-redo-revisions-v2/dadi/nomig_bgs_drosophila_20000/ --output DROSOPHILA-testing-redo-revisions-v2/ --prefix nomig_bgs_drosophila_20000

python ./python_scripts/run_dadi.py --input ../SFS-redo-revision/DROSOPHILA-testing-redo-revisions-v2/dadi/p1_p2_bgs_drosophila_1250/ --output DROSOPHILA-testing-redo-revisions-v2/ --prefix p1_p2_bgs_drosophila_1250
python ./python_scripts/run_dadi_5k.py --input ../SFS-redo-revision/DROSOPHILA-testing-redo-revisions-v2/dadi/p1_p2_bgs_drosophila_5000/ --output DROSOPHILA-testing-redo-revisions-v2/ --prefix p1_p2_bgs_drosophila_5000
python ./python_scripts/run_dadi_20k.py --input ../SFS-redo-revision/DROSOPHILA-testing-redo-revisions-v2/dadi/p1_p2_bgs_drosophila_20000/ --output DROSOPHILA-testing-redo-revisions-v2/ --prefix p1_p2_bgs_drosophila_20000

python ./python_scripts/run_dadi.py --input ../SFS-redo-revision/DROSOPHILA-testing-redo-revisions-v2/dadi/p2_p1_bgs_drosophila_1250/ --output DROSOPHILA-testing-redo-revisions-v2/ --prefix p2_p1_bgs_drosophila_1250
python ./python_scripts/run_dadi_5k.py --input ../SFS-redo-revision/DROSOPHILA-testing-redo-revisions-v2/dadi/p2_p1_bgs_drosophila_5000/ --output DROSOPHILA-testing-redo-revisions-v2/ --prefix p2_p1_bgs_drosophila_5000
python ./python_scripts/run_dadi_20k.py --input ../SFS-redo-revision/DROSOPHILA-testing-redo-revisions-v2/dadi/p2_p1_bgs_drosophila_20000/ --output DROSOPHILA-testing-redo-revisions-v2/ --prefix p2_p1_bgs_drosophila_20000
