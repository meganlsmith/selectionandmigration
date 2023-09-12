#!/bin/bash
#SBATCH -A general
#SBATCH -J bgs_20000_p2_p1
#SBATCH -p general
#SBATCH -o bgs_20000_p2_p1_%j.txt
#SBATCH -e bgs_20000_p2_p1_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --time=96:00:00

module load python
python python_scripts/sample_parameters_slim.py -s p2_p1_bgs_drosophila.slim -r 10000 -d 20000
python ./python_scripts/tskit_Drosophilamaps_to_msout_v2.py -d 20000 -r 10000 -s ./slim_scripts/p2_p1_bgs_drosophila.slim --prefix p2_p1_bgs_drosophila -p ../params/p2_p1_bgs_drosophila_params_20000.txt -c 24 -f bgs -x /N/project/Prophysaongenomics/FILET_Organized_24January2023/programs/build/slim --start 7768
