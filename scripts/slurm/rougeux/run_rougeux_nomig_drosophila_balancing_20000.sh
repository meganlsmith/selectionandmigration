#!/bin/bash
#SBATCH -A r00279
#SBATCH -J rougeux_balancing_drosophila_20000
#SBATCH -p general 
#SBATCH -o rougeux_balancing_drosophila_20000_%j.txt
#SBATCH -e rougeux_balancing_drosophila_20000_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mls16@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=3
#SBATCH --cpus-per-task=1
#SBATCH --time=60:00:00

module load python
directory=DROSOPHILA-testing-redo-revisions/nomig_balancing_drosophila_20000_15percent
mkdir -p $directory
for i in $(seq 0 99); do
  (
    echo $i
    cd $directory
    python /N/project/Prophysaongenomics/FILET_Organized_24January2023/rougeux/scripts/script_inference_anneal2_newton_mis_new_models_revised_v2.py -o rep$i -f /N/project/Prophysaongenomics/FILET_Organized_24January2023/SFS-redo-revision/DROSOPHILA-testing-redo-revisions-v2/dadi/nomig_balancing_drosophila_20000_15percent/rep_$i.fs -m SI,SI2N,IM,IM2N,IM2m -p 40,50,60
    cd ../../
  ) & 
done

wait
