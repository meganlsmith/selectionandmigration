"""This script will look at SLiM simulations,
find the average pi and the sd of pi in each population,
and do simulations in msmove that match the average pi,
or that match both the average and the standard deviation of pi."""

from optparse import OptionParser
import pandas as pd
import sample_parameters_functions
import numpy as np
import os
import sys


# get command line input from user using optparse.
parser = OptionParser()
parser.add_option("-t","--theta", help="starting point for theta.",
                    action="store", type="int", dest="starttheta")
parser.add_option("-p","--rho", help="starting point for rho ",
                    action="store", type="int", dest="startrho")
parser.add_option("-w","--window", help="Window size to use in simulation.",
                    action="store", type="str", dest="window")
parser.add_option("-r","--numreps", help="Number of replicates to simulate.",
                    action="store", type="int", dest="numreps")
parser.add_option("-d","--divtime", help="Divergence time (msmove units).",
                    action="store", type="float", dest="divtime")
parser.add_option("-i","--inputfile", help="Path to SLiM feature vector.",
                    action="store", type="str", dest="inputfile")
parser.add_option("-o","--outputfolder", help="Folder to store msmove output.",
                    action="store", type="str", dest="outputfolder")
parser.add_option("-s","--suffix", help="Suffix for organization.",
                    action="store", type="str", dest="suffix")
parser.add_option("-m","--msmovepath", help="Path to msmove.",
                    action="store", type="str", dest="msmovepath")
parser.add_option("-f","--filetpath", help="Path to filetpath.",
                    action="store", type="str", dest="filetpath")
(options, args) = parser.parse_args()

# make sure the user provided all necessary input and produce helpful message if not.
if not options.starttheta:   
    parser.error('Theta not given.')
if not options.startrho:   
    parser.error('Rho not given.')
if not options.divtime:   
    parser.error('Divergence time not given.')
if not options.window:   
    parser.error('Window Size not given.')
if not options.numreps:   
    parser.error('Number of replicates not given.')
if not options.inputfile:   
    parser.error('Input file not given.')
if not options.outputfolder:  
    parser.error('Output folder not given.')
if not options.suffix:  
    parser.error('Suffix not given.')
if not options.msmovepath:  
    parser.error('Path to msmove not given.')
if not options.filetpath:  
    parser.error('Path to FILET not given.')

# read in SLiM feature vector to calculate averages and sd of pop-specific pi.
slimfeaturecsv = pd.read_csv(options.inputfile, sep = '\t')
meanpi1 = slimfeaturecsv["pi1"].mean()
meanpi2 = slimfeaturecsv["pi2"].mean()
stdpi1 = slimfeaturecsv["pi1"].std()
stdpi2 = slimfeaturecsv["pi2"].std()

print('Mean pi1: %r\nMean pi2: %r\nStD pi1: %r\nStD pi2: %r' % (meanpi1, meanpi2, stdpi1, stdpi2))

# use a while loop to simulate data while changing theta until we match our mean pi values

theta = options.starttheta
go=True
model12 = options.outputfolder + '/mig12_' + options.suffix
model21 = options.outputfolder + '/mig21_' + options.suffix
modelnomig =options.outputfolder + '/nomig_' + options.suffix

os.system('mkdir -p %s ' % options.outputfolder)

while go==True:
    
    # get parameter files introgression, divtime, theta, rho, window, numreps, model
    sample_parameters_functions.sampleparameters(introgression=True, divtime=options.divtime, theta=theta, rho=options.startrho, window=options.window, numreps=100, model=model12)
    sample_parameters_functions.sampleparameters(introgression=True, divtime=options.divtime, theta=theta, rho=options.startrho, window=options.window, numreps=100, model=model21)
    sample_parameters_functions.sampleparameters(introgression=False, divtime=options.divtime, theta=theta, rho=options.startrho, window=options.window, numreps=100, model=modelnomig)
    
    # perform simulations
    os.mkdir('%s/trainingSims_%s' % (options.outputfolder, options.suffix))
    os.system('%s 40 100 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 -ev tbs 1 2 tbs <  %s_params_%s_%s_%s_%s.txt > %s/trainingSims_%s/mig12.msOut' % (options.msmovepath, model12, theta, options.startrho, options.window, options.divtime, options.outputfolder, options.suffix))
    os.system('%s 40 100 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 -ev tbs 2 1 tbs <  %s_params_%s_%s_%s_%s.txt > %s/trainingSims_%s/mig21.msOut' % (options.msmovepath, model21, theta, options.startrho, options.window, options.divtime, options.outputfolder, options.suffix))
    os.system('%s 40 100 -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 <  %s_params_%s_%s_%s_%s.txt > %s/trainingSims_%s/noMig.msOut' % (options.msmovepath, modelnomig, theta, options.startrho, options.window, options.divtime, options.outputfolder, options.suffix))

    # remove temp parameter files
    os.system('rm %r_params_%r_%r_%r_%r.txt' % (model12, theta, options.startrho, options.window, options.divtime))
    os.system('rm %r_params_%r_%r_%r_%r.txt' % (model21, theta, options.startrho, options.window, options.divtime))
    os.system('rm %r_params_%r_%r_%r_%r.txt' % (modelnomig, theta, options.startrho, options.window, options.divtime))
    
    # calculate summary statistics
    os.system('mkdir -p %s/trainingSimsStats_%s %s/trainingSets_%s' % (options.outputfolder, options.suffix, options.outputfolder, options.suffix))
    os.system('for inFile in `ls %s/trainingSims_%s/ | grep .msOut` ; do cat %s/trainingSims_%s/$inFile | %s/twoPopnStats_forML 20 20| python %s/normalizeTwoPopnStats.py None %s > %s/trainingSimsStats_%s/$inFile; done' % (options.outputfolder, options.suffix, options.outputfolder, options.suffix, options.filetpath, options.filetpath, options.window, options.outputfolder, options.suffix))
    os.system('python %s/buildThreeClassTrainingSet.py %s/trainingSimsStats_%s/ %s/trainingSets_%s/threeClass.fvec' % (options.filetpath, options.outputfolder, options.suffix, options.outputfolder, options.suffix))

    # remove simulations
    os.system('rm -r %r/trainingSims_%r' % (options.outputfolder, options.suffix))

    # calculate mean and standard deviation of within population pi
    msmovesumstats = pd.read_csv(options.outputfolder+'/trainingSets_'+options.suffix+'/threeClass.fvec', sep = '\t')
    simmeanpi1 = msmovesumstats["pi1"].mean()
    simmeanpi2 = msmovesumstats["pi2"].mean()
    simstdpi1 = msmovesumstats["pi1"].std()
    simstdpi2 = msmovesumstats["pi2"].std()
    print('SIMULATIONS: \nMean pi1: %r\nMean pi2: %r\nStD pi1: %r\nStD pi2: %r' % (simmeanpi1, simmeanpi2, simstdpi1, simstdpi2))

    # check to see how close we are to matching our slim simulations in terms of average pi
    propdifmeanpi1 = (simmeanpi1-meanpi1)/meanpi1
    propdifmeanpi2 = (simmeanpi2-meanpi2)/meanpi2
    print('MEAN PI 1 is %r away from the desired value.\nMEAN PI 2 is %r away from the desired value.' % (propdifmeanpi1, propdifmeanpi2))

    # decide what to do
    if(abs(propdifmeanpi1) < 0.05 and abs(propdifmeanpi2) < 0.05):
        # we are close enough, stop simulating
        finaltheta = theta
        go=False
    elif(propdifmeanpi1 <0):
        # pi is too low, increase theta
        change = np.random.randint(low=1, high=10, size=1)[0]
        theta = theta+change
    elif(propdifmeanpi1 >0):
        # pi is too high, decrease theta
        change = np.random.randint(low=1, high=10, size=1)[0]
        theta = theta-change
    if theta < 0:
       stop('ERROR: theta below 0')


print('Our final theta was %s' % theta)

    
# get parameter files
sample_parameters_functions.sampleparameters(True, options.divtime, theta, options.startrho, options.window, options.numreps, model12)
sample_parameters_functions.sampleparameters(True, options.divtime, theta, options.startrho, options.window, options.numreps, model21)
sample_parameters_functions.sampleparameters(False, options.divtime, theta, options.startrho, options.window, options.numreps, modelnomig)

# perform simulations
os.mkdir('%s/trainingSims_%s' % (options.outputfolder, options.suffix))
os.system('%r 40 %s -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 -ev tbs 1 2 tbs <  %r_params_%r_%r_%r_%r.txt > %r/trainingSims_%r/mig12.msOut' % (options.msmovepath, options.numreps, model12, theta, options.startrho, options.window, options.divtime, options.outputfolder, options.suffix))
os.system('%r 40 %s -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 -ev tbs 2 1 tbs <  %r_params_%r_%r_%r_%r.txt > %r/trainingSims_%r/mig21.msOut' % (options.msmovepath, options.numreps, model21, theta, options.startrho, options.window, options.divtime, options.outputfolder, options.suffix))
os.system('%r 40 %s -t tbs -r tbs tbs -I 2 20 20 -ej tbs 2 1 <  %r_params_%r_%r_%r_%r.txt > %r/trainingSims_%r/noMig.msOut' % (options.msmovepath, options.numreps, modelnomig, theta, options.startrho, options.window, options.divtime, options.outputfolder, options.suffix))

    
# calculate summary statistics
os.system('mkdir -p %s/trainingSimsStats_%s %s/trainingSets_%s' % (options.outputfolder, options.suffix, options.outputfolder, options.suffix))
os.system('for inFile in `ls %s/trainingSims_%s/ | grep .msOut` ; do cat %s/trainingSims_%s/$inFile | %s/twoPopnStats_forML 20 20| python %s/normalizeTwoPopnStats.py None %s > %s/trainingSimsStats_%s/$inFile; done' % (options.outputfolder, options.suffix, options.outputfolder, options.suffix, options.filetpath, options.filetpath, options.window, options.outputfolder, options.suffix))
os.system('python %s/buildThreeClassTrainingSet.py %s/trainingSimsStats_%s/ %s/trainingSets_%s/threeClass.fvec' % (options.filetpath, options.outputfolder, options.suffix, options.outputfolder, options.suffix))
    

