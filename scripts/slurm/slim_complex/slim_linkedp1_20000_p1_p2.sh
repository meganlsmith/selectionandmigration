#!/bin/bash
#SBATCH -A r00279
#SBATCH -J linkedp1_20000_p1_p2
#SBATCH -p general
#SBATCH -o linkedp1_20000_p1_p2_%j.txt
#SBATCH -e linkedp1_20000_p1_p2_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --time=96:00:00

module load python/3.9.8

# Generate 4 random bytes from /dev/urandom and convert to hex
random_hex=$(od -N 4 -t x4 /dev/urandom | awk '{print $2}')

# Convert hex to decimal
random_seed=$((0x$random_hex))

echo "Random seed generated: $random_seed"

python python_scripts/sample_parameters_slim.py -s p1_p2_linkedp1_drosophila.slim -r 1500 -d 2000000

python ./python_scripts/tskit_Drosophilamaps_to_msout_v3.py -d 2000000 -r 1500 -s ./slim_scripts/p1_p2_linkedp1_drosophila.slim --prefix p1_p2_linkedp1_drosophila -p ../params/p1_p2_linkedp1_drosophila_params_2000000.txt -c 24 -f sweep -x /N/project/Prophysaongenomics/FILET_Organized_24January2023/programs/build/slim --scale 100 --seed $random_seed

