import sys
import os
import tskit
import pandas as pd

input_directory = sys.argv[1]
output_file = sys.argv[2]
dfs = []

# list files
input_files = os.listdir(input_directory)
input_files = [x for x in input_files if x.endswith('_overlaid.trees')]

for file in input_files:
    ts = tskit.load(os.path.join(input_directory, file))
    sets = [ts.samples(), ts.samples(0), ts.samples(1)]
    pair = [ts.samples(0), ts.samples(1)]
    dxy = ts.divergence(pair)
    fst = ts.Fst(pair)
    pi1 = ts.diversity(sets[1])
    pi2 = ts.diversity(sets[2])
    data = {'file': file, 'pi1': pi1, 'pi2': pi2, 'dxy': dxy, 'fst': fst}

    dfs.append(pd.DataFrame(data, index=[0]))

result_df = pd.concat(dfs, ignore_index=True)

result_df.to_csv(output_file)
