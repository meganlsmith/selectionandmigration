#!/bin/bash
#SBATCH -A general
#SBATCH -J fsc_linkedp1_scaled_5000_nomig_15percent
#SBATCH -p general
#SBATCH -o fsc_linkedp1_scaled_5000_nomig_15percent_%j.txt
#SBATCH -e fsc_linkedp1_scaled_5000_nomig_15percent_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mls16@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=24
#SBATCH --time=96:00:00

# FSC OPTIONS
# -t Name of template parameter file.
# -e Name of parameter prior definition file.
# -n Number of simulatioins to perform.
# -d Compute the SFS for the derived alleles.
# -M Perform parameter estimation by maximum composite likelihood from the SFS.
# -L Number of ECM cycles to be performed when estimating parameters from SFS.
# -q Quiet
# -u Generates or uses multidimensional SFS.
# -c Number of threads to use.

mkdir -p SLiM-testing-redo/fsc_linkedp1_scaled_5000_nomig_15percent
cd SLiM-testing-redo/fsc_linkedp1_scaled_5000_nomig_15percent
for i in {0..100}
do
  mkdir -p rep_$i;
  cd rep_$i;
  cp ../../../../SFS-redo/SLiM-testing-redo/fsc/nomig_linkedp1_scaled_5000_15percent/rep_$i.fs ./Nomig_5000_DSFS.obs;
  cp ../../../fsc_files/Nomig_5000.tpl ./;
  cp ../../../fsc_files/Nomig_5000.est ./;
  ../../../programs/fsc27_linux64_new/fsc27093 -t Nomig_5000.tpl -e Nomig_5000.est -n 100000 -d -M -L 40 -q -u -c 24;
  cd ../
done
cd ../../



