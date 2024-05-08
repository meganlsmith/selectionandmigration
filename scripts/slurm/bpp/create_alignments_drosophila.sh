#!/bin/bash
#SBATCH -A r00279 
#SBATCH -J drosophilaalignments                                  
#SBATCH -p general
#SBATCH -o drosophilaalignments_%j.txt
#SBATCH -e drosophilaalignments_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=10:00:00

module load python

# Neutral
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/DROSOPHILA-testing-redo-revisions-v2/nomig_neutral_drosophila_1250/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/DROSOPHILA-testing-redo-revisions-v2/nomig_neutral_drosophila_5000/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/DROSOPHILA-testing-redo-revisions-v2/nomig_neutral_drosophila_20000/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/DROSOPHILA-testing-redo-revisions-v2/p1_p2_neutral_drosophila_1250/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/DROSOPHILA-testing-redo-revisions-v2/p1_p2_neutral_drosophila_5000/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/DROSOPHILA-testing-redo-revisions-v2/p1_p2_neutral_drosophila_20000/ -o bpp_alignments

# BGS
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/DROSOPHILA-testing-redo-revisions-v2/nomig_bgs_drosophila_1250/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/DROSOPHILA-testing-redo-revisions-v2/nomig_bgs_drosophila_5000/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/DROSOPHILA-testing-redo-revisions-v2/nomig_bgs_drosophila_20000/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/DROSOPHILA-testing-redo-revisions-v2/p1_p2_bgs_drosophila_1250/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/DROSOPHILA-testing-redo-revisions-v2/p1_p2_bgs_drosophila_5000/ -o bpp_alignments
python ./python_scripts/create_alignment.py -s /N/project/Prophysaongenomics/FILET_Organized_24January2023/DROSOPHILA-testing-redo-revisions-v2/p1_p2_bgs_drosophila_20000/ -o bpp_alignments
