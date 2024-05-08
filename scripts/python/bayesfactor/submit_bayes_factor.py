"""This python will submit bayes factor runs given the following information
* path to the ctl file to use
* prefix for  the output file for storing results
"""

import optparse
import os
import sys

def main():
    parser = optparse.OptionParser()

    # Add options for each parameter
    parser.add_option("-c", "--control", dest="control", help="Path to original file.")
    parser.add_option("-o", "--output", dest="output", help="Path to output directory.")
    parser.add_option("-b", "--base", dest="base", help="Path to previous baseline directory.")
    parser.add_option('--force', action='store_true', help='force overwrite if output file exists (default: False)')

    # Parse user input
    (options, args) = parser.parse_args()

    # Check if required options are provided
    if not (options.control and options.output and options.base):
        parser.error("All parameters (alignment, lmap, control, output) are required.")

    # check for output
    if os.path.exists(options.output): 
        if not options.force:
            sys.exit(f"Aborted: {options.output} already exists")
        else:
            print(f"Overwriting existing {options.output}.")
            os.system('rm -r %s' % options.output)
    os.system(f"mkdir -p {options.output}")

    # get alignment file name and lmapfile name from ctl file
    with open(options.control, 'r') as f:
        for line in f.readlines():
            if "seqfile" in line:
                alignment = os.path.join(options.base, line.split(" = ")[1].strip().split("./")[1])
            elif "Imapfile" in line:
                mapfile = os.path.join(options.base, line.split(" = ")[1].strip().split("./")[1])

    # print the alignment and mapping files being used.
    print(f"Running analyses using the alignment file {alignment} and the mapping file {mapfile}.")

    # create new baseline control files
    ctl_original = []
    with open(options.control, 'r') as f:
        for line in f.readlines():
            if 'outfile' in line:
                newline = "outfile = out_model1_g1.txt\n"
            elif 'mcmc' in line:
                newline = "mcmcfile = mcmc_model1_g1.txt\n"
            elif 'seqfile' in line:
                newline = f"seqfile = {alignment}\n"
            elif 'Imapfile' in line:
                newline = f"Imapfile = {mapfile}\n"
            else:
                newline = line
            ctl_original.append(newline)

    with open(os.path.join(options.output, 'model1.ctl'), 'w') as f:
        for item in ctl_original:
            f.write(item)

    ctl_nomig = []
    for item in ctl_original:
        if 'outfile' in item:
            new_item = "outfile = out_model2.txt\n"
        elif 'mcmc' in item:
            new_item = "mcmcfile = mcmc_model2.txt\n"
        elif '((pop1, (pop2) Y)X, (X)Y)R;' in item:
            new_item = '                 (pop1, pop2);'
        else:
            new_item = item
        ctl_nomig.append(new_item)

    with open(os.path.join(options.output, 'model2.ctl'), 'w') as f:
        for item in ctl_nomig:
            f.write(item)

    # change to output dir
    startdir = os.getcwd()
    os.chdir(options.output)
   
    # create directory structure
    os.system("mkdir -p model{1..2}/{1..8}")

    # copy the model fiels
    os.system('cp model1.ctl ./model1/model1.ctl')
    os.system('cp model2.ctl ./model2/model2.ctl')    

    # get the control files
    os.system('for i in {1..2}; do cd model$i; ../../bpp/src/bpp --bfdriver model${i}.ctl --points 8; cd ../; done')
    os.system('for i in {1..2}; do cd model$i; for j in {1..8}; do mv model$i.ctl.$j $j; done; cd ../; done')

    # create slurm scripts
    template = open('../run_bpp_template.sh', 'r')
    lines = template.readlines()
    template.close()

    for model in range(1, 3):
        for gval in range(1, 9):

            # modify ctl
            modified_ctl_lines = []
            with open(os.path.join(f"model{model}",f"{gval}",f"model{model}.ctl.{gval}"), 'r') as f:
                for line in f.readlines():
                    if 'outfile' in line:
                       mod_line = f"outfile = out_model{model}_g{gval}.txt\n"
                    elif 'mcmc' in line:
                       mod_line = f"mcmcfile = mcmc_model{model}_g{gval}.txt\n"
                    else:
                       mod_line = line
                    modified_ctl_lines.append(mod_line)
            with open(os.path.join(f"model{model}",f"{gval}",f"model{model}.ctl.{gval}"), 'w') as f:
                for item in modified_ctl_lines:
                    f.write(item)
            
            new_lines = []
            for line in lines:
                if "#SBATCH -J bpp_model1_g1" in line:
                    new_line = f"#SBATCH -J bpp_model{model}_g{gval}\n"
                elif "#SBATCH -o bpp_model1_g1.out" in line:
                    new_line = f"#SBATCH -o bpp_model{model}_g{gval}.out\n"
                elif "#SBATCH -e bpp_model1_g1.err" in line:
                    new_line = f"#SBATCH -o bpp_model{model}_g{gval}.err\n"
                elif "i=1 # model" in line:
                    new_line = f"i={model} # model\n"
                elif "g=1 # g" in line:
                    new_line = f"g={gval} # g\n"
                else:
                    new_line = line
                new_lines.append(new_line)

            with open(f"run_bpp_model{model}_g{gval}.sh", 'w') as f:
                for item in new_lines:
                    f.write(item)
            
            os.system(f"sbatch run_bpp_model{model}_g{gval}.sh")

    # return to startdir
    os.chdir(startdir)
 
if __name__ == "__main__":
    main()
