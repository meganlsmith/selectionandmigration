import os
import pandas

# get list of directories we need to iterate over
slim = os.listdir('SLiM-testing-redo-revisions')
slim = [os.path.join('SLiM-testing-redo-revisions', x) for x in slim]
drosophila = os.listdir('DROSOPHILA-testing-redo-revisions-v2')
drosophila = [os.path.join('DROSOPHILA-testing-redo-revisions-v2', x) for x in drosophila]
all_directories = slim + drosophila

beginning = True

for directory in all_directories:

    print("Processing: ", directory)

    # get time
    if '1250' in directory:
        time = 1250
    elif '5000' in directory:
        time=5000
    elif '20000' in directory:
        time=20000

    # get model info: time, genome, model, DFE, percent
    genome = directory.split('_')[2]
    if 'nomig' in directory:
        model = 'nomig'
    elif 'p1_p2' in directory:
        model = 'p1_p2'
    elif 'p2_p1' in directory:
        model = 'p2_p1'
    dfe = directory.split('_')[1]
    if 'linked' in dfe or 'adaptive' in dfe or 'balancing' in dfe:
        percent = directory.split('_')[-1]
    else:
        percent = 'NA'


    for replicate in range(100):
        
        # get name of .bestlhoods file
        filename = os.path.join(directory, 'rep_%s' % str(replicate), 'Migration_%s' % str(time), 'Migration_%s.bestlhoods' % str(time))
        
        # read file as pandas csv
        temp_file = pandas.read_csv(filepath_or_buffer = filename, sep = '\t')
                
        # add this info to the dataframe
        temp_file['time'] = time
        temp_file['genome'] = genome
        temp_file['model'] = model
        temp_file['dfe'] = dfe
        temp_file['percent'] = percent
        temp_file['replicate'] = replicate

        # add to growing dataframe
        if beginning == True:
            results_df = temp_file
            beginning = False
        else:
            results_df = pandas.concat([results_df, temp_file])

results_df.to_csv(path_or_buf='summary_results.csv')
