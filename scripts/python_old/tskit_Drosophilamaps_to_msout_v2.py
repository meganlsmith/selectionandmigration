import numpy as np
import sys
import selRegionsFromAnnot_MLS as selRegionsFromAnnot
import os
from optparse import OptionParser
import msprime, pyslim
import multiprocessing as mp

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

(options, args) = parser.parse_args()

if not options.slimfile:   # if slim script name is not given
    parser.error('SLiM file name not given')
if not options.divtime:   # if divergence time is not given
    parser.error('Divergence time not given')
if options.dfe not in ('bgs', 'neutral', 'sweep'):   # if dfe not supported
    parser.error('DFE not supported.')

def sample_sites(ts):
    positions = []
    genotype_matrix = np.empty((0,40), int)
    for var in ts.variants():# loop through variants
        unique_genotypes = np.unique(var.genotypes) # get list of unique genotypes among sampled individuals
        if 2 not in unique_genotypes and len(unique_genotypes)>1: # filter sites with multiple mutations and sites that are fixed for a single allel
            genotype_matrix = np.vstack((genotype_matrix, var.genotypes))
            positions.append(str(var.position/10000))
    return(genotype_matrix, positions)


# set variables that will be constant across simulations

# files to look at for annotations
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

# make folder for recombination and genetic maps
def slimulation(repnumber):
    prefix = options.slimfile.split('.slim')[0] # get prefix from SLiM file name.

    
    # get chromosome lengths
    chrLens = selRegionsFromAnnot.readChrLens(chrLenFileName)
    
    # get selection regions
    winC, winS, winE = selRegionsFromAnnot.pickRandomWindow(L, chrLens, gapFileName=gapFileName, numSubWins=1, state=np.random.get_state())
    
    # print which region we are using
    sys.stderr.write("modeling simulated region after %s:%d-%d\n" %(winC, winS, winE))
    
    # get annotation information
    sregionCoords, totSelRegionSize = selRegionsFromAnnot.readSelRegionsInWinFromGtf(geneAnnotFileName, winC, winS, winE, cncSelRatio, phastConsFileName=cncAnnotFileName, codingSelFrac=codingSelFrac, nonCodingSelFrac=nonCodingSelFrac)
    
    # get recombination map
    recregionCoords, totalRecRateInMorgans = selRegionsFromAnnot.readRecRegionsInWinFromWig(recRateFileName, winC, winS, winE, rRescale=rMean)
    
    
    # write recombination map to a file
    locationlist = []
    ratelist = []
    recombinationratefile = 'rfile.txt'
    with open(recombinationratefile, 'w') as f:
        for item in recregionCoords:
            end = item[1]
            rate = item[2]
            locationlist.append(item[0])
            ratelist.append(rate)
            f.write('%r\t%r\n' % (end, rate))
    locationlist.append(item[1])
    ratelist.append(0)
    ratelist = [i * 100 for i in ratelist]

            
    # write genome map to a file
    genomicmapfile = 'gfile.txt'
    with open(genomicmapfile, 'w') as f:
        for item in sregionCoords:
            begin = item[0]
            end = item[1]
            propdel = item[2]
            selratio = item[3]
            f.write('%r\t%r\t%r\t%r\t\n' % (begin, end, propdel, selratio))

    # run slimulation
        # get parameters and run SLiM if it is a migration model
    if options.paramsfile != 'None':
        parameters = open(options.paramsfile, 'r').readlines()
        currentparams = parameters[int(repnumber)-1].strip()
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
    
    # move the maps
    os.system('mv %s ./recombination_genetic_maps/rfile_%r.txt' % (recombinationratefile, repnumber))
    os.system('mv %s ./recombination_genetic_maps/gfile_%r.txt' % (genomicmapfile, repnumber))

    # load tree sequences
    ts = pyslim.load("%s_%s.trees" % (prefix, repnumber))
    
    ## recapitate 
    if options.dfe in ('neutral', 'sweep', 'bgs'):
        if len(locationlist) > 2:
            recmap = msprime.RecombinationMap(locationlist, ratelist)
            ts = ts.recapitate(recombination_map=recmap, Ne=1250)
        else:
            ts = ts.recapitate(recombination_rate=ratelist[0], Ne=1250)

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

    ## add neutral mutations if neutral simulation or sweep
    if options.dfe in ('neutral', 'sweep'):
        mutrate = np.random.uniform(3.445e-7, 3.445e-6)
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






prefix = options.slimfile.split('.slim')[0] # get prefix from SLiM file name.
folder = prefix+'_'+str(options.divtime)
# make a directory for output and copy params file
os.mkdir(folder)
os.chdir(folder)
os.mkdir('recombination_genetic_maps')
if options.paramsfile != 'None':
    os.system('cp ../%s ./' % options.paramsfile)


for i in range(1,options.numreps+1):
    slimulation(i)

os.chdir('../')
