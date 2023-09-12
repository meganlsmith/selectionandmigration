#!/bin/bash
#SBATCH -A general
#SBATCH -J linkedp1_5000_nomig
#SBATCH -p general
#SBATCH -o linkedp1_5000_nomig_%j.txt
#SBATCH -e linkedp1_5000_nomig_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --time=96:00:00

module load python

python ./python_scripts/tskit_Drosophilamaps_to_msout_v2.py -d 5000 -r 1500 -s ./slim_scripts/nomig_linkedp1_drosophila.slim --prefix nomig_linkedp1_drosophila -p None -c 24 -f sweep -x /N/project/Prophysaongenomics/FILET_Organized_24January2023/programs/build/slim
