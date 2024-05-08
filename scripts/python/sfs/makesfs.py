"""This script will look to a directory with a set of .msout files. 
It will build X SFS by sampling with replacement X times a single SNP
from each .msout file and building a SFS with the sampled SNPs."""

import os
import pandas as pd
import numpy as np
import sys
import argparse
import math


def get_snps(input_directory, maxfiles, length):
    """This function will loop through the msout input files and get a list of list of SNPs in each file for sampling later."""

    msout_files = os.listdir(input_directory)
    msout_files = [x for x in msout_files if x.endswith('_ms.out')]
    keep = []
    for x in msout_files:
        if x.split('_')[0] == 'nomig':
            num = x.split('_')[3]
        else:
            num = x.split('_')[4]
        if int(num) <= maxfiles:
            keep.append(x)
    msout_files = sorted(keep, key=lambda x: int(x.split('_')[-3]))

    # list for storing SNPs.
    snps = []
    seg_sites = []
    
    # loop through input and store data as a matrix in the list of snps.
    for file in msout_files:
        with open(os.path.join(input_directory, file), 'r') as f:
            count=0
            for line in f.readlines():
                count+=1
                if 'segsites' in line:
                    nsites = int(line.split(': ')[1])
                    toskip = count+1
                    break
        data = pd.read_fwf(os.path.join(input_directory, file), skiprows=toskip, header=None, widths=[1]*nsites)
        data_matrix = data.to_numpy()
        
        mask = np.any((data_matrix != 0) & (data_matrix != 1), axis=0)
        filtered_data_matrix = data_matrix[:, ~mask]
        unique_elements = [np.unique(filtered_data_matrix[:, i]) for i in range(filtered_data_matrix.shape[1])]
        variable_columns = [i for i, unique_vals in enumerate(unique_elements) if len(unique_vals) > 1]
        filtered_data_matrix = filtered_data_matrix[:, variable_columns]

        snps.append(filtered_data_matrix)
        filtered_seg_sites = filtered_data_matrix.shape[1]
        seg_sites.append(filtered_seg_sites)
    
    # to caluclate monomorphic:
    # number invariant: length - seg_sites
    # sampling proportion: 1 / seg_sites
    # monomorphics = invariant * sampling proportion
    monomorphic = sum([int(round((length - x) * (1/x))) for x in seg_sites])
    
    return(snps, monomorphic)

def sample_snps(snps, x):
    """For X replicates, sample one SNP per matrix (with replacement)."""
    snp_samples = []
    for i in range(x):
        snp_sample = [A[:, np.random.randint(A.shape[1], size=1)] for A in snps] # iterate over each element A (a numpy array) in the snps list. generate a random integer index within the range of the second dimension (columns) of A. Select a random column from the array using that column number. assign the output to snp_sample.
        snp_samples.append(snp_sample)
    return(snp_samples)

def build_sfs(snp_samples, x, npop0, npop1):
    """For X replicates, built an SFS from sampled SNPs."""
    sfs_list = []
    for i in range(x):
        sfs = np.zeros((npop0+1, npop1+1)) 
        for thesnp in snp_samples[i]:
            pop0 = thesnp[0:npop0]
            pop1 = thesnp[npop0:(npop0+npop1+1)]
            pop0_1s = len([y for y in pop0 if y == 1])
            pop1_1s = len([y for y in pop1 if y == 1])
            sfs[pop0_1s,pop1_1s] += 1
        sfs_list.append(sfs)
    return(sfs_list)

def write_sfs(sfs_list, npop0, npop1, output_SFS1, output_SFS2, monomorphic):
    """Write SFS to output directory."""
    # Write dadi SFS to output file
    os.system('mkdir -p %s' % output_SFS1)
    for item in range(len(sfs_list)):
        output_file = os.path.join(output_SFS1, 'rep_%r.fs' % item)
        output_file = open(output_file, 'w')
        output_file.write('%r %r unfolded\n' % (npop0+1, npop1+1))
        towrite = ""
        for i in range(npop0+1):
            for j in range(npop1+1):
                towrite += str(int(sfs_list[item][i,j]))
                towrite += ' '
        output_file.write(towrite)
        output_file.close()

    # write fsc SFS to output file
    os.system('mkdir -p %s' % output_SFS2)
    for item in range(len(sfs_list)):
        output_file = os.path.join(output_SFS2, 'rep_%r.fs' % item)
        output_file = open(output_file, 'w')
        output_file.write('1 observation\n')
        output_file.write('2 %r %r\n' % (npop0, npop1))
        towrite = ""
        sfs_list[item][0,0] = monomorphic
        for i in range(npop0+1):
            for j in range(npop1+1):
                towrite += str(int(sfs_list[item][i,j]))
                towrite += ' '
        output_file.write(towrite)
        output_file.close()


if __name__ == "__main__":

    # Parse arguments
    parser = argparse.ArgumentParser(description='Process input and output folders')
    parser.add_argument('--input', dest="input", type=str,
                        help='an input folder with msout files.')
    parser.add_argument('--output1', dest="output1", type=str,
                        help='an output folder for dadi formatted files.')
    parser.add_argument('--output2', dest="output2", type=str,
                        help='an output folder for fsc formatted files.')
    parser.add_argument('--reps', dest="reps", type=int,
                        help='Number of replicates to perform.')
    parser.add_argument('--npop0', dest="npop0", type=int,
                        help='Number of samples from population 0.')
    parser.add_argument('--npop1', dest="npop1", type=int,
                        help='Number of samples from population 1.')
    parser.add_argument('--max', dest="max", type=int, default=math.inf,
                        help="Maximum number of simulated fragments to include (will include first n fragments")
    parser.add_argument('--length', dest="length", type=int,
                        help="Length of simulated fragments.")
    args = parser.parse_args()
    
    # get the list of lists of snps for sampling
    print('getting snps')
    snps, monomorphic = get_snps(args.input, args.max, args.length)
    
    # sample snps for sfs replicates
    print('sampling snps')
    sampled_snps = sample_snps(snps, args.reps)
    
    # build sfs for replicates
    print('building sfs')
    sfs = build_sfs(sampled_snps, args.reps, args.npop0, args.npop1)
    
    # write sfs to files
    print('writing sfs')
    write_sfs(sfs, args.npop0, args.npop1, args.output1, args.output2, monomorphic)
    
