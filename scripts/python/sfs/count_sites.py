"""this python script will count the average number of sites in all fsc2 SFS."""

import os
import pandas as pd


# function to get all the files
def get_all_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list


# get list of all sfs
base_SLiM_directory = 'SLiM-testing-redo-revisions/fsc/' 
SLiM_training_SFS = get_all_files(base_SLiM_directory)
base_DROSOPHILA_directory = 'DROSOPHILA-testing-redo-revisions-v2/fsc/'
DROSOPHILA_training_SFS = get_all_files(base_DROSOPHILA_directory)
all_SFS = SLiM_training_SFS + DROSOPHILA_training_SFS

# empty pandas dataframe
columns = ["model", "genome", "dfe","percent", "divtime", "sites"]
df = pd.DataFrame(columns=columns)

#DROSOPHILA-training/fsc/p2_p1_linkedp1_drosophila_5000_5percent/rep_88.fs


# iterate over files
for file_path in all_SFS:

    # get condition info
    info = file_path.split("/")[2]
    if "nomig" in file_path:
        model = info.split("_")[0]
        baseline = 0
    else:
        model = info.split("_")[0] + "_" + info.split("_")[1]
        baseline = 1
    dfe = info.split("_")[1+baseline]
    if "linked" in dfe or "adaptive" in dfe or "balancing" in dfe:
        percent = info.split("_")[4+baseline].split("percent")[0]
    else:
        percent = 'NA'
    divtime = info.split("_")[3+baseline]
    if "DROSOPHILA" in file_path:
        genome = "complex"
    else:
        genome = "simple"

    # get number sites
    data = open(file_path, 'r')
    lines = data.readlines()
    data.close()
    sfs_data = lines[2]
    sfs_data = sfs_data.split()
    sfs_data = [int(x) for x in sfs_data]
    sites = sum(sfs_data)


    # add to dataframe
    row_data = {
        "model": model,
        "genome": genome,
        "dfe": dfe,
        "percent": percent,
        "divtime": divtime,
        "sites": sites
    }

    # Add the row to the DataFrame
    df = df.append(row_data, ignore_index=True)

df.to_csv('site_counts.csv', index=False)
