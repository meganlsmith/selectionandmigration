from functools import partial
import numpy as np
import sys
import selRegionsFromAnnot_MLS as selRegionsFromAnnot
import os
from optparse import OptionParser
import msprime, pyslim
import tskit
import multiprocessing as mp
import warnings
from os.path import exists
warnings.simplefilter('ignore', msprime.TimeUnitsMismatchWarning)

def parse_arguments():
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
    parser.add_option("-f","--dfe", help="What DFE was used? neutral, bgs, bgsh5, balancing, or sweep",
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
    parser.add_option("--seed", help="Seed for drawing mutation rate, recombination rate, fragments.",
                    action="store", type="int", dest="seed", default=1)
    

    (options, args) = parser.parse_args()

    if not options.slimfile:   # if slim script name is not given
        parser.error('SLiM file name not given')
    if not options.divtime:   # if divergence time is not given
        parser.error('Divergence time not given')
    if options.dfe not in ('bgs', 'bgsh5', 'neutral', 'sweep', 'balancing'):   # if dfe not supported
        parser.error('DFE not supported.')

    return options,args


def sample_sites(ts):
    """Returns a genotype matrix and the locations of snps."""
    positions = []
    genotype_matrix = np.empty((0,40), int)
    for var in ts.variants():# loop through variants
        genotype_matrix = np.vstack((genotype_matrix, var.genotypes))
        positions.append(str((var.position+1)/10000))
    return(genotype_matrix, positions)

# make folder for recombination and genetic maps
def slimulation(repnumber, options, seeds):

    np.random.seed(seeds[repnumber-1])
    
    annotDir='../drosophilaAnnotations/'
    chrLenFileName=annotDir+'chromolens_dm3_autosOnly.txt'
    recRateFileName=annotDir+'comeron.allMajArms.normalized.wig'
    gapFileName=annotDir+'gaps.bed'
    geneAnnotFileName=annotDir+'refSeqAnnot.dm3.ucsc.12212018.gtf.gz'
    cncAnnotFileName=annotDir+'phastConsElements15way_dm3.txt.gz'

    # ratios, ractions, lengths, and mean rates.
    codingSelFrac=0.75
    nonCodingSelFrac=0.75
    cncSelRatio=0.1
    rMean=2.3e-8
    L = 10000

    # define constants (unscaled)
    sel_bgs = -0.000133
    min_sel_sweep = 0.001
    max_sel_sweep = 0.005
    ancestral_Ne = 125000
    bgs_burnin = 2500000
    sweep_burnin = 100000
    balancing_burnin = 500000

    # scale the constants
    scaled_sel_bgs = sel_bgs*options.scale
    scaled_min_sel_sweep = min_sel_sweep*options.scale
    scaled_max_sel_sweep = max_sel_sweep*options.scale

    scaled_ancestral_Ne = int(ancestral_Ne/options.scale)
    scaled_divtime = int(options.divtime/options.scale)
    scaled_bgs_burnin = int(bgs_burnin/options.scale)
    scaled_sweep_burnin = int(sweep_burnin/options.scale)
    scaled_balancing_burnin = int(balancing_burnin/options.scale)

    # remove unscaled so we cannot accidentally use them
    del (sel_bgs, min_sel_sweep, max_sel_sweep, ancestral_Ne, bgs_burnin, sweep_burnin, balancing_burnin)

    if not exists("%s_%s_overlaid_ms.out" % (options.prefix, str(repnumber))): # check whether the output already exists

        if options.trees is None and options.overlaidtrees is None: # check whether the user provided tree sequence paths.

            # get chromosome lengths
            chrLens = selRegionsFromAnnot.readChrLens(chrLenFileName)

            # get selection regions
            winC, winS, winE = selRegionsFromAnnot.pickRandomWindow(L, chrLens, gapFileName=gapFileName, numSubWins=1, state=seeds[repnumber-1])

            # print which region we are using
            sys.stderr.write("modeling simulated region after %s:%d-%d\n" %(winC, winS, winE))

            # get annotation information
            sregionCoords, totSelRegionSize = selRegionsFromAnnot.readSelRegionsInWinFromGtf(geneAnnotFileName, winC, winS, winE, cncSelRatio, phastConsFileName=cncAnnotFileName, codingSelFrac=codingSelFrac, nonCodingSelFrac=nonCodingSelFrac)

            # get recombination map
            recregionCoords, totalRecRateInMorgans = selRegionsFromAnnot.readRecRegionsInWinFromWig(recRateFileName, winC, winS, winE, rRescale=rMean)

            # get recombination rate
            if len(recregionCoords)>1:
                sys.exit('Recombination rate list includes more than one value. Issue.')
            recombination_rate = recregionCoords[0][2]

            # draw mutation rate from prior
            mutrate = np.random.uniform(3.445e-9, 3.445e-8)

            # scale mutation and recombination rate
            scaled_recombination_rate = recombination_rate*options.scale
            scaled_mutrate = mutrate*options.scale

            # remove unsclaed mutation and recrate
            del (recombination_rate, mutrate)

            # write genome map to a file
            genomicmapfile = 'gfile_%s.txt' % str(repnumber)
            with open(genomicmapfile, 'w') as f:
                for item in sregionCoords:
                    begin = item[0]
                    end = item[1]
                    propdel = item[2]
                    selratio = item[3]
                    f.write('%r\t%r\t%r\t%r\t\n' % (begin, end, propdel, selratio))

            # set slim file name and copy file
            slimfilerep = options.prefix+'_'+str(repnumber)+'.slim'
            os.system('cp ../%s %s' % (options.slimfile, slimfilerep))

            # burnin is scaled_bgs_burnin for bgs, scaled_sweep_burnin for linked ancestor, scaled_balancing_burnin for balancing selection, and zero otherwise
            if options.dfe == 'bgs' or options.dfe == 'bgsh5':
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
                os.system("%s -d rep=%r -d tmig=%r -d pmig=%r -d divtime=%r -d npop=%r -d burnin=%r -d mutrate=%r -d sel_coding=%r -d sel_cnc=%r -d recrate=%r -seed %s %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, scaled_tmig, pmig, scaled_divtime, scaled_ancestral_Ne, scaled_burnin, scaled_mutrate, scaled_sel_bgs, scaled_sel_bgs*cncSelRatio, scaled_recombination_rate, seeds[repnumber-1], slimfilerep, options.prefix, repnumber))

            elif options.paramsfile == 'None' and options.dfe == 'bgs': # if no migration and bgs
                os.system("%s -d rep=%r -d divtime=%r -d npop=%r -d burnin=%r -d mutrate=%r -d sel_coding=%r -d sel_cnc=%r -d recrate=%r -seed %s %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, scaled_divtime, scaled_ancestral_Ne, scaled_burnin, scaled_mutrate, scaled_sel_bgs, scaled_sel_bgs*cncSelRatio, scaled_recombination_rate, seeds[repnumber-1], slimfilerep, options.prefix, repnumber))

            elif options.paramsfile != 'None' and options.dfe == 'bgsh5': # if migration and bgsh5
                os.system("%s -d rep=%r -d tmig=%r -d pmig=%r -d divtime=%r -d npop=%r -d burnin=%r -d mutrate=%r -d sel_coding=%r -d sel_cnc=%r -d recrate=%r -seed %s %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, scaled_tmig, pmig, scaled_divtime, scaled_ancestral_Ne, scaled_burnin, scaled_mutrate, scaled_sel_bgs, scaled_sel_bgs*cncSelRatio, scaled_recombination_rate, seeds[repnumber-1], slimfilerep, options.prefix, repnumber))

            elif options.paramsfile == 'None' and options.dfe == 'bgsh5': # if no migration and bgsh5
                os.system("%s -d rep=%r -d divtime=%r -d npop=%r -d burnin=%r -d mutrate=%r -d sel_coding=%r -d sel_cnc=%r -d recrate=%r -seed %s %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, scaled_divtime, scaled_ancestral_Ne, scaled_burnin, scaled_mutrate, scaled_sel_bgs, scaled_sel_bgs*cncSelRatio, scaled_recombination_rate, seeds[repnumber-1], slimfilerep, options.prefix, repnumber))

            elif options.paramsfile != 'None' and options.dfe == 'sweep': # if migration and sweep
                os.system("%s -d rep=%r -d tmig=%r -d pmig=%r -d divtime=%r -d npop=%r -d minsel=%r -d maxsel=%r -d burnin=%r -d recrate=%r -seed %s %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, scaled_tmig, pmig, scaled_divtime, scaled_ancestral_Ne, scaled_min_sel_sweep, scaled_max_sel_sweep, scaled_burnin, scaled_recombination_rate, seeds[repnumber-1], slimfilerep, options.prefix, repnumber))

            elif options.paramsfile == 'None' and options.dfe == 'sweep': # if no migration and sweep
                os.system("%s -d rep=%r -d divtime=%r -d npop=%r -d minsel=%r -d maxsel=%r -d burnin=%r -d recrate=%r -seed %s %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, scaled_divtime, scaled_ancestral_Ne, scaled_min_sel_sweep, scaled_max_sel_sweep, scaled_burnin, scaled_recombination_rate, seeds[repnumber-1], slimfilerep, options.prefix, repnumber))

            elif options.paramsfile != 'None' and options.dfe == 'balancing': # if migration and balancing
                os.system("%s -d rep=%r -d tmig=%r -d pmig=%r -d divtime=%r -d npop=%r -d burnin=%r -d recrate=%r -seed %s %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, scaled_tmig, pmig, scaled_divtime, scaled_ancestral_Ne, scaled_burnin, scaled_recombination_rate, seeds[repnumber-1], slimfilerep, options.prefix, repnumber))

            elif options.paramsfile == 'None' and options.dfe == 'balancing': # if no migration and blaancing
                os.system("%s -d rep=%r -d divtime=%r -d npop=%r -d burnin=%r -d recrate=%r -seed %s %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, scaled_divtime, scaled_ancestral_Ne, scaled_burnin, scaled_recombination_rate, seeds[repnumber-1], slimfilerep, options.prefix, repnumber))

            elif options.paramsfile != 'None': # if migration and neutral
                os.system("%s -d rep=%r -d tmig=%r -d pmig=%r -d divtime=%r -d npop=%r -d recrate=%r -seed %s %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, scaled_tmig, pmig, scaled_divtime, scaled_ancestral_Ne, scaled_recombination_rate, seeds[repnumber-1], slimfilerep, options.prefix, repnumber))

            elif options.paramsfile == 'None': # if no migration and neutral
                os.system("%s -d rep=%r -d divtime=%r -d npop=%r -d recrate=%r -seed %s %s > %s_%r_sliminfo.txt" % (options.slimexecutable, repnumber, scaled_divtime, scaled_ancestral_Ne, scaled_recombination_rate, seeds[repnumber-1], slimfilerep, options.prefix, repnumber))
        
            # remove slim file
            os.system('rm %s' % (slimfilerep))
    
            # move the maps
            os.system('mv %s ./recombination_genetic_maps/gfile_%r.txt' % (genomicmapfile, repnumber))

        if options.overlaidtrees is None: # if a path to overlaid trees files was not provided

            if options.trees is None: # if we created the trees using SLiM above
                orig_ts = tskit.load("%s_%s.trees" % (options.prefix, repnumber))

            else: # if we are loading the trees provided with options.trees

                orig_ts = tskit.load(os.path.join(options.trees, "%s_%s.trees" % (options.prefix, repnumber)))

                # get mutation and recombination rates from sliminfo file
                sliminfofilerep = os.path.join(options.trees, "%s_%r_sliminfo.txt" % (options.prefix, repnumber))

                if options.dfe == 'bgs' or options.dfe == 'bgsh5':
                    # get the mutation rate
                    with open(sliminfofilerep, 'r') as f:
                        for line in f.readlines():
                            if 'initializeMutationRate' in line:
                                scaled_mutrate =  line.strip().split("(")[1].split(")")[0]
                else:
                    # draw mutation rate from prior
                    mutrate = np.random.uniform(3.445e-9, 3.445e-8)

                    # scale mutation rate
                    scaled_mutrate = mutrate*options.scale


                # get recombinatio rate from file
                with open(sliminfofilerep, 'r') as f:
                    for line in f.readlines():
                        if 'initializeRecombinationRate' in line:
                            scaled_recombination_rate =  line.strip().split("(")[1].split(")")[0]

            # recapitate
            ts = pyslim.recapitate(orig_ts, recombination_rate=scaled_recombination_rate, ancestral_Ne=scaled_ancestral_Ne, random_seed=seeds[repnumber-1])
 
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

            # add neutral mutations for neutral, sweep, balancing.
            if options.dfe in ('neutral', 'sweep', 'balancing'):
                ts = msprime.sim_mutations(ts, rate=scaled_mutrate, model=msprime.SLiMMutationModel(type=5), keep=True, random_seed=seeds[repnumber-1])   

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

def main():

    # parse the arguments
    options, args = parse_arguments()

    # create the output directory
    folder = options.prefix+'_'+str(int(options.divtime/options.scale))
    os.system('mkdir -p %s' % folder)

    # change to the directory
    os.chdir(folder)

    # create a directory for storing genetic maps
    os.system('mkdir -p %s' % 'recombination_genetic_maps')

    # intialize parallelization
    pool = mp.Pool(options.processors)

    # get random seeds for drawing fragments, recombination rates, mutation rates
    rng = np.random.default_rng(options.seed)
    seeds = rng.integers(2**32, size=options.numreps)

    # run SLiMulations and write output
    slimulation_with_options = partial(slimulation, options=options, seeds=seeds)
    pool.map(slimulation_with_options, [rep for rep in range(int(options.previous)+1,options.numreps+1)])

    # close pool
    pool.close()

    # change directory
    os.chdir('../')

if __name__ == "__main__":
    main()
