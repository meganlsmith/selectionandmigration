# Keywords: Python, tree-sequence recording, tree sequence recording

# This is a Python recipe; note that it runs the SLiM model internally, below

## usage: python neutral_tskit_to_msout.py -s slimfile.slim -r repnumber -p parfile -d divtime
## replace 'slimfile.slim' with the  name of your slim file
## replace 'repnumber' with your replicate number
## if migration in model replace parfile with the file with migration paramters, 
## else, replace with None
## replace div time with the desired divergence time

import msprime, pyslim
import os
import numpy as np
import sys
from optparse import OptionParser
import multiprocessing as mp
from os.path import exists

# A function to sample sites that, in the sampled individuals:
# a) do not have multiple mutations
# b) are not fixed for the ancestral allele
# c) are not fixed for the derived allele
# returns genotype matrix and positions
def sample_sites(ts):
    positions = []
    genotype_matrix = np.empty((0,40), int)
    for var in ts.variants():# loop through variants
        unique_genotypes = np.unique(var.genotypes) # get list of unique genotypes among sampled individuals
        if 2 not in unique_genotypes and len(unique_genotypes)>1: # filter sites with multiple mutations and sites that are fixed for a single allel
            genotype_matrix = np.vstack((genotype_matrix, var.genotypes))
            positions.append(str(var.position/10000))
    return(genotype_matrix, positions)

# A function to run SLiM
def slimulation(repnumber):

    if not exists("%s_%s_overlaid_ms.out" % (prefix, str(repnumber))):
       

        # get parameters and run SLiM if it is a migration model
        if options.paramsfile != 'None':
            parameters = open(options.paramsfile, 'r').readlines()
            linenumber = int(repnumber)-int(options.previous)-1
            print(repnumber, linenumber)
            currentparams = parameters[int(repnumber)-int(options.previous)-1].strip()
            tmig = currentparams.split()[0]
            pmig = currentparams.split()[1]
            slimfilerep = prefix+'_'+str(repnumber)+'.slim'
            os.system('cp ../%s %s' % (options.slimfile, slimfilerep))
            os.system("%s -d rep=%r -d tmig=%r -d pmig=%r -d divtime=%r %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, tmig, pmig, options.divtime, slimfilerep, prefix, repnumber))
            os.system('rm %s' % (slimfilerep))

        else: ### Run the SLiM model and load the resulting .trees
            slimfilerep = prefix+'_'+str(repnumber)+'.slim'
            os.system('cp ../%s %s' % (options.slimfile, slimfilerep))
            os.system("%s -d rep=%r -d divtime=%r %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, options.divtime, slimfilerep, prefix, repnumber))
            os.system('rm %s' % (slimfilerep))

        # load tree sequences
        ts = pyslim.load("%s_%s.trees" % (prefix, repnumber))
        
        ## recapitate if not background model
        if options.dfe in ('neutral', 'sweep', 'bgs'):
            ts = ts.recapitate(recombination_rate=5e-6, Ne=1250)

        # sample 10 individuals from each population
        alive = ts.individuals_alive_at(0)
        pops = [np.where(
                   ts.individual_populations[alive] == k)[0] for k in [1, 2]]
        sample_inds = [np.random.choice(pop, 10, replace=False) for pop in pops]
        keep_inds = np.concatenate(sample_inds)
    
        # simplify tree sequence to contain only ten individuals per population
        keep_nodes = []
        for i in keep_inds:
            keep_nodes.extend(ts.individual(i).nodes)
        ts = ts.simplify(keep_nodes)

        ## add neutral mutations
        if options.dfe in ('neutral'):
            mutrate = 1e-6
        elif options.dfe in ('bgs'):
            mutrate = 2.5e-7
        elif options.dfe in ('sweep'):
            mutrate = 1e-6

        ts = pyslim.SlimTreeSequence(msprime.mutate(ts, rate=mutrate, keep=True))
    
    
        ## dump 
        ts.dump("%s_%s_overlaid.trees" % (prefix, repnumber))
    
        ## get genotypes and positions of variants for the individuals included
        ## this function excludes sites that don't vary among sampled individuals
        ## it also excludes sites in which multiple mutations occurred in the history of the entire sample

        mygenotypematrix, mypositions = sample_sites(ts)

        # transpose genotype matrix for ms output
        tmygenotypematrix = mygenotypematrix.transpose()

        ## write tab separated output formatted ms style
        openfilename = '%s_%s_overlaid_ms.out' % (prefix, repnumber)
        outfile = open(openfilename, 'w')
        outfile.write('\n\n//\n')
        outfile.write('segsites: %r\n' % len(mypositions))
        outfile.write('positions: ')
        outfile.write(' '.join(mypositions))
        outfile.write('\n')
        outfile.close()
        outfile = open(openfilename, 'ab')
        np.savetxt(outfile, tmygenotypematrix, fmt="%s", delimiter="")
        outfile.close()
    
        # check for missing data, and if present, exit with error
        with open(openfilename) as f:
            if '-' in f.read():
                print('Rep %r PROBLEM: There is missing data in output. Ancestors did not coalesce.' % repnumber)

    else:
        print("Replicate %s already exists. Skipping." % repnumber)



# get command line input from user using optparse.
parser = OptionParser()
parser.add_option("-s","--slimfile", help="SLiM script to use for simulation",
                    action="store", type="string", dest="slimfile")
parser.add_option("-r","--numreps", help="Number of replicates to simulate",
                    default = 1, action="store", type="int", dest="numreps")
parser.add_option("-p","--paramsfile", help="Migration model parameters, if relevant. Default is None for divergence only.",
                    default='None', action="store", type="string", dest="paramsfile")
parser.add_option("-d","--divtime", help="Divergence time to use for simulations",
                    action="store", type="int", dest="divtime")
parser.add_option("-x","--slimexecutable", help="Path to slim executable",
                    default='slim', action="store", type="str", dest="slimexecutable")
parser.add_option("-c","--processors", help="Number of processors to use",
                    default=1, action="store", type="int", dest="processors")
parser.add_option("-f","--dfe", help="What DFE was used? neutral, bgs, or sweep",
                    default=1, action="store", type="string", dest="dfe")
parser.add_option("-o","--previous", help="Number of replicates previously simulated",
                    default = 1, action="store", type="int", dest="previous")

(options, args) = parser.parse_args()

if not options.slimfile:   # if slim script name is not given
    parser.error('SLiM file name not given')
if not options.divtime:   # if divergence time is not given
    parser.error('Divergence time not given')
if options.dfe not in ('bgs', 'neutral', 'sweep'):   # if dfe not supported
    parser.error('DFE not supported.')


prefix = options.slimfile.split('.slim')[0] # get prefix from SLiM file name.
folder = prefix+'_'+str(options.divtime)
# make a directory for output and copy params file
#os.mkdir(folder)
os.chdir(folder)
if options.paramsfile != 'None':
    os.system('cp ../%s ./' % options.paramsfile)

# intialize parallelization
pool = mp.Pool(options.processors)

# run SLiMulations and write output
print(int(options.previous)+1,options.numreps+1)
pool.map(slimulation, [rep for rep in range(int(options.previous)+1,options.numreps+1)])

pool.close()


os.chdir('../')
