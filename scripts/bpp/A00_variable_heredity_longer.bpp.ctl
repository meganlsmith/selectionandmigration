seed =  -1

seqfile = ./bpp_input/subdir/prefix_alignment.phy 
Imapfile = ./bpp_templates/lmapfile.txt 
outfile = ./bpp_output/subdir/prefix_out.txt
mcmcfile = ./bpp_output/subdir/prefix_mcmc.txt

# fixed number of species/populations 
speciesdelimitation = 0

# fixed species tree
speciestree = 0

species&tree = 2  pop1 pop2 
                  20 20 
                 ((pop1, (pop2) Y)X, (X)Y)R; 

# do not phase
phase =   0  0

# use sequence likelihood
usedata = 1

nloci = 10 

# do not remove sites with ambiguity data
cleandata = 0

# gamma(a, b) for theta (estimate theta)
thetaprior = invgamma 3 0.01 

# invgamma(a, b) for root tau & Dirichlet(a) for other tau's
tauprior = invgamma 3 0.01

phiprior = 1 1

locusrate = 1 0 0 2 iid
heredity = 1 4 4

# MCMC samples, locusrate, heredityscalars, Genetrees
print = 1 0 0 0 0 * 
burnin = 20000
sampfreq = 2 
nsample = 500000
