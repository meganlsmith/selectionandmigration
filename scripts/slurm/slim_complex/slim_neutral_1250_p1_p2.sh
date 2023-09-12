#!/bin/bash
#SBATCH -A general
#SBATCH -J neutral_1250_p1_p2
#SBATCH -p general
#SBATCH -o neutral_1250_p1_p2_%j.txt
#SBATCH -e neutral_1250_p1_p2_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --time=96:00:00

module load python
python python_scripts/sample_parameters_slim.py -s p1_p2_neutral_drosophila.slim -r 10000 -d 1250
python ./python_scripts/tskit_Drosophilamaps_to_msout_v2.py -d 1250 -r 10000 -s ./slim_scripts/p1_p2_neutral_drosophila.slim --prefix p1_p2_neutral_drosophila -p ../params/p1_p2_neutral_drosophila_params_1250.txt -c 24 -f neutral -x /N/project/Prophysaongenomics/FILET_Organized_24January2023/programs/build/slim --start 7279
