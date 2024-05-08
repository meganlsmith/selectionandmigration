#!/bin/bash
#SBATCH -A r00279 
#SBATCH -J slimalignments                                  
#SBATCH -p general
#SBATCH -o slimalignments_%j.txt
#SBATCH -e slimalignments_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=10:00:00

module load python

# Neutral
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/SLiM-testing-redo-revisions/nomig_neutral_scaled_1250/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/SLiM-testing-redo-revisions/nomig_neutral_scaled_5000/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/SLiM-testing-redo-revisions/nomig_neutral_scaled_20000/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/SLiM-testing-redo-revisions/p1_p2_neutral_scaled_1250/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/SLiM-testing-redo-revisions/p1_p2_neutral_scaled_5000/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/SLiM-testing-redo-revisions/p1_p2_neutral_scaled_20000/ -o bpp_alignments

# BGS
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/SLiM-testing-redo-revisions/nomig_bgs_scaled_1250/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/SLiM-testing-redo-revisions/nomig_bgs_scaled_5000/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/SLiM-testing-redo-revisions/nomig_bgs_scaled_20000/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/SLiM-testing-redo-revisions/p1_p2_bgs_scaled_1250/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/SLiM-testing-redo-revisions/p1_p2_bgs_scaled_5000/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/SLiM-testing-redo-revisions/p1_p2_bgs_scaled_20000/ -o bpp_alignments
