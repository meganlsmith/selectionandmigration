""" read results and create a table."""
import os
import re
import pandas as pd

df = pd.DataFrame(columns=['model', 'condition', 'genome', 'divtime', 'replicate', 'bf'])

available_results = next(os.walk('.'))[1]
available_results = [x for x in available_results if not re.search(r'_(6|7|8|9|10)$', x)]
available_results = [x for x in available_results if not 'bpp' in x and not 'python_scripts' in x]
for item in available_results:

    # get metadata
    model = item.split('_')[0]
    if model == 'p1':
        model = 'p1_p2'
        ix = 2
    else:
        ix = 1
    condition = item.split('_')[ix]
    genome = item.split('_')[ix+1]
    divtime = item.split('_')[ix+2]
    replicate = item.split('_')[ix+3]
    if genome == "DROSOPHILA":
       genome = "complex"
    elif genome == "SLiM":
       genome = "uniform"

    # get results
    with open(os.path.join(item,'bf_calculations.txt'),'r') as f:
        for line in f.readlines():
             bf = line.split()[-1]

    data_to_add = {'model': model, 'condition': condition, 'genome': genome, 'divtime': divtime, 'replicate': replicate, 'bf': bf}
    df = df.append(data_to_add, ignore_index = True)

df.to_csv('all_results.csv')
