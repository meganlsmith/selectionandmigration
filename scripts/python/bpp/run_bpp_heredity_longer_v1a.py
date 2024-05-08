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
parser.add_option("--outputfolder", help="Destination of output files.",
                    action="store", type="string", dest="outputfolder")
parser.add_option("--outputfolder2", help="Destination of output files 2.",
                    action="store", type="string", dest="outputfolder2")
parser.add_option("--prefix", help="Prefix for naming output files.",
                    action="store", type="string", dest="prefix")

(options, args) = parser.parse_args()

# make the output directories
os.system('mkdir -p %s' % options.outputfolder)
os.system('mkdir -p %s' % options.outputfolder2)


chunks = 20

for item in range(1, chunks+1):

    # path to the alignment files
    alignment = os.path.join(options.alignmentfolder, options.prefix + '_' + str(item) + '_alignment.phy')

    # create the .ctl file
    template = open('./bpp_templates/A00_variable_heredity_longer.bpp.ctl', 'r')
    templatelines = template.readlines()
    template.close()
    newfile = os.path.join(options.outputfolder, options.prefix + '_' + str(item) + '.ctl')
    outfilename = os.path.join(options.outputfolder2, 'out_' + options.prefix + '_' + str(item) + '.txt')
    mcmcfilename = os.path.join(options.outputfolder2, 'mcmc_' + options.prefix + '_' + str(item) + '.txt')

    with open(newfile, 'w') as f:
        for line in templatelines:
            if 'seqfile' in line:
                newline = 'seqfile = %s\n' % alignment
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
    pbsfilename = os.path.join(options.outputfolder, options.prefix + '_' + str(item) + '.pbs')

    with open(pbsfilename, 'w') as f:
        f.write('#!/bin/bash\n')
        f.write('#SBATCH -A r00279\n')
        f.write('#SBATCH -J bpp_%s_%s\n' % (options.prefix, str(item)))
        f.write('#SBATCH -p general\n')
        f.write('#SBATCH -o bpp_%s_%s.out\n' % (options.prefix, str(item)))
        f.write('#SBATCH -e bpp_%s_%s.err\n' % (options.prefix, str(item)))
        f.write('#SBATCH --mail-type=FAIL\n')
        f.write('#SBATCH --mail-user=mls16@indiana.edu\n')
        f.write('#SBATCH --nodes=1\n')
        f.write('#SBATCH --ntasks-per-node=1\n')
        f.write('#SBATCH --time=96:00:00\n\n')
        f.write('module load python\n')
        f.write('./bpp-4.4.0-linux-x86_64/bin/bpp -cfile %s' % newfile)
    os.system('sbatch %s' % pbsfilename)
