# Keywords: Python, tree-sequence recording, tree sequence recording

# This is a Python recipe; note that it runs the SLiM model internally, below

## usage: python neutral_tskit_to_msout.py -s slimfile.slim -r numreps -p parfile -d divtime -x slimexecutable -c processors -f dfe -o previous --prefix prefix --trees trees --scale scale --overlaidtrees overlaidtrees
## See help messages to understand parameters.

import tskit
import msprime, pyslim
import os
import numpy as np
import sys
from optparse import OptionParser
import multiprocessing as mp
from os.path import exists
import warnings
warnings.simplefilter('ignore', msprime.TimeUnitsMismatchWarning)

def sample_sites(ts):
    """Returns a genotype matrix and the locations of snps."""
    positions = []
    genotype_matrix = np.empty((0,40), int)
    for var in ts.variants():# loop through variants
        genotype_matrix = np.vstack((genotype_matrix, var.genotypes))
        positions.append(str((var.position+1)/10000))
    return(genotype_matrix, positions)

def slimulation(repnumber):

    """Runs slim (unless trees are provided), performs recapitation and adds neutral mutations (unless overlaid trees are provided) and outputs a fasta file and a ms-style output file."""

    # define constants (unscaled)
    recombination_rate = 5e-8
    mutrate_neutral = 1e-8
    mutrate_sweep = 1e-8
    neutral_mutrate_bgs = 2.5e-9
    deleterious_mutrate_bgs = 7.5e-9 
    sel_bgs = -0.000133
    min_sel_sweep = 0.001
    max_sel_sweep = 0.005
    ancestral_Ne = 125000
    bgs_burnin = 2500000
    sweep_burnin = 100000
    balancing_burnin = 500000

    # scale the constants
    scaled_recombination_rate = recombination_rate*options.scale
    scaled_mutrate_neutral = mutrate_neutral*options.scale
    scaled_mutrate_sweep = mutrate_sweep*options.scale
    scaled_neutral_mutrate_bgs = neutral_mutrate_bgs*options.scale
    scaled_deleterious_mutrate_bgs = deleterious_mutrate_bgs*options.scale
    scaled_sel_bgs = sel_bgs*options.scale
    scaled_min_sel_sweep = min_sel_sweep*options.scale
    scaled_max_sel_sweep = max_sel_sweep*options.scale

    scaled_ancestral_Ne = int(ancestral_Ne/options.scale)
    scaled_divtime = int(options.divtime/options.scale)
    scaled_bgs_burnin = int(bgs_burnin/options.scale)
    scaled_sweep_burnin = int(sweep_burnin/options.scale)
    scaled_balancing_burnin = int(balancing_burnin/options.scale)

    # remove unscaled so we cannot accidentally use them
    del (recombination_rate, mutrate_neutral, mutrate_sweep, neutral_mutrate_bgs, deleterious_mutrate_bgs, sel_bgs, min_sel_sweep, max_sel_sweep, ancestral_Ne, bgs_burnin, sweep_burnin, balancing_burnin)

    if not exists("%s_%s_overlaid_ms.out" % (options.prefix, str(repnumber))): # check whether the output already exists
       
        if options.trees is None and options.overlaidtrees is None: # check whether the user provided tree sequence paths.

            # set slim file name and copy file
            slimfilerep = options.prefix+'_'+str(repnumber)+'.slim'
            os.system('cp ../%s %s' % (options.slimfile, slimfilerep))

            ## set parameters based on model

            # SLiM mutation rate is equal to the deleterious mutation rate if the model is bgs and zero otherwise.
            if options.dfe == 'bgs':
                scaled_slim_mutrate = scaled_deleterious_mutrate_bgs
            else:
                scaled_slim_mutrate = 0

            # burnin is scaled_bgs_burnin for bgs, scaled_sweep_burnin for linked ancestor, scaled_balancing_burnin for balancing selection, and zero otherwise
            if options.dfe == 'bgs':
                scaled_burnin = scaled_bgs_burnin
            elif options.dfe == 'sweep' and 'ancestor' in options.prefix:
                scaled_burnin = scaled_sweep_burnin
            elif options.dfe == 'balancing':
                scaled_burnin = scaled_balancing_burnin
            else:
                scaled_burnin = 0

            # get parameters if our model includes migration
            if options.paramsfile != "None":
                parameters = open(options.paramsfile, 'r').readlines()  # open the parameter file
                linenumber = int(repnumber)-1 # get the line to use for current parameters
                currentparams = parameters[linenumber].strip() # retrieve the line
                scaled_tmig = int(float(currentparams.split()[0])/ options.scale) # get the migration time, and adjust it for scale
                pmig = currentparams.split()[1] # get p

            # run SLiM
            if options.paramsfile != 'None' and options.dfe == 'bgs': # if migration and bgs
                os.system("%s -d rep=%r -d tmig=%r -d pmig=%r -d divtime=%r -d npop=%r -d recrate=%r -d burnin=%r -d mutrate=%r -d sel=%r %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, scaled_tmig, pmig, scaled_divtime, scaled_ancestral_Ne, scaled_recombination_rate, scaled_burnin, scaled_slim_mutrate, scaled_sel_bgs, slimfilerep, options.prefix, repnumber))

            elif options.paramsfile == 'None' and options.dfe == 'bgs': # if no migration and bgs
                os.system("%s -d rep=%r -d divtime=%r -d npop=%r -d recrate=%r -d burnin=%r -d mutrate=%r -d sel=%r  %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, scaled_divtime, scaled_ancestral_Ne, scaled_recombination_rate, scaled_burnin, scaled_slim_mutrate, scaled_sel_bgs, slimfilerep, options.prefix, repnumber))

            elif options.paramsfile != 'None' and options.dfe == 'sweep': # if migration and sweep
                os.system("%s -d rep=%r -d tmig=%r -d pmig=%r -d divtime=%r -d npop=%r -d recrate=%r -d minsel=%r -d maxsel=%r -d burnin=%r %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, scaled_tmig, pmig, scaled_divtime, scaled_ancestral_Ne, scaled_recombination_rate, scaled_min_sel_sweep, scaled_max_sel_sweep, scaled_burnin, slimfilerep, options.prefix, repnumber))

            elif options.paramsfile == 'None' and options.dfe == 'sweep': # if no migration and sweep
                os.system("%s -d rep=%r -d divtime=%r -d npop=%r -d recrate=%r -d minsel=%r -d maxsel=%r -d burnin=%r %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, scaled_divtime, scaled_ancestral_Ne, scaled_recombination_rate, scaled_min_sel_sweep, scaled_max_sel_sweep, scaled_burnin, slimfilerep, options.prefix, repnumber))

            elif options.paramsfile != 'None' and options.dfe == 'balancing': # if migration and balancing
                os.system("%s -d rep=%r -d tmig=%r -d pmig=%r -d divtime=%r -d npop=%r -d recrate=%r -d burnin=%r %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, scaled_tmig, pmig, scaled_divtime, scaled_ancestral_Ne, scaled_recombination_rate, scaled_burnin, slimfilerep, options.prefix, repnumber))

            elif options.paramsfile == 'None' and options.dfe == 'balancing': # if no migration and blaancing
                os.system("%s -d rep=%r -d divtime=%r -d npop=%r -d recrate=%r -d burnin=%r %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, scaled_divtime, scaled_ancestral_Ne, scaled_recombination_rate, scaled_burnin, slimfilerep, options.prefix, repnumber))

            elif options.paramsfile != 'None': # if migration and neutral
                os.system("%s -d rep=%r -d tmig=%r -d pmig=%r -d divtime=%r -d npop=%r -d recrate=%r %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, scaled_tmig, pmig, scaled_divtime, scaled_ancestral_Ne, scaled_recombination_rate, slimfilerep, options.prefix, repnumber))

            elif options.paramsfile == 'None': # if no migration and neutral
                os.system("%s -d rep=%r -d divtime=%r -d npop=%r -d recrate=%r %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, scaled_divtime, scaled_ancestral_Ne, scaled_recombination_rate, slimfilerep, options.prefix, repnumber))
        
        # remove slim file
        os.system('rm %s' % (slimfilerep))
            

        if options.overlaidtrees is None: # if a path to overlaid trees files was not provided
            if options.trees is None: # if we created the trees using SLiM above
                orig_ts = tskit.load("%s_%s.trees" % (options.prefix, repnumber))
            else: # if we are loading the trees provided with options.trees
                orig_ts = tskit.load(os.path.join(options.trees, "%s_%s.trees" % (options.prefix, repnumber)))


            # recapitate
            ts = pyslim.recapitate(orig_ts, recombination_rate=scaled_recombination_rate, ancestral_Ne=scaled_ancestral_Ne)


            # sample 10 individuals from each population
            alive = pyslim.individuals_alive_at(ts, 0)
            pops = [np.where(
                       ts.individual_populations[alive] == k)[0] for k in [1, 2]]
            sample_inds = [np.random.choice(pop, 10, replace=False) for pop in pops]
            keep_inds = np.concatenate(sample_inds)
    
            # simplify tree sequence to contain only ten individuals per population
            keep_nodes = []
            for i in keep_inds:
                keep_nodes.extend(ts.individual(i).nodes)
            ts = ts.simplify(keep_nodes)

            # add neutral mutations
            if options.dfe in ('neutral'):
                scaled_mutrate = scaled_mutrate_neutral
            elif options.dfe in ('bgs'):
                scaled_mutrate = scaled_neutral_mutrate_bgs
            elif options.dfe in ('sweep','balancing'):
                scaled_mutrate = scaled_mutrate_sweep

            ts = msprime.sim_mutations(ts, rate=scaled_mutrate, model=msprime.SLiMMutationModel(type=5), keep=True)   
    
            # dump 
            ts.dump("%s_%s_overlaid.trees" % (options.prefix, repnumber))
    
        else: # if overlaidtrees were provided
            ts = tskit.load(os.path.join(options.overlaidtrees, "%s_%s_overlaid.trees" % (options.prefix, repnumber)))

        ## get genotypes and positions of variants for the individuals included
        mygenotypematrix, mypositions = sample_sites(ts)

        # transpose genotype matrix for ms output
        tmygenotypematrix = mygenotypematrix.transpose()

        ## write tab separated output formatted ms style
        openfilename = '%s_%s_overlaid_ms.out' % (options.prefix, repnumber)
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
                print('Rep %r PROBLEM: There is missing data in output.' % repnumber)

        # add nucleotides
        nts = pyslim.generate_nucleotides(ts)
        nts = pyslim.convert_alleles(nts)

        # write fasta
        nts.write_fasta("%s_%s.fa" % (options.prefix, repnumber))

    else: # if output files already exist for the replicate
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
parser.add_option("-f","--dfe", help="What DFE was used? neutral, bgs, balancing, or sweep",
                    action="store", type="string", dest="dfe")
parser.add_option("-o","--previous", help="Number of replicates previously simulated",
                    default = 0, action="store", type="int", dest="previous")
parser.add_option("--prefix", help="Prefix for naming file",
                    action="store", type="string", dest="prefix")
parser.add_option("--trees", help="Path to slim tree sequences without overlaid mutations.",
                    action="store", type="string", dest="trees", default=None)
parser.add_option("--scale", help="Factor by which to scale mutation rates, etc.",
                    action="store", type="int", dest="scale", default=1)
parser.add_option("--overlaidtrees", help="Path to slim tree sequences with overlaid mutations.",
                    action="store", type="string", dest="overlaidtrees", default=None)

(options, args) = parser.parse_args()

if not options.slimfile:   # if slim script name is not given
    parser.error('SLiM file name not given')
if not options.divtime:   # if divergence time is not given
    parser.error('Divergence time not given')
if options.dfe not in ('bgs', 'neutral', 'sweep', 'balancing'):   # if dfe not supported
    parser.error('DFE not supported.')


folder = options.prefix+'_'+str(int(options.divtime/options.scale))

# make a directory for output and copy params file
os.system('mkdir -p %s' % folder)
os.chdir(folder)

# intialize parallelization
pool = mp.Pool(options.processors)

# run SLiMulations and write output
pool.map(slimulation, [rep for rep in range(int(options.previous)+1,options.numreps+1)])

pool.close()


os.chdir('../')
