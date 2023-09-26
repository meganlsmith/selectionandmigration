"""this script will take as input a .msOut file and will convert it into a phylip file of a user-specified sequence length. 
We assume equal base probabilities and a Jukes-Cantor model."""

from optparse import OptionParser
import os
import numpy as np
import random

# get command line input from user using optparse.
parser = OptionParser()
parser.add_option("-m","--msout", help=".msOut file in msformat including position information in decimal format.",
                    action="store", type="string", dest="msout")
parser.add_option("-l","--length", help="Length of sequences to output.",
                    action="store", type="int", dest="length")
parser.add_option("-n", "--number", help="Number of simulated loci to process.",
                    action="store", type="int", dest="number")
parser.add_option("-o","--outputphylip", help="Destination of output phylip files.",
                    action="store", type="string", dest="outputphylip")


(options, args) = parser.parse_args()

os.system('mkdir -p %s' % options.outputphylip)

# first loop through the input file and find the loci
number_counted = 0 # counter to track number of loci
start=False # indicator to indicate if we're past the first few lines
totalcount = 0


# we will loop through the file and create a dictionary with key=locus number, values= positions, startread, stopread (where startread and stopread indicate where to start and stop reading the matrix in in terms of line numbers
locusdict = {}

with open(options.msout, 'r') as f:

    linecount = 0
    for line in f.readlines():

        if '//' in line: # if we're at the start of a new locus
            number_counted += 1 # increment our locus counter
            start=True # indicate that we're ready to start recording info

        if number_counted<=options.number and start == True: # if we should be recording info

            # get positions of variable sites
            if 'positions' in line: #  if we are at the list of positions
                
                positions = line.split(' ') # split based on space
                print(positions)
                positions.pop(0) # remove first item which is 'positions:'
                positions = [float(x) for x in positions] # conver to float 
                positions = [round(x * 10000) for x in positions] # convert to int based on 10000 bp simulations

                locusdict[number_counted]=[positions,linecount+1, linecount+41] 

             

        elif number_counted > options.number: # if we're at the number of loci we wanted.
            break
        linecount+=1


# now, for each entry in the locus dict read in the matrix
msout = open(options.msout, 'r')
msoutlines = msout.readlines()
msout.close()


for key in locusdict:
    matrix = msoutlines[locusdict[key][1]:locusdict[key][2]]
    matrix = [x.strip('\n') for x in matrix]
    matrix = [list(x) for x in matrix]
    matrix = [[int(y) for y in x] for x in matrix]
    matrix = np.array(matrix)
    colmatrix = matrix.transpose()
    
    # dictionary to store sequence data
    keyList = [*range(40)]
    myDict = {key: [] for key in keyList} 
  
    bpcount = 0 
    varcount = 0

    for variant in range(colmatrix.shape[1]):

        if bpcount >= options.length:
            thebreak=1
            break


        # get constant bases proce3eding hte variant
        while bpcount < locusdict[key][0][varcount] and bpcount < options.length :
            bpcount += 1
            thisbp = random.sample(['A', 'T', 'C', 'G'],1)
            for indkey in myDict:
                myDict[indkey].append(thisbp)
                
        if bpcount >= options.length:
            thebreak=2 
            break
 

        # record the variant
        letters = random.sample(['A', 'T', 'C', 'G'], 2) # sample two letters without replacement
        
        indcount = 0
    
        if len(set(colmatrix[variant])) > 2:
            skip=True
        else:
            skip=False
        if skip == False: 
            alleleA = list(set(colmatrix[variant]))[0]
            alleleB = list(set(colmatrix[variant]))[1]
            #print(colmatrix[variant])
            #print(set(colmatrix[variant]))
            for item in colmatrix[variant]:
                if item == alleleA:
                    myDict[indcount].append(letters[0])

                elif item == alleleB:
                    myDict[indcount].append(letters[1])

                #else:
                #     print(item)
                #     print(set(colmatrix[variant]))
                #     print(len(set(colmatrix[variant])))
                indcount+=1
            varcount+=1
            bpcount+=1



     
    # get constant bases after the variant
    while bpcount < options.length:
        bpcount += 1
        thisbp = random.sample(['A', 'T', 'C', 'G'],1)
        for indkey in myDict:
            myDict[indkey].append(thisbp)


    outfile = options.outputphylip + '/alignment_' + str(key) + '.phy'
    with open(outfile, 'w') as f:
        f.write('   40 ')
        f.write(str(options.length))
        f.write('\n')
        for indkey in myDict:
            totalcount+=1
            indkeynum = int(indkey)
            indstring = str(indkeynum).zfill(4)
            f.write(str(totalcount))
            f.write('^') 
            f.write(indstring)
            f.write(' ')
            for bp in myDict[indkey]:
                f.write(str(bp[0]))
            f.write('\n')

