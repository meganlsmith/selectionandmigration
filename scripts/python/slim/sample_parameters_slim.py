"""This script will sample migration times, and migration rates
from a grid and write them to a file for slim to draw from.
It takes as input: SLiM file name, the number of reps, and a divergencetime.
It outputs a file called modelname_params_divtime.txt
which has migtime\tmigrate."""

# usage: sample_paramters.py -s slimfilename -r numreps -d divtime
# example: sample_paramters.py -s p1_p2_deleterious_scaled.slim -r 10 -d 1250

import random
import numpy as np
from optparse import OptionParser
import sys

# get command line input from user using optparse.
parser = OptionParser()
parser.add_option("-s","--slimfile", help="SLiM script to use for simulation",
                    action="store", type="string", dest="slimfile")
parser.add_option("-r","--numreps", help="Number of replicates to simulate",
                    default = 1, action="store", type="int", dest="numreps")
parser.add_option("-d","--divtime", help="Divergence time to use for simulations",
                    action="store", type="int", dest="divtime")

(options, args) = parser.parse_args()

if not options.slimfile:   # if slim script name is not given
    parser.error('SLiM file name not given')
if not options.divtime:   # if divergence time is not given
    parser.error('Divergence time not given')


# multipliers for tmig (actual tmig is value * tdiv)
tmigs = [0.01, 0.05, 0.10, 0.15, 0.20,
        0.25, 0.30, 0.35, 0.40, 0.45,
        0.50, 0.55, 0.60, 0.65, 0.70,
        0.75, 0.80, 0.85, 0.90]

# proportions of migrants to consider
pmigs = [0.05, 0.10, 0.15, 0.20,
        0.25, 0.30, 0.35, 0.40, 0.45,
        0.50, 0.55, 0.60, 0.65, 0.70,
        0.75, 0.80, 0.85, 0.90, 0.95]




# get paramters
tmigsample = np.random.choice(tmigs, options.numreps) # sample migration time multipliers
tmigsample = [np.ceil(i * options.divtime) for i in tmigsample] # multiply migration mults by tdiv
pmigsample = np.random.choice(pmigs, options.numreps) # sample props of migrants
Sample = np.array([tmigsample, pmigsample]) # build nop array
Sample = Sample.transpose() # transpose so each row has each paramter

# write to output file
outfilename = './params/'+options.slimfile.split('.slim')[0]+'_params_'+str(options.divtime)+'.txt'
np.savetxt(outfilename, Sample, fmt="%s", delimiter="\t")
