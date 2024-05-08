"""This script will get alignments from a directory, and create combos of alignments formatted as phylip files for input into BPP."""
import sys
import os
from Bio import AlignIO 
import optparse

parser = optparse.OptionParser()
parser.add_option("-s", "--source", dest="source_directory", help="Source directory")
parser.add_option("-o", "--output", dest="output_directory", help="Output directory")

(options, args) = parser.parse_args()

if not (options.source_directory and options.output_directory):
    parser.error("Please provide all the required options")

source_directory = options.source_directory
output_directory = options.output_directory

# get directory name
os.system('mkdir -p %s' % output_directory)

# set some parameters
maxloci = 10000
chunksize = 500

# create file prefix
prefix = source_directory.strip('/').split("/")[-1]

# first draw which alignments to sample
locilist = [*range(1,maxloci+1)]

# break this into 20 lists
chunks = [locilist[x:x+chunksize] for x in range(0, len(locilist), chunksize)]

# iterate over the replicates
for count,item in enumerate(chunks):

    # get the outfile name
    outfilename = os.path.join(output_directory, prefix+'_'+str(count+1)+'_alignment.phy')

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

    # close the outfile
    outfile.close()
