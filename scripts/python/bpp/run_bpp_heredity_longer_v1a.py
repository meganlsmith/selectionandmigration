"""This script will grab a user-specified number of phylip files from a user-specified directory.
It will format them as BPP input, and it will record the migration parameters for the loci if relevant."""

from optparse import OptionParser
import os
import numpy as np
import random
import pandas as pd

# get command line input from user using optparse.
parser = OptionParser()
parser.add_option("-a","--alignmentfolder", help="folder with phylip formatted alignments.",
                    action="store", type="string", dest="alignmentfolder")
parser.add_option("-o","--outputfolder", help="Destination of output files.",
                    action="store", type="string", dest="outputfolder")
parser.add_option("-p","--outputfolder2", help="Destination of output files 2.",
                    action="store", type="string", dest="outputfolder2")
parser.add_option("--prefix", help="Prefix for naming output files.",
                    action="store", type="string", dest="prefix")

(options, args) = parser.parse_args()

# make the output directories
os.system('mkdir -p %s' % options.outputfolder)
os.system('mkdir -p %s' % options.outputfolder2)

# first draw which alignments to sample
locilist = [*range(10000)]

# break this into 20 lists
chunks = [locilist[x:x+500] for x in range(0, len(locilist), 500)]

count=0
for item in chunks:

    count+=1

    # concatenate the loci files
    outlocus = options.alignmentfolder + '/' + options.prefix + '_' + str(count) + '_alignment.phy'

    # create the .ctl file
    template = open('./bpp_templates/A00_variable_heredity_longer.bpp.ctl', 'r')
    templatelines = template.readlines()
    template.close()
    newfile = options.outputfolder + '/' +  options.prefix + '_' + str(count) + '.ctl'
    outfilename =  options.outputfolder2 + '/out_' + options.prefix + '_' + str(count) + '.txt'
    mcmcfilename = options.outputfolder2 + '/mcmc_' + options.prefix+ '_' + str(count) + '.txt'
    with open(newfile, 'w') as f:
        for line in templatelines:
            if 'seqfile' in line:
                newline = 'seqfile = %s\n' % outlocus
            elif 'outfile' in line:
                newline = 'outfile = %s\n' % outfilename
            elif 'mcmcfile' in line:
                newline = 'mcmcfile = %s\n' % mcmcfilename
            elif 'nloci' in line:
                newline = 'nloci = %r\n' % 500
            else:
                newline = line
            f.write(newline)

    # create and submit the pbs file
    pbsfilename = options.outputfolder + '/' + options.prefix + '_' + str(count) + '.pbs'

    with open(pbsfilename, 'w') as f:
        f.write('#!/bin/bash\n')
        f.write('#SBATCH -A r00279')
        f.write('#SBATCH -J bpp_%s_%s\n' % (options.prefix, str(count)))
        f.write('#SBATCH -p general\n')
        f.write('#SBATCH -o bpp_%s_%s.out\n' % (options.prefix, str(count)))
        f.write('#SBATCH -e bpp_%s_%s.err\n' % (options.prefix, str(count)))
        f.write('#SBATCH --nodes=1\n')
        f.write('#SBATCH --ntasks-per-node=1\n')
        f.write('#SBATCH --time=96:00:00\n\n')
        f.write('module load python\n')
        f.write('./bpp-4.4.0-linux-x86_64/bin/bpp -cfile %s' % newfile)
    os.system('sbatch %s' % pbsfilename)
