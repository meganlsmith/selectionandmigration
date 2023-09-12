#!/bin/bash
#SBATCH -A general
#SBATCH -J bgs_5000_p2_p1
#SBATCH -p general
#SBATCH -o bgs_5000_p2_p1_%j.txt
#SBATCH -e bgs_5000_p2_p1_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --time=96:00:00

module load python

python python_scripts/sample_parameters_slim.py -s p2_p1_bgs_scaled.slim -r 10000 -d 5000
python ./python_scripts/neutral_tskit_to_msout_v3.py -d 5000 -r 10000 -s ./slim_scripts/p2_p1_bgs_scaled.slim --prefix p2_p1_bgs_scaled -p ../params/p2_p1_bgs_scaled_params_5000.txt -c 24 -f bgs -x /N/project/Prophysaongenomics/FILET_Organized_24January2023/programs/build/slim
