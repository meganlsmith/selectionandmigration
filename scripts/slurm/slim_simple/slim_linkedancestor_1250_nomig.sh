#!/bin/bash
#SBATCH -A general
#SBATCH -J linkedancestor_1250_nomig
#SBATCH -p general
#SBATCH -o linkedancestor_1250_nomig_%j.txt
#SBATCH -e linkedancestor_1250_nomig_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --time=96:00:00

module load python

python ./python_scripts/neutral_tskit_to_msout_v3.py -d 1250 -r 1500 -s ./slim_scripts/nomig_linkedancestor_scaled.slim --prefix nomig_linkedancestor_scaled -p None -c 24 -f sweep -x /N/project/Prophysaongenomics/FILET_Organized_24January2023/programs/build/slim

