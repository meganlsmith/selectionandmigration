"""This script will sample divergence times, migration times, and migration rates
from a grid and write them to a file for msmove to draw from.
It takes as input: theta, rho, window size for ms, divergence time, model,
presence or absence of gene flow, and number of reps.
It outputs a file called modelname_params_theta_rho_window_divtime.txt
which has theta\trho\twindow\tdivtime\tmigtime\tmigrate if migration is true,
or theta\trho\twindow\tdivtime if migration is false."""

# usage: sample_paramters.py -t theta -r rho -w window -x xreps -m modelid -g True or False -d divtime
# example: sample_paramters.py -t 50 -r 250 -w 10000 -x 10 -m mig12 -g True -d 0.25

import random
import numpy as np
import getopt
import sys
from optparse import OptionParser


# get command line input from user using optparse.
parser = OptionParser()
parser.add_option("-t","--theta", help="theta to use in simulation.",
                    action="store", type="int", dest="theta")
parser.add_option("-p","--rho", help="rho to use in simulation ",
                    action="store", type="int", dest="rho")
parser.add_option("-w","--window", help="Window size to use in simulation.",
                    action="store", type="str", dest="window")
parser.add_option("-r","--numreps", help="Number of paramters to draw from prior.",
                    action="store", type="int", dest="numreps")
parser.add_option("-m","--model", help="Name of model for which priors are being drawn.",
                    action="store", type="str", dest="model")
parser.add_option("-i","--introgression", help="Add flag to turn on introgresion.",
                    action="store_true", dest="introgression", default = False)
parser.add_option("-d","--divtime", help="Divergence time to use for model.",
                    action="store", type="float", dest="divtime")

(options, args) = parser.parse_args()

if not options.theta:   # if slim script name is not given
    parser.error('Theta not given.')
if not options.rho:   # if divergence time is not given
    parser.error('Rho not given.')
if not options.window:   # if divergence time is not given
    parser.error('Window Size not given.')
if not options.numreps:   # if divergence time is not given
    parser.error('Number of replicates not given.')
if not options.model:   # if divergence time is not given
    parser.error('Model name not given.')
if not options.divtime:   # if divergence time is not given
    parser.error('Divergence time not given.')


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




if options.introgression == True:
    # get paramters
    tmigsample = np.random.choice(tmigs, options.numreps) # sample migration time multipliers
    tmigsample = [i * options.divtime for i in tmigsample] # multiply migration mults by tdiv
    pmigsample = np.random.choice(pmigs, options.numreps) # sample props of migrants
    tdivsample = [options.divtime] * options.numreps # get list of div times
    thetasample = [options.theta] * options.numreps # get list of thetas
    rhosample = [options.rho] * options.numreps # get list of rhos
    windowsample = [options.window] * options.numreps # get list of windowsizes
    Sample = np.array([thetasample, rhosample, windowsample, tdivsample, 
        tmigsample, pmigsample]) # build nop array
    Sample = Sample.transpose() # transpose so each row has each paramter
    
    # write to output file
    outfilename = options.model+'_params_'+str(options.theta)+'_'+str(options.rho)+'_'+str(options.window)+'_'+str(options.divtime)+'.txt'
    np.savetxt(outfilename, Sample, fmt="%s", delimiter="\t")

elif options.introgression == False:

    # get paramters
    tdivsample = [options.divtime] * options.numreps # get list of div times
    thetasample = [options.theta] * options.numreps # get list of thetas
    rhosample = [options.rho] * options.numreps # get list of rhos
    windowsample = [options.window] * options.numreps # get list of windowsizes
    Sample = np.array([thetasample, rhosample, windowsample, tdivsample]) # build nop array
    Sample = Sample.transpose() # transpose so each row has each paramter

    # write to output file
    outfilename = options.model+'_params_'+str(options.theta)+'_'+str(options.rho)+'_'+str(options.window)+'_'+str(options.divtime)+'.txt'
    np.savetxt(outfilename, Sample, fmt="%s", delimiter="\t")
