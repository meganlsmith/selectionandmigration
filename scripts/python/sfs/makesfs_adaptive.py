"""This script will look to a directory with a set of .msout files. 
It will build X SFS by sampling with replacement X times a single SNP
from each .msout file and building a SFS with the sampled SNPs.
It will samples a user-specified number of SNPs from the input file,
and will get the remaining number of SNPs from a background file."""

import os
import pandas as pd
import numpy as np
import sys
import argparse
import math
import random


def get_snps(input_directory, maxfiles, percent, background_directory, reps, maxadaptivefiles, length):
    """This function will loop through the msout input files and get a list of list of SNPs in each file for sampling later.
    It will pull percent files from the input_directory and 100 - percent files from the background directory.
    The process will be repeated for x replicates."""

    msout_files = os.listdir(input_directory)
    msout_files = [x for x in msout_files if x.endswith('_ms.out')]
    background_files = os.listdir(background_directory)
    background_files = [x for x in background_files if x.endswith('_ms.out')]

    # keep only correct number of background files (in the case of Drosophila test, where we have 10,000, this is a necesary step for consistency.
    
    # only do this part if necessary
    if maxfiles < len(background_files):
        keep_background = []
        for x in background_files:
            if x.split('_')[0] == 'nomig':
                num = x.split('_')[3]
            else:
                num = x.split('_')[4]
            if int(num) <= maxfiles:
                keep_background.append(x)
        background_files = sorted(keep_background, key=lambda x: int(x.split('_')[-3]))
    else:
        background_files = sorted(background_files)
        background_files = sorted(background_files, key=lambda x: int(x.split('_')[-3]))

    # keep only correct number of input files (in the case of test, where we have 2,000, this is a necesary step for consistency.
    if maxadaptivefiles < len(msout_files):
        keep_input = []
        for x in msout_files:
            if x.split('_')[0] == 'nomig':
                num = x.split('_')[3]
            else:
                num = x.split('_')[4]
            if int(num) <= maxadaptivefiles:
                keep_input.append(x)
        msout_files = sorted(keep_input, key=lambda x: int(x.split('_')[-3]))
    else:
        msout_files = sorted(msout_files)
        msout_files = sorted(msout_files, key=lambda x: int(x.split('_')[-3]))
 
    # sample specified percent from msout_files and remainder from background
    snp_replicates = []
    monomorphic_list = []

        
    # list for storing SNPs.
    snps_adaptive = []
    seg_sites_adaptive = []
    snps_background = []
    seg_sites_background = []
    
    # loop through input and store data as a matrix in the list of snps.
    for file in msout_files:
        with open(os.path.join(input_directory, file), 'r') as f:
            snpline = [x for x in f.readlines() if 'segsites' in x]
            nsites = int(snpline[0].split(": ")[1])
            toskip = 5
        data = pd.read_fwf(os.path.join(input_directory, file), skiprows=toskip, header=None, widths=[1]*nsites)
        data_matrix = data.to_numpy()

        mask = np.any((data_matrix != 0) & (data_matrix != 1), axis=0)
        filtered_data_matrix = data_matrix[:, ~mask]
        unique_elements = [np.unique(filtered_data_matrix[:, i]) for i in range(filtered_data_matrix.shape[1])]
        variable_columns = [i for i, unique_vals in enumerate(unique_elements) if len(unique_vals) > 1]
        filtered_data_matrix = filtered_data_matrix[:, variable_columns]

        snps_adaptive.append(filtered_data_matrix)
        filtered_seg_sites = filtered_data_matrix.shape[1]
        seg_sites_adaptive.append(filtered_seg_sites)

    # loop through input and store data as a matrix in the list of snps.
    for file in background_files:
        with open(os.path.join(background_directory, file), 'r') as f:
            snpline = [x for x in f.readlines() if 'segsites' in x]
            nsites = int(snpline[0].split(": ")[1])
            toskip = 5
        data = pd.read_fwf(os.path.join(background_directory, file), skiprows=toskip, header=None, widths=[1]*nsites)
        data_matrix = data.to_numpy()

        mask = np.any((data_matrix != 0) & (data_matrix != 1), axis=0)
        filtered_data_matrix = data_matrix[:, ~mask]
        unique_elements = [np.unique(filtered_data_matrix[:, i]) for i in range(filtered_data_matrix.shape[1])]
        variable_columns = [i for i, unique_vals in enumerate(unique_elements) if len(unique_vals) > 1]
        filtered_data_matrix = filtered_data_matrix[:, variable_columns]

        snps_background.append(filtered_data_matrix)
        filtered_seg_sites = filtered_data_matrix.shape[1]
        seg_sites_background.append(filtered_seg_sites)

    snp_replicates = []
    for rep in range(reps):
        
        # sample snps and monomorphics
        snps_adaptive_indices = random.sample(range(0, len(snps_adaptive)), int(np.ceil(percent/100 * maxfiles)))
        snps_adaptive_sample = [snps_adaptive[x] for x in snps_adaptive_indices]
        seg_sites_adaptive_sample = [seg_sites_adaptive[x] for x in snps_adaptive_indices]

        snps_background_indices = random.sample(range(0, len(snps_background)), int(maxfiles - (np.ceil(percent/100 * maxfiles))))
        snps_background_sample = [snps_background[x] for x in snps_background_indices]
        seg_sites_background_sample = [seg_sites_background[x] for x in snps_background_indices]

        sampled_snps = snps_adaptive_sample + snps_background_sample
        sampled_seg_sites = seg_sites_adaptive_sample + seg_sites_background_sample

        snp_replicates.append(sampled_snps)
        monomorphics = sum([int(round((length - x) * (1/x))) for x in sampled_seg_sites])
        monomorphic_list.append(monomorphics)
    
    return(snp_replicates, monomorphic_list)

def sample_snps(snp_replicates):
    """For X replicates, sample one SNP per matrix (with replacement)."""
    snp_samples = []
    for snp in snp_replicates:
        snp_sample = [A[:, np.random.randint(A.shape[1], size=1)] for A in snp]
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
        sfs_list[item][0,0] = monomorphic[item]
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
    parser.add_argument('--maxadapt', dest="maxadapt", type=int, default=math.inf,
                        help="Maximum number of simulated adaptive fragments to include (will include first n fragments")
    parser.add_argument('--percent', dest="percent", type=int, 
                        help="The percent of SNPs drawn from the input file. The remaining up to max will be drawn from the background file.")
    parser.add_argument('--background', dest="background", type=str,
                        help="Background file for drawing 100 minus percent of the SNPs.")
    parser.add_argument('--length', dest="length", type=int,
                        help="Length of simulated fragments.")

    args = parser.parse_args()
    
    # get the list of lists of snps for sampling
    print('getting snps')
    snp_replicates, monomorphics = get_snps(args.input, args.max, args.percent, args.background, args.reps, args.maxadapt, args.length)
    
    # sample snps for sfs replicates
    print('sampling snps')
    sampled_snps = sample_snps(snp_replicates)
    
    # build sfs for replicates
    print('build sfs')
    sfs = build_sfs(sampled_snps, args.reps, args.npop0, args.npop1)
    
    ## write sfs to files
    print('write sfs')
    write_sfs(sfs, args.npop0, args.npop1, args.output1, args.output2, monomorphics)

    
