"""this python script will compare models using a likelihood ratio test and return a table with a row for each dataset 
with information on the generating model for the dataset, the parameter estimates under both models, the likelihood under both models,
and the likelihood ratio test results."""

import os
import pandas as pd
import numpy as np
import scipy.stats as stats

# get a list of all results files
results = os.listdir('results')

# temporarily remove linked and adaptiveint results
#results = [x for x in results if 'linked' not in x]
#results = [x for x in results if 'adaptive' not in x]

# keep only the nomig results
results = [x for x in results if 'nomig' in x]
results_nomigmodel = [x for x in results if 'nomigmodel' in x]
results_migmodel = [x for x in results if x not in results_nomigmodel]

# create empty pandas dataframe for storing resultsi
columns = ['genome', 'model', 'dfe', 'percent', 'T', 'lhood_mig', 'nu1_mig', 'nu2_mig', 'tau_mig', 'm12_mig', 'm21_mig', 'theta0_mig', 'lhood_nomig', 'nu1_nomig', 'nu2_nomig', 'tau_nomig', 'theta0_nomig', 'LRT_stat', 'p_value']
output = pd.DataFrame(columns=columns)

# iterate over files and get information
for filename in results_migmodel:

    # get filename
    mig_file = os.path.join('results', filename)
    nomig_filename = filename.split('fits')[0] + 'nomigmodel_fits.txt'
    nomig_file = os.path.join('results', nomig_filename)

    # get basic info
    model = 'nomig'
    dfe = filename.split('_')[1]
    genome = filename.split('_')[2]
    T = filename.split('_')[3]
    if 'percent' in filename:
        percent = filename.split('_')[4].strip('percent')
    else:
        percent = np.nan

    # get info for migmodel
    mig_data = pd.read_csv(mig_file, header=None, sep="\t")
    mig_colnames = ['lhood_mig', 'nu1_mig', 'nu2_mig', 'tau_mig', 'm12_mig', 'm21_mig', 'theta0_mig']
    mig_data.columns = mig_colnames

    # get info for nomigmodel 
    nomig_data = pd.read_csv(nomig_file, header=None, sep="\t")
    nomig_colnames = ['lhood_nomig', 'nu1_nomig', 'nu2_nomig', 'tau_nomig', 'theta0_nomig']
    nomig_data.columns = nomig_colnames

    # combine dataframes
    all_data = pd.concat([mig_data, nomig_data], axis=1)

    # add basic info
    all_data['genome'] = genome
    all_data['model'] = model
    all_data['dfe'] = dfe
    all_data['T'] = T
    all_data['percent'] = percent

    # conduct LRT
    all_data['LRT_stat'] = 2 * (all_data['lhood_mig'] - all_data['lhood_nomig'])
    all_data['p_value'] = 1 - stats.chi2.cdf(all_data['LRT_stat'], 2)

    # combine with reulsts
    output = pd.concat([output, all_data], ignore_index = True)

# save results
output.to_csv('dadi_LRT_results.csv')
