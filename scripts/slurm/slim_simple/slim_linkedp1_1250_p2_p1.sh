#!/bin/bash
#SBATCH -A general
#SBATCH -J linkedp1_1250_p2_p1
#SBATCH -p general
#SBATCH -o linkedp1_1250_p2_p1_%j.txt
#SBATCH -e linkedp1_1250_p2_p1_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --time=96:00:00

module load python

python python_scripts/sample_parameters_slim.py -s p2_p1_linkedp1_scaled.slim -r 1500 -d 1250
python ./python_scripts/neutral_tskit_to_msout_v3.py -d 1250 -r 1500 -s ./slim_scripts/p2_p1_linkedp1_scaled.slim --prefix p2_p1_linkedp1_scaled -p ../params/p2_p1_linkedp1_scaled_params_1250.txt -c 24 -f sweep -x /N/project/Prophysaongenomics/FILET_Organized_24January2023/programs/build/slim
