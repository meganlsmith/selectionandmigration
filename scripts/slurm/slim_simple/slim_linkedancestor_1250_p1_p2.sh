#!/bin/bash
#SBATCH -A general
#SBATCH -J linkedancestor_1250_p1_p2
#SBATCH -p general
#SBATCH -o linkedancestor_1250_p1_p2_%j.txt
#SBATCH -e linkedancestor_1250_p1_p2_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --time=96:00:00

module load python

python python_scripts/sample_parameters_slim.py -s p1_p2_linkedancestor_scaled.slim -r 1500 -d 1250
python ./python_scripts/neutral_tskit_to_msout_v3.py -d 1250 -r 1500 -s ./slim_scripts/p1_p2_linkedancestor_scaled.slim --prefix p1_p2_linkedancestor_scaled -p ../params/p1_p2_linkedancestor_scaled_params_1250.txt -c 24 -f sweep -x /N/project/Prophysaongenomics/FILET_Organized_24January2023/programs/build/slim
