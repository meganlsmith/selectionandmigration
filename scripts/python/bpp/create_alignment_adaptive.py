"""This script will get alignments from a directory, and create combos of alignments formatted as phylip files for input into BPP."""
import sys
import os
from Bio import AlignIO 
import numpy as np
import optparse

parser = optparse.OptionParser()
parser.add_option("-s", "--source", dest="source_directory", help="Source directory")
parser.add_option("-b", "--background", dest="background_directory", help="Background directory")
parser.add_option("-o", "--output", dest="output_directory", help="Output directory")
parser.add_option("-p", "--percentage", dest="percentage", type="int", help="Percentage")

(options, args) = parser.parse_args()

if not (options.source_directory and options.background_directory and options.output_directory and options.percentage):
    parser.error("Please provide all the required options")

source_directory = options.source_directory
background_directory = options.background_directory
output_directory = options.output_directory
percentage = options.percentage

# create the output directory
os.system('mkdir -p %s' % output_directory)

# set some parameters
maxloci = 10000
chunksize = 500
reps = 20
adaptiveloci = int(np.floor(percentage/100*chunksize))
backgroundloci = chunksize-adaptiveloci

# create file prefix
prefix = source_directory.strip('/').split("/")[-1]
background_prefix = background_directory.strip('/').split("/")[-1] 


# first draw which alignments to sample
adaptivelocilist = [*range(1,adaptiveloci*reps+1)]
backgroundlocilist = [*range(1,backgroundloci*reps+1)]

# break this into 20 lists
adaptivechunks = [adaptivelocilist[x:x+adaptiveloci] for x in range(0, len(adaptivelocilist), adaptiveloci)]
backgroundchunks = [backgroundlocilist[x:x+backgroundloci] for x in range(0, len(backgroundlocilist), backgroundloci)]

# iterate over the replicates
for count,item in enumerate(adaptivechunks):

    # get the outfile name
    outfilename = os.path.join(output_directory, prefix+ '_' + str(percentage)+'percent'+'_'+str(count+1)+'_alignment.phy')

    # open the outfile
    outfile = open(outfilename, 'w')

    for locus in item:

        # get the infile name
        prefix_subset = '_'.join(prefix.split('_')[:-1])
        infile = os.path.join(source_directory, prefix_subset+'_'+str(locus)+'.fa')

        # open the infile
        alignment = AlignIO.read(infile, 'fasta')
 
        # keep the middle 500 characters
        mid500 = [int(len(alignment[0])/2-chunksize/2), int(len(alignment[0])/2+chunksize/2)]
        alignment = alignment[:,mid500[0]:mid500[1]]

        # write to phylip
        outfile.write("%s %s\n" % (len(alignment), len(alignment[0])))
        for record in alignment:
            if int(record.id.split('n')[1]) < 10:
               outfile.write('^%s    %s\n' % (record.id, record.seq))
            else:
               outfile.write('^%s   %s\n' % (record.id, record.seq))
        outfile.write('\n')

    for locus in backgroundchunks[count]:

        # get the infile name
        prefix_subset = '_'.join(background_prefix.split('_')[:-1])
        infile = os.path.join(background_directory, prefix_subset+'_'+str(locus)+'.fa')

        # open the infile
        alignment = AlignIO.read(infile, 'fasta')
 
        # keep the middle 500 characters
        mid500 = [int(len(alignment[0])/2-chunksize/2), int(len(alignment[0])/2+chunksize/2)]
        alignment = alignment[:,mid500[0]:mid500[1]]

        # write to phylip
        outfile.write("%s %s\n" % (len(alignment), len(alignment[0])))
        for record in alignment:
            if int(record.id.split('n')[1]) < 10:
               outfile.write('^%s    %s\n' % (record.id, record.seq))
            else:
               outfile.write('^%s   %s\n' % (record.id, record.seq))
        outfile.write('\n')

    # close the outfile
    outfile.close()
