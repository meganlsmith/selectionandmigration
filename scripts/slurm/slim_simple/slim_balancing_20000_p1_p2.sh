#!/bin/bash
#SBATCH -A r00279
#SBATCH -J balancing_20000_p1_p2
#SBATCH -p general
#SBATCH -o balancing_20000_p1_p2_%j.txt
#SBATCH -e balancing_20000_p1_p2_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --time=96:00:00

module load python/3.9.8

python python_scripts/sample_parameters_slim.py -s p1_p2_balancing_scaled.slim -r 10000 -d 2000000

python ./python_scripts/neutral_tskit_to_msout_v4.py -d 2000000 -r 10000 -s ./slim_scripts/p1_p2_balancing_scaled.slim --prefix p1_p2_balancing_scaled -p ../params/p1_p2_balancing_scaled_params_2000000.txt -c 24 -f balancing -x /N/project/Prophysaongenomics/FILET_Organized_24January2023/programs/build/slim --scale 100

