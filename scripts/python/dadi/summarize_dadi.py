"""This script will summarize the results of dadi runs in the 'results' folder by creating a csv."""
import os
import pandas as pd

# get result list
all_results = os.listdir('results')
all_results = [x for x in all_results if not 'nomigmodel' in x]

# create empty dataframe
all_results_df = pd.DataFrame(columns=['L', 'nu1', 'nu2', 'T', 'm12', 'm21', 'theta0', 'model', 'genome', 'dfe', 'divtime', 'percent'])
new_column_names = ['L', 'nu1', 'nu2', 'T', 'm12', 'm21', 'theta0']

for i in all_results:

    # get info for columns
    info = i.split('_')

    if info[0] == "nomig":
        subtract = 1
        model = info[0]
    else:
        subtract = 0
        model = info[0]+'_'+info[1]
    genome = info[3-subtract]
    if genome=='scaled':
        genome='simple'
    dfe = info[2-subtract]
    if dfe == 'linkedp1' or dfe == 'linkedancestor' or dfe == 'adaptiveint' or dfe == "balancing":
        percent = info[5-subtract].split('percent')[0]
        #dfe = dfe + '_' + percent
    else:
        percent = 'NA'
    divtime = info[4-subtract]

    # get results
    results = pd.read_csv('results/%s' % i, delimiter = "\t", header=None)
    results.columns = new_column_names
    
    # add variables to dataframe
    results['model'] = model
    results['genome'] = genome
    results['dfe'] = dfe
    results['divtime'] = divtime
    results['percent'] = percent

    # add to growing dataframe
    all_results_df = pd.concat([all_results_df, results], ignore_index = True)

    # remove info
    del results
    del info
    del model
    del subtract
    del genome
    del dfe
    del percent
    del divtime

# save as csv
all_results_df.to_csv('results_summary.csv', index = False)
