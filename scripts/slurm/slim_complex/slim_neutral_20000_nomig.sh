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

# Generate 4 random bytes from /dev/urandom and convert to hex
random_hex=$(od -N 4 -t x4 /dev/urandom | awk '{print $2}')

# Convert hex to decimal
random_seed=$((0x$random_hex))

echo "Random seed generated: $random_seed"

python ./python_scripts/tskit_Drosophilamaps_to_msout_v3.py -d 2000000 -r 10000 -s ./slim_scripts/nomig_neutral_drosophila.slim --prefix nomig_neutral_drosophila -p None -c 24 -f neutral -x /N/project/Prophysaongenomics/FILET_Organized_24January2023/programs/build/slim --scale 100 --seed $random_seed  

