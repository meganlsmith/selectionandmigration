"""This will make a table with information for each analysis from the out_ files."""

import os
import pandas as pd

# get a list of the output files in the two output directories
DROSOPHILA_files = os.listdir('bpp_output/DROSOPHILA-testing-redo')
DROSOPHILA_files = [x for x in DROSOPHILA_files if x.startswith('out_')]
DROSOPHILA_files = [os.path.join('bpp_output/DROSOPHILA-testing-redo', x) for x in DROSOPHILA_files]
SLiM_files = os.listdir('bpp_output/SLiM-testing-redo')
SLiM_files = [x for x in SLiM_files if x.startswith('out_')]
SLiM_files = [os.path.join('bpp_output/SLiM-testing-redo', x) for x in SLiM_files]
all_files = DROSOPHILA_files + SLiM_files

# create dataframe for storing results
column_names = ["tau_3R_mean", "tau_4X_mean", "tau_5Y_mean", "phi_X_mean", "phi_Y_mean", "lnL_mean",
    "tau_3R_median", "tau_4X_median", "tau_5Y_median", "phi_X_median", "phi_Y_median", "lnL_median",
    "tau_3R_sd", "tau_4X_sd", "tau_5Y_sd", "phi_X_sd", "phi_Y_sd", "lnL_sd",
    "tau_3R_min", "tau_4X_min", "tau_5Y_min", "phi_X_min", "phi_Y_min", "lnL_min",
    "tau_3R_max", "tau_4X_max", "tau_5Y_max", "phi_X_max", "phi_Y_max", "lnL_max",
    "tau_3R_percent25", "tau_4X_percent25", "tau_5Y_percent25", "phi_X_percent25", "phi_Y_percent25", "lnL_percent25",
    "tau_3R_percent975", "tau_4X_percent975", "tau_5Y_percent975", "phi_X_percent975", "phi_Y_percent975", "lnL_percent975",
    "tau_3R_hpd25", "tau_4X_hpd25", "tau_5Y_hpd25", "phi_X_hpd25", "phi_Y_hpd25", "lnL_hpd25",
    "tau_3R_hpd975", "tau_4X_hpd975", "tau_5Y_hpd975", "phi_X_hpd975", "phi_Y_hpd975", "lnL_hpd975",
    "tau_3R_ess", "tau_4X_ess", "tau_5Y_ess", "phi_X_ess", "phi_Y_ess", "lnL_ess",
    "tau_3R_eff", "tau_4X_eff", "tau_5Y_eff", "phi_X_eff", "phi_Y_eff", "lnL_eff",
    "genome", "model", "dfe", "divtime", "percent", "rep"]

results = pd.DataFrame(columns = column_names)

# iterate over files
count = 0
for file in all_files:

    # determine when to start reading lines into a table
    record = False

    # list of lines with relevant information
    relevant_lines = []

    # iterate over lines to find the parts that we need to put in a table
    with open(file, 'r') as f:

        for line in f.readlines():

            if record == False:
                if 'spent in MCMC' in line:
                    record = True # then we need to start recording
            else:

                # determine when to stop recording
                if 'List of nodes, taus and thetas' in line:
                    record = False

                # otherwise, record
                else:
                    relevant_lines.append(line)

    # remove the first line, which is just blank
    relevant_lines = relevant_lines[1:]
    
    # get the values
    try:
        mean_label, tau_3R_mean, tau_4X_mean, tau_5Y_mean, phi_X_mean, phi_Y_mean, lnL_mean = relevant_lines[1].split()
    except:
        continue
    median_label, tau_3R_median, tau_4X_median, tau_5Y_median, phi_X_median, phi_Y_median, lnL_median = relevant_lines[2].split()
    sd_label, tau_3R_sd, tau_4X_sd, tau_5Y_sd, phi_X_sd, phi_Y_sd, lnL_sd = relevant_lines[3].split()
    min_label, tau_3R_min, tau_4X_min, tau_5Y_min, phi_X_min, phi_Y_min, lnL_min = relevant_lines[4].split()
    max_label, tau_3R_max, tau_4X_max, tau_5Y_max, phi_X_max, phi_Y_max, lnL_max = relevant_lines[5].split()
    percent25_label, tau_3R_percent25, tau_4X_percent25, tau_5Y_percent25, phi_X_percent25, phi_Y_percent25, lnL_percent25 = relevant_lines[6].split()
    percent975_label, tau_3R_percent975, tau_4X_percent975, tau_5Y_percent975, phi_X_percent975, phi_Y_percent975, lnL_percent975 = relevant_lines[7].split()
    hpd25_label, tau_3R_hpd25, tau_4X_hpd25, tau_5Y_hpd25, phi_X_hpd25, phi_Y_hpd25, lnL_hpd25 = relevant_lines[8].split()
    hpd975_label, tau_3R_hpd975, tau_4X_hpd975, tau_5Y_hpd975, phi_X_hpd975, phi_Y_hpd975, lnL_hpd975 = relevant_lines[9].split()
    ess_label, tau_3R_ess, tau_4X_ess, tau_5Y_ess, phi_X_ess, phi_Y_ess, lnL_ess = relevant_lines[10].split()
    eff_label, tau_3R_eff, tau_4X_eff, tau_5Y_eff, phi_X_eff, phi_Y_eff, lnL_eff = relevant_lines[11].split()


    # get some information about this run
    genome = file.split("/")[1]
    modelbase = file.split("/")[-1].split("_")

    if genome == "SLiM-testing-redo":
        if modelbase[1] == 'nomig':
            model = modelbase[1]
            dfe = modelbase[2]
            divtime = modelbase[3]
            if dfe == 'linkedp1' or dfe == 'linkedancestor' or dfe == 'adaptiveint':
                percent = modelbase[4]
                rep = modelbase[5]
                divtime = modelbase[3]
            else:
                percent = "NA"
                rep = modelbase[5]
                divtime = modelbase[4]
            
        else:
            model = modelbase[1] + '_' + modelbase[2]
            dfe = modelbase[3]
            divtime = modelbase[4]
            if dfe == 'linkedp1' or dfe == 'linkedancestor' or dfe == 'adaptiveint':
                percent = modelbase[5]
                divtime = modelbase[4]
                rep = modelbase[6]
            else:
                percent = "NA"
                rep = modelbase[6]
                divtime = modelbase[5]

    elif genome == "DROSOPHILA-testing-redo":
        if modelbase[1] == 'nomig':
            model = modelbase[1]
            dfe = modelbase[2]
            divtime = modelbase[3]
            if dfe == 'linkedp1' or dfe == 'linkedancestor' or dfe == 'adaptiveint':
                divtime = modelbase[3]
                percent = modelbase[4]
                rep = modelbase[5]
            else:
                percent = "NA"
                rep = modelbase[5]
                divtime = modelbase[4]           
        else:
            model = modelbase[1] + '_' + modelbase[2]
            dfe = modelbase[3]
            if dfe == 'linkedp1' or dfe == 'linkedancestor' or dfe == 'adaptiveint':
                percent = modelbase[5]
                rep = modelbase[6]
                divtime = modelbase[4]
            else:
                divtime = modelbase[5]
                percent = "NA"
                rep = modelbase[6]

    rep = rep.split(".txt")[0]

 
    results.loc[count] = [tau_3R_mean, tau_4X_mean, tau_5Y_mean, phi_X_mean, phi_Y_mean, lnL_mean,
        tau_3R_median, tau_4X_median, tau_5Y_median, phi_X_median, phi_Y_median, lnL_median,
        tau_3R_sd, tau_4X_sd, tau_5Y_sd, phi_X_sd, phi_Y_sd, lnL_sd,
        tau_3R_min, tau_4X_min, tau_5Y_min, phi_X_min, phi_Y_min, lnL_min,
        tau_3R_max, tau_4X_max, tau_5Y_max, phi_X_max, phi_Y_max, lnL_max,
        tau_3R_percent25, tau_4X_percent25, tau_5Y_percent25, phi_X_percent25, phi_Y_percent25, lnL_percent25,
        tau_3R_percent975, tau_4X_percent975, tau_5Y_percent975, phi_X_percent975, phi_Y_percent975, lnL_percent975,
        tau_3R_hpd25, tau_4X_hpd25, tau_5Y_hpd25, phi_X_hpd25, phi_Y_hpd25, lnL_hpd25,
        tau_3R_hpd975, tau_4X_hpd975, tau_5Y_hpd975, phi_X_hpd975, phi_Y_hpd975, lnL_hpd975,
        tau_3R_ess, tau_4X_ess, tau_5Y_ess, phi_X_ess, phi_Y_ess, lnL_ess,
        tau_3R_eff, tau_4X_eff, tau_5Y_eff, phi_X_eff, phi_Y_eff, lnL_eff,
        genome, model, dfe, divtime, percent, rep] 
    count+=1

# write to csv
results.to_csv('all_results.csv', index=False)

