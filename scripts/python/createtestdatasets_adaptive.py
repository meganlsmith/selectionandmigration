"""This script will create the following datasets for a given divergence time:
BGS + linked p1 (5%)
BGS + linked p1 (10%)
BGS + linked p1 (15%)
BGS + linked anc (5%)
BGS + linked anc (10%)
BGS + linked anc (15%)
BGS + linked adaptive int (5%)
BGS + linked adaptive int (10%)
BGS + linked adaptive int (15%)
"""

from optparse import OptionParser
import os
import pandas as pd

# get command line input from user using optparse.
parser = OptionParser()
parser.add_option("-i","--inputfolder", help="Folder with SimStats",
                    action="store", type="string", dest="inputfolder")

(options, args) = parser.parse_args()

# print list of datasets
datasets = os.listdir(options.inputfolder)

# start with getting all the adaptive dataframes and the bgs dataframes

# linked p1 
linkedp1_nomig = pd.read_csv(options.inputfolder + '/' + 'nomig_linkedp1.msOut', sep = '\t', na_filter = False)
linkedp1_p1_p2 = pd.read_csv(options.inputfolder + '/' + 'p1_p2_linkedp1.msOut', sep = '\t', na_filter = False)
linkedp1_p2_p1 = pd.read_csv(options.inputfolder + '/' + 'p2_p1_linkedp1.msOut', sep = '\t', na_filter = False)

# linked ancestor
linkedanc_nomig = pd.read_csv(options.inputfolder + '/' + 'nomig_linkedancestor.msOut', sep = '\t', na_filter = False)
linkedanc_p1_p2 = pd.read_csv(options.inputfolder + '/' + 'p1_p2_linkedancestor.msOut', sep = '\t', na_filter = False)
linkedanc_p2_p1 = pd.read_csv(options.inputfolder + '/' + 'p2_p1_linkedancestor.msOut', sep = '\t', na_filter = False)

# adaptive introgression
adaptiveint_p1_p2 = pd.read_csv(options.inputfolder + '/' + 'p1_p2_adaptiveint.msOut', sep = '\t', na_filter = False)

# BGS
bgs_nomig = pd.read_csv(options.inputfolder + '/' + 'nomig_bgs.msOut', sep = '\t')
bgs_p1_p2 = pd.read_csv(options.inputfolder + '/' + 'p1_p2_bgs.msOut', sep = '\t')
bgs_p2_p1 = pd.read_csv(options.inputfolder + '/' + 'p2_p1_bgs.msOut', sep = '\t')

# get subsampled datasets for 5 and 10 percent from adaptive data

# linked p1
linkedp1_nomig_5 = linkedp1_nomig.sample(n=500, replace=False)
linkedp1_p1_p2_5 = linkedp1_p1_p2.sample(n=500, replace=False)
print(linkedp1_p1_p2_5)
linkedp1_p2_p1_5 = linkedp1_p2_p1.sample(n=500, replace=False)
linkedp1_nomig_10 = linkedp1_nomig.sample(n=1000, replace=False)
linkedp1_p1_p2_10 = linkedp1_p1_p2.sample(n=1000, replace=False)
linkedp1_p2_p1_10 = linkedp1_p2_p1.sample(n=1000, replace=False)

# linked ancestor
linkedanc_nomig_5 = linkedanc_nomig.sample(n=500, replace=False)
linkedanc_p1_p2_5 = linkedanc_p1_p2.sample(n=500, replace=False)
linkedanc_p2_p1_5 = linkedanc_p2_p1.sample(n=500, replace=False)
linkedanc_nomig_10 = linkedanc_nomig.sample(n=1000, replace=False)
linkedanc_p1_p2_10 = linkedanc_p1_p2.sample(n=1000, replace=False)
linkedanc_p2_p1_10 = linkedanc_p2_p1.sample(n=1000, replace=False)
 
# adaptive introgression
adaptiveint_p1_p2_5 = adaptiveint_p1_p2.sample(n=500, replace=False)
adaptiveint_p1_p2_10 = adaptiveint_p1_p2.sample(n=1000, replace=False)

# sample BGS data for 5, 10, 15 percent datasets
bgs_nomig_5 = bgs_nomig.sample(n=9500, replace=False)
bgs_p1_p2_5 = bgs_p1_p2.sample(n=9500, replace=False)
bgs_p2_p1_5 = bgs_p2_p1.sample(n=9500, replace=False)
bgs_nomig_10 = bgs_nomig.sample(n=9000, replace=False)
bgs_p1_p2_10 = bgs_p1_p2.sample(n=9000, replace=False)
bgs_p2_p1_10 = bgs_p2_p1.sample(n=9000, replace=False)
bgs_nomig_15 = bgs_nomig.sample(n=8500, replace=False)
bgs_p1_p2_15 = bgs_p1_p2.sample(n=8500, replace=False)
bgs_p2_p1_15 = bgs_p2_p1.sample(n=8500, replace=False)

#make combined datasets

# bgs + linked p1
bgs_linkedp1_5_nomig = linkedp1_nomig_5.append(bgs_nomig_5)
bgs_linkedp1_5_p1_p2 = linkedp1_p1_p2_5.append(bgs_p1_p2_5)
print(bgs_linkedp1_5_p1_p2)
bgs_linkedp1_5_p2_p1 = linkedp1_p2_p1_5.append(bgs_p2_p1_5)
bgs_linkedp1_10_nomig = linkedp1_nomig_10.append(bgs_nomig_10)
bgs_linkedp1_10_p1_p2 = linkedp1_p1_p2_10.append(bgs_p1_p2_10)
bgs_linkedp1_10_p2_p1 = linkedp1_p2_p1_10.append(bgs_p2_p1_10)
bgs_linkedp1_15_nomig = linkedp1_nomig.append(bgs_nomig_15)
bgs_linkedp1_15_p1_p2 = linkedp1_p1_p2.append(bgs_p1_p2_15)
bgs_linkedp1_15_p2_p1 = linkedp1_p2_p1.append(bgs_p2_p1_15)

# bgs + linked ancestor 
bgs_linkedanc_5_nomig = linkedanc_nomig_5.append(bgs_nomig_5)
bgs_linkedanc_5_p1_p2 = linkedanc_p1_p2_5.append(bgs_p1_p2_5)
bgs_linkedanc_5_p2_p1 = linkedanc_p2_p1_5.append(bgs_p2_p1_5)
bgs_linkedanc_10_nomig = linkedanc_nomig_10.append(bgs_nomig_10)
bgs_linkedanc_10_p1_p2 = linkedanc_p1_p2_10.append(bgs_p1_p2_10)
bgs_linkedanc_10_p2_p1 = linkedanc_p2_p1_10.append(bgs_p2_p1_10)
bgs_linkedanc_15_nomig = linkedanc_nomig.append(bgs_nomig_15)
bgs_linkedanc_15_p1_p2 = linkedanc_p1_p2.append(bgs_p1_p2_15)
bgs_linkedanc_15_p2_p1 = linkedanc_p2_p1.append(bgs_p2_p1_15)

# bgs + adaptiveint 
bgs_adaptiveint_5_p1_p2 = adaptiveint_p1_p2_5.append(bgs_p1_p2_5)
bgs_adaptiveint_10_p1_p2 = adaptiveint_p1_p2_10.append(bgs_p1_p2_10)
bgs_adaptiveint_15_p1_p2 = adaptiveint_p1_p2.append(bgs_p1_p2_15)


# write csvs

bgs_linkedp1_5_nomig.to_csv(path_or_buf=options.inputfolder + 'nomig_linkedp1_bgs_5percent.msOut', sep='\t', na_rep='nan', index=False)
bgs_linkedp1_5_p1_p2.to_csv(path_or_buf=options.inputfolder + 'p1_p2_linkedp1_bgs_5percent.msOut', sep='\t', na_rep='nan', index=False) 
bgs_linkedp1_5_p2_p1.to_csv(path_or_buf=options.inputfolder + 'p2_p1_linkedp1_bgs_5percent.msOut', sep='\t', na_rep='nan', index=False) 
bgs_linkedp1_10_nomig.to_csv(path_or_buf=options.inputfolder + 'nomig_linkedp1_bgs_10percent.msOut', sep='\t', na_rep='nan', index=False)
bgs_linkedp1_10_p1_p2.to_csv(path_or_buf=options.inputfolder + 'p1_p2_linkedp1_bgs_10percent.msOut', sep='\t', na_rep='nan', index=False)
bgs_linkedp1_10_p2_p1.to_csv(path_or_buf=options.inputfolder + 'p2_p1_linkedp1_bgs_10percent.msOut', sep='\t', na_rep='nan', index=False)
bgs_linkedp1_15_nomig.to_csv(path_or_buf=options.inputfolder + 'nomig_linkedp1_bgs_15percent.msOut', sep='\t', na_rep='nan', index=False)
bgs_linkedp1_15_p1_p2.to_csv(path_or_buf=options.inputfolder + 'p1_p2_linkedp1_bgs_15percent.msOut', sep='\t', na_rep='nan', index=False)
bgs_linkedp1_15_p2_p1.to_csv(path_or_buf=options.inputfolder + 'p2_p1_linkedp1_bgs_15percent.msOut', sep='\t', na_rep='nan', index=False)

bgs_linkedanc_5_nomig.to_csv(path_or_buf=options.inputfolder + 'nomig_linkedancestor_bgs_5percent.msOut', sep='\t', na_rep='nan', index=False)
bgs_linkedanc_5_p1_p2.to_csv(path_or_buf=options.inputfolder + 'p1_p2_linkedancestor_bgs_5percent.msOut', sep='\t', na_rep='nan', index=False)
bgs_linkedanc_5_p2_p1.to_csv(path_or_buf=options.inputfolder + 'p2_p1_linkedancestor_bgs_5percent.msOut', sep='\t', na_rep='nan', index=False)
bgs_linkedanc_10_nomig.to_csv(path_or_buf=options.inputfolder + 'nomig_linkedancestor_bgs_10percent.msOut', sep='\t', na_rep='nan', index=False)
bgs_linkedanc_10_p1_p2.to_csv(path_or_buf=options.inputfolder + 'p1_p2_linkedancestor_bgs_10percent.msOut', sep='\t', na_rep='nan', index=False)
bgs_linkedanc_10_p2_p1.to_csv(path_or_buf=options.inputfolder + 'p2_p1_linkedancestor_bgs_10percent.msOut', sep='\t', na_rep='nan', index=False)
bgs_linkedanc_15_nomig.to_csv(path_or_buf=options.inputfolder + 'nomig_linkedancestor_bgs_15percent.msOut', sep='\t', na_rep='nan', index=False)
bgs_linkedanc_15_p1_p2.to_csv(path_or_buf=options.inputfolder + 'p1_p2_linkedancestor_bgs_15percent.msOut', sep='\t', na_rep='nan', index=False)
bgs_linkedanc_15_p2_p1.to_csv(path_or_buf=options.inputfolder + 'p2_p1_linkedancestor_bgs_15percent.msOut', sep='\t', na_rep='nan', index=False)

bgs_adaptiveint_5_p1_p2.to_csv(path_or_buf=options.inputfolder + 'p1_p2_adaptiveint_bgs_5percent.msOut', sep='\t', na_rep='nan', index=False)
bgs_adaptiveint_10_p1_p2.to_csv(path_or_buf=options.inputfolder + 'p1_p2_adaptiveint_bgs_10percent.msOut', sep='\t', na_rep='nan', index=False)
bgs_adaptiveint_15_p1_p2.to_csv(path_or_buf=options.inputfolder + 'p1_p2_adaptiveint_bgs_15percent.msOut', sep='\t', na_rep='nan', index=False)







