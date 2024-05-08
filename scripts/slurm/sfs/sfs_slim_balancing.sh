#!/bin/bash
#SBATCH -A r00279
#SBATCH -J sfs_balancing_scaled
#SBATCH -p general
#SBATCH -o sfs_balancing_scaled_%j.txt
#SBATCH -e sfs_balancing_scaled_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mls16@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=18:00:00

module load python

python ./python_scripts/makesfs_adaptive.py --input ../SLiM-testing-redo-revisions/nomig_balancing_scaled_1250/ --output1 ./SLiM-testing-redo-revisions/dadi/nomig_balancing_scaled_1250_5percent/ --output2 ./SLiM-testing-redo-revisions/fsc/nomig_balancing_scaled_1250_5percent/ --reps 100 --npop0 20 --npop1 20 --max 10000 --maxadapt 1500 --percent 5 --background ../SLiM-testing-redo-revisions/nomig_neutral_scaled_1250/ --length 10000
python ./python_scripts/makesfs_adaptive.py --input ../SLiM-testing-redo-revisions/nomig_balancing_scaled_1250/ --output1 ./SLiM-testing-redo-revisions/dadi/nomig_balancing_scaled_1250_10percent/ --output2 ./SLiM-testing-redo-revisions/fsc/nomig_balancing_scaled_1250_10percent/ --reps 100 --npop0 20 --npop1 20 --max 10000 --maxadapt 1500 --percent 10 --background ../SLiM-testing-redo-revisions/nomig_neutral_scaled_1250/ --length 10000
python ./python_scripts/makesfs_adaptive.py --input ../SLiM-testing-redo-revisions/nomig_balancing_scaled_1250/ --output1 ./SLiM-testing-redo-revisions/dadi/nomig_balancing_scaled_1250_15percent/ --output2 ./SLiM-testing-redo-revisions/fsc/nomig_balancing_scaled_1250_15percent/ --reps 100 --npop0 20 --npop1 20 --max 10000 --maxadapt 1500 --percent 15 --background ../SLiM-testing-redo-revisions/nomig_neutral_scaled_1250/ --length 10000

python ./python_scripts/makesfs_adaptive.py --input ../SLiM-testing-redo-revisions/nomig_balancing_scaled_5000/ --output1 ./SLiM-testing-redo-revisions/dadi/nomig_balancing_scaled_5000_5percent/ --output2 ./SLiM-testing-redo-revisions/fsc/nomig_balancing_scaled_5000_5percent/ --reps 100 --npop0 20 --npop1 20 --max 10000 --maxadapt 1500 --percent 5 --background ../SLiM-testing-redo-revisions/nomig_neutral_scaled_5000/ --length 10000
python ./python_scripts/makesfs_adaptive.py --input ../SLiM-testing-redo-revisions/nomig_balancing_scaled_5000/ --output1 ./SLiM-testing-redo-revisions/dadi/nomig_balancing_scaled_5000_10percent/ --output2 ./SLiM-testing-redo-revisions/fsc/nomig_balancing_scaled_5000_10percent/ --reps 100 --npop0 20 --npop1 20 --max 10000 --maxadapt 1500 --percent 10 --background ../SLiM-testing-redo-revisions/nomig_neutral_scaled_5000/ --length 10000
python ./python_scripts/makesfs_adaptive.py --input ../SLiM-testing-redo-revisions/nomig_balancing_scaled_5000/ --output1 ./SLiM-testing-redo-revisions/dadi/nomig_balancing_scaled_5000_15percent/ --output2 ./SLiM-testing-redo-revisions/fsc/nomig_balancing_scaled_5000_15percent/ --reps 100 --npop0 20 --npop1 20 --max 10000 --maxadapt 1500 --percent 15 --background ../SLiM-testing-redo-revisions/nomig_neutral_scaled_5000/ --length 10000

python ./python_scripts/makesfs_adaptive.py --input ../SLiM-testing-redo-revisions/nomig_balancing_scaled_20000/ --output1 ./SLiM-testing-redo-revisions/dadi/nomig_balancing_scaled_20000_5percent/ --output2 ./SLiM-testing-redo-revisions/fsc/nomig_balancing_scaled_20000_5percent/ --reps 100 --npop0 20 --npop1 20 --max 10000 --maxadapt 1500 --percent 5 --background ../SLiM-testing-redo-revisions/nomig_neutral_scaled_20000/ --length 10000
python ./python_scripts/makesfs_adaptive.py --input ../SLiM-testing-redo-revisions/nomig_balancing_scaled_20000/ --output1 ./SLiM-testing-redo-revisions/dadi/nomig_balancing_scaled_20000_10percent/ --output2 ./SLiM-testing-redo-revisions/fsc/nomig_balancing_scaled_20000_10percent/ --reps 100 --npop0 20 --npop1 20 --max 10000 --maxadapt 1500 --percent 10 --background ../SLiM-testing-redo-revisions/nomig_neutral_scaled_20000/ --length 10000
python ./python_scripts/makesfs_adaptive.py --input ../SLiM-testing-redo-revisions/nomig_balancing_scaled_20000/ --output1 ./SLiM-testing-redo-revisions/dadi/nomig_balancing_scaled_20000_15percent/ --output2 ./SLiM-testing-redo-revisions/fsc/nomig_balancing_scaled_20000_15percent/ --reps 100 --npop0 20 --npop1 20 --max 10000 --maxadapt 1500 --percent 15 --background ../SLiM-testing-redo-revisions/nomig_neutral_scaled_20000/ --length 10000

python ./python_scripts/makesfs_adaptive.py --input ../SLiM-testing-redo-revisions/p1_p2_balancing_scaled_1250/ --output1 ./SLiM-testing-redo-revisions/dadi/p1_p2_balancing_scaled_1250_5percent/ --output2 ./SLiM-testing-redo-revisions/fsc/p1_p2_balancing_scaled_1250_5percent/ --reps 100 --npop0 20 --npop1 20 --max 10000 --maxadapt 1500 --percent 5 --background ../SLiM-testing-redo-revisions/p1_p2_neutral_scaled_1250/ --length 10000
python ./python_scripts/makesfs_adaptive.py --input ../SLiM-testing-redo-revisions/p1_p2_balancing_scaled_1250/ --output1 ./SLiM-testing-redo-revisions/dadi/p1_p2_balancing_scaled_1250_10percent/ --output2 ./SLiM-testing-redo-revisions/fsc/p1_p2_balancing_scaled_1250_10percent/ --reps 100 --npop0 20 --npop1 20 --max 10000 --maxadapt 1500 --percent 10 --background ../SLiM-testing-redo-revisions/p1_p2_neutral_scaled_1250/ --length 10000
python ./python_scripts/makesfs_adaptive.py --input ../SLiM-testing-redo-revisions/p1_p2_balancing_scaled_1250/ --output1 ./SLiM-testing-redo-revisions/dadi/p1_p2_balancing_scaled_1250_15percent/ --output2 ./SLiM-testing-redo-revisions/fsc/p1_p2_balancing_scaled_1250_15percent/ --reps 100 --npop0 20 --npop1 20 --max 10000 --maxadapt 1500 --percent 15 --background ../SLiM-testing-redo-revisions/p1_p2_neutral_scaled_1250/ --length 10000

python ./python_scripts/makesfs_adaptive.py --input ../SLiM-testing-redo-revisions/p1_p2_balancing_scaled_5000/ --output1 ./SLiM-testing-redo-revisions/dadi/p1_p2_balancing_scaled_5000_5percent/ --output2 ./SLiM-testing-redo-revisions/fsc/p1_p2_balancing_scaled_5000_5percent/ --reps 100 --npop0 20 --npop1 20 --max 10000 --maxadapt 1500 --percent 5 --background ../SLiM-testing-redo-revisions/p1_p2_neutral_scaled_5000/ --length 10000
python ./python_scripts/makesfs_adaptive.py --input ../SLiM-testing-redo-revisions/p1_p2_balancing_scaled_5000/ --output1 ./SLiM-testing-redo-revisions/dadi/p1_p2_balancing_scaled_5000_10percent/ --output2 ./SLiM-testing-redo-revisions/fsc/p1_p2_balancing_scaled_5000_10percent/ --reps 100 --npop0 20 --npop1 20 --max 10000 --maxadapt 1500 --percent 10 --background ../SLiM-testing-redo-revisions/p1_p2_neutral_scaled_5000/ --length 10000
python ./python_scripts/makesfs_adaptive.py --input ../SLiM-testing-redo-revisions/p1_p2_balancing_scaled_5000/ --output1 ./SLiM-testing-redo-revisions/dadi/p1_p2_balancing_scaled_5000_15percent/ --output2 ./SLiM-testing-redo-revisions/fsc/p1_p2_balancing_scaled_5000_15percent/ --reps 100 --npop0 20 --npop1 20 --max 10000 --maxadapt 1500 --percent 15 --background ../SLiM-testing-redo-revisions/p1_p2_neutral_scaled_5000/ --length 10000

python ./python_scripts/makesfs_adaptive.py --input ../SLiM-testing-redo-revisions/p1_p2_balancing_scaled_20000/ --output1 ./SLiM-testing-redo-revisions/dadi/p1_p2_balancing_scaled_20000_5percent/ --output2 ./SLiM-testing-redo-revisions/fsc/p1_p2_balancing_scaled_20000_5percent/ --reps 100 --npop0 20 --npop1 20 --max 10000 --maxadapt 1500 --percent 5 --background ../SLiM-testing-redo-revisions/p1_p2_neutral_scaled_20000/ --length 10000
python ./python_scripts/makesfs_adaptive.py --input ../SLiM-testing-redo-revisions/p1_p2_balancing_scaled_20000/ --output1 ./SLiM-testing-redo-revisions/dadi/p1_p2_balancing_scaled_20000_10percent/ --output2 ./SLiM-testing-redo-revisions/fsc/p1_p2_balancing_scaled_20000_10percent/ --reps 100 --npop0 20 --npop1 20 --max 10000 --maxadapt 1500 --percent 10 --background ../SLiM-testing-redo-revisions/p1_p2_neutral_scaled_20000/ --length 10000
python ./python_scripts/makesfs_adaptive.py --input ../SLiM-testing-redo-revisions/p1_p2_balancing_scaled_20000/ --output1 ./SLiM-testing-redo-revisions/dadi/p1_p2_balancing_scaled_20000_15percent/ --output2 ./SLiM-testing-redo-revisions/fsc/p1_p2_balancing_scaled_20000_15percent/ --reps 100 --npop0 20 --npop1 20 --max 10000 --maxadapt 1500 --percent 15 --background ../SLiM-testing-redo-revisions/p1_p2_neutral_scaled_20000/ --length 10000




