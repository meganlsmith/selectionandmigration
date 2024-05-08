
"""Script to calculate AIC."""
import sys
import os
import pandas as pd
import numpy as np

output_folder = sys.argv[1]
output_prefix = sys.argv[2]
results = sys.argv[3]

# create pandas dataframe
columns = ['AIC_SI', 'AIC_SI2N', 'AIC_IM', 'AIC_IM2N', 'AIC_IM2m','wAIC_SI', 'wAIC_SI2N', 'wAIC_IM', 'wAIC_IM2N', 'wAIC_IM2m', 'best_model']
models = ['SI', 'SI2N', 'IM', 'IM2N', 'IM2m']
results_df = pd.DataFrame(columns=columns)


directories = os.listdir(os.path.join(output_folder))

for directory in directories:

    files = os.listdir(os.path.join(output_folder, directory))[0]

    # get the scores
    AIC_scores = [] #SI SI2N IM IM2N IM2m 
    with open(os.path.join(output_folder, directory,files), 'r') as f:
        for line in f.readlines():
            if 'AIC' in line:
                AIC_scores.append(line.strip().split(':')[1])
    AIC_scores = [float(x) for x in AIC_scores]

    # calculate the weights
    delta_AIC = np.array(AIC_scores) - np.min(AIC_scores)
    AIC_weights = np.exp(-0.5 * delta_AIC) / np.sum(np.exp(-0.5 * delta_AIC))

    # get the best model
    max_index = np.argmax(AIC_weights)
    best_model = models[max_index]

    # populate dataframe
    row_values = AIC_scores + list(AIC_weights) + [best_model]
    results_df.loc[len(results_df)] = row_values

results_df.to_csv(results, index=False)

