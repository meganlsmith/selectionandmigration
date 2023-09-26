# NLopt is the optimization libary dadi uses
import nlopt
import dadi
import argparse
import os

def read_data(dataset):

    """Read the Site Frequency Spectrum."""

    # read sfs
    data_fs = dadi.Spectrum.from_file(dataset)

    # get sample sizes
    ns = data_fs.sample_sizes
    
    return(data_fs, ns)

def split_mig(params, ns, pts):
    nu1, nu2, T = params
    xx = dadi.Numerics.default_grid(pts)

    phi = dadi.PhiManip.phi_1D(xx)
    phi = dadi.PhiManip.phi_1D_to_2D(xx, phi)
    phi = dadi.Integration.two_pops(phi, xx, T, nu1, nu2, m12 = 0, m21 = 0)

    fs = dadi.Spectrum.from_phi(phi, ns, (xx, xx))
    return fs

def define_model(ns):

    """Set up the model for inference."""

    # Define the grid points based on the sample size.
    # For smaller data (largest sample size is about <100) [ns+20, ns+30, ns+40] is a good starting point.
    # For larger data (largest sample size is about >=100) or for heavily down projected data [ns+100, ns+110, ns+120] is a good starting point.
    pts_l = [max(ns)+20, max(ns)+30, max(ns)+40]
    pts_l = [max(ns)+150, max(ns)+160, max(ns)+170]

    
    model = split_mig

    # Wrap the demographic model in a function that utilizes grid points which increases dadi's ability to more accurately generate a model frequency spectrum.
    model = dadi.Numerics.make_extrap_func(model)

    return(model, pts_l)

def fit_model(data_fs, model, pts_l):
    # Define starting parameters
    params = [0.1, 0.1, 0.5] 

    # Define boundaries of optimization.
    # It is a good idea to have boundaries to avoid optimization
    # from trying parameter sets that are time consuming without
    # nessicarily being correct.
    # If optimization infers parameters very close to the boundaries, we should increase them.
    lower_bounds = [1e-2, 1e-2, 0.04]
    upper_bounds = [5, 5, 16]

    
    # Perturb parameters
    # Optimizers dadi uses are mostly deterministic
    # so we will want to randomize parameters for each optimization.
    # It is recommended to optimize at least 20 time if we only have
    # our local machin, 100 times if we have access to an HPC.
    # If we want a single script to do multiple runs, we will want to
    # start a for loop here
    p0 = dadi.Misc.perturb_params(params, fold=1, upper_bound=upper_bounds,
                                  lower_bound=lower_bounds)
    
    # Run optimization
    # At the end of the optimization we will get the
    # optimal parameters and log-likelihood.
    # We can modify verbose to watch how the optimizer behaves,
    # what number we pass it how many evaluations are done
    # before the evaluation is printed.
    
    popt, ll_model = dadi.Inference.opt(p0, data_fs, model, pts_l,
                                        lower_bound=lower_bounds,
                                        upper_bound=upper_bounds,
                                        algorithm=nlopt.LN_BOBYQA,
                                        maxeval=400, verbose=100)
    
    return(popt, ll_model)

def calc_theta(popt, ns, pts_l, model, data_fs):
    # Calculate the synonymous theta
    model_fs = model(popt, ns, pts_l)
    theta0 = dadi.Inference.optimal_sfs_scaling(model_fs, data_fs)
    return(theta0)

def write_results(namedata, ll_model, popt, theta0):
    # Write results to fid
    fid = open('results/'+namedata+'_fits.txt','a')
    res = [ll_model] + list(popt) + [theta0]
    fid.write('\t'.join([str(ele) for ele in res])+'\n')
    fid.close()


if __name__ == "__main__":

    # Parse arguments
    parser = argparse.ArgumentParser(description='Process input and output folders')
    parser.add_argument('--input', dest="input", type=str,
                        help='an input folder with sfs files.')
    parser.add_argument('--output', dest="output", type=str,
                        help='an output folder.')
    parser.add_argument('--prefix', dest="prefix", type=str,
                        help='Prefix for naming output.')
    args = parser.parse_args()

    # for each replicate, run analysis
    list_sfs = os.listdir(args.input)
    list_sfs = [x for x in list_sfs if x.endswith('.fs')]
    
    for i in range(len(list_sfs)):
    
        # read the sfs
        data_fs, ns = read_data(os.path.join(args.input, list_sfs[i]))
        
        # define the model
        model, pts_l = define_model(ns)
        
        # fit the model
        popt, ll_model = fit_model(data_fs, model, pts_l)
        print(popt, ll_model)
        
        # calculate theta
        theta0 = calc_theta(popt, ns, pts_l, model, data_fs)
        
        # write results
        write_results(args.prefix, ll_model, popt, theta0)
