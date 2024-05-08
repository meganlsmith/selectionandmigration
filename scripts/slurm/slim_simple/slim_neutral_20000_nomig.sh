#!/bin/bash
#SBATCH -A r00279
#SBATCH -J neutral_20000_nomig
#SBATCH -p general
#SBATCH -o neutral_20000_nomig_%j.txt
#SBATCH -e neutral_20000_nomig_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --time=96:00:00

module load python/3.9.8

python ./python_scripts/neutral_tskit_to_msout_v4.py -d 2000000 -r 10000 -s ./slim_scripts/nomig_neutral_scaled.slim --prefix nomig_neutral_scaled -p None -c 24 -f neutral -x /N/project/Prophysaongenomics/FILET_Organized_24January2023/programs/build/slim --scale 100  

