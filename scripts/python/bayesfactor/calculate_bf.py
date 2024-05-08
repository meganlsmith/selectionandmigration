"""this python script will calculate BF."""
import optparse
import os
import sys
import pandas as pd
import numpy as np

def main():
    parser = optparse.OptionParser()

    # Add options for each parameter
    parser.add_option("-i", "--input", dest="input", help="Path to results for processing.")

    # Parse user input
    (options, args) = parser.parse_args()

    # Check if required options are provided
    if not (options.input):
        parser.error("Please provide a path to the results to process..")

    # get the beta weights information
    marginal_likelihoods = []

    for model in ['model1','model2']:

        lnf_values = []

        for rep in range(1,9):

            # get the elnf value
            with open(os.path.join(options.input,model,str(rep),f"out_{model}_g{rep}.txt"),'r') as f:

                for line in f.readlines():

                    if "BFbeta" in line:

                        lnf = float(line.split()[-1])
                        lnf_values.append(lnf)

        # add to betaweights
        betaweights = pd.read_csv(os.path.join(options.input,model,'betaweights.csv'))
        betaweights['ElnfX'] = lnf_values

        # calculate marginal likelihoods
        betaweights['product'] = betaweights['weight']*betaweights['ElnfX']
        total_product = np.sum(betaweights['product'])
        marginal_likelihood = total_product / 2
        marginal_likelihoods.append(marginal_likelihood)

    # calculate bf
    bf12 = marginal_likelihoods[0] - marginal_likelihoods[1]
    bf21 = marginal_likelihoods[1] - marginal_likelihoods[0]

    with open(os.path.join(options.input,'bf_calculations.txt'),'w') as f:
        f.write(f"Bayes Factor 1 2 (evidence against Model 2--simple) is {bf12}\n")
        f.write(f"Bayes Factor 2 1 (evidence against Model 1--complex) is {bf21}\n")


if __name__ == "__main__":
    main()


