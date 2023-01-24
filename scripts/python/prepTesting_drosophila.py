
import sys, os

def readAndLabelStats(statFileName, label, numSites):
    examples = []
    with open(statFileName) as statFile:
        first = True
        chromStart = 10000
        for line in statFile:
            if first:
                header = "chrom\tchromStart\tchromEnd\tnumSites\t"+line
                first = False
            else:
                examples.append(str(label)+"\t"+str(chromStart)+"\t"+str(chromStart+10000)+"\t"+str(numSites)+"\t"+line)
                chromStart = chromStart + 10000
    return header, examples


statDir, trainingSetFileName = sys.argv[1:]
headerH = {}
print(trainingSetFileName)
# first, prep bgs datasets
header, nomigbgsTrainingSet = readAndLabelStats("%s/nomig_bgs.msOut" %(statDir), 1, 10000)
header, p1p2bgsTrainingSet = readAndLabelStats("%s/p1_p2_bgs.msOut" %(statDir), 2, 10000)
header, p2p1bgsTrainingSet = readAndLabelStats("%s/p2_p1_bgs.msOut" %(statDir), 3, 10000)
with open(trainingSetFileName+'bgs.fvec', "w") as outFile:
    outFile.write(header)
    for line in nomigbgsTrainingSet:
        outFile.write(line)
    for line in p1p2bgsTrainingSet:
        outFile.write(line)
    for line in p2p1bgsTrainingSet:
        outFile.write(line)


# next, prep neutral dataset
header, nomigneutralTrainingSet = readAndLabelStats("%s/nomig_neutral.msOut" %(statDir), 1, 10000)
header, p1p2neutralTrainingSet = readAndLabelStats("%s/p1_p2_neutral.msOut" %(statDir), 2, 10000)
header, p2p1neutralTrainingSet = readAndLabelStats("%s/p2_p1_neutral.msOut" %(statDir), 3, 10000)
with open(trainingSetFileName+'neutral.fvec', "w") as outFile:
    outFile.write(header)
    for line in nomigneutralTrainingSet:
        outFile.write(line)
    for line in p1p2neutralTrainingSet:
        outFile.write(line)
    for line in p2p1neutralTrainingSet:
        outFile.write(line)

# next, prep linked p1 5% dataset
header, nomiglinkedp1_5percent_TrainingSet = readAndLabelStats("%s/nomig_linkedp1_bgs_5percent.msOut" %(statDir), 1, 10000)
header, p1p2linkedp1_5percent_TrainingSet = readAndLabelStats("%s/p1_p2_linkedp1_bgs_5percent.msOut" %(statDir), 2, 10000)
header, p2p1linkedp1_5percent_TrainingSet = readAndLabelStats("%s/p2_p1_linkedp1_bgs_5percent.msOut" %(statDir), 3, 10000)
print(statDir+'nomig_linkedp1_bgs_5percent.msOut')
with open(trainingSetFileName+'linkedp1_5percent.fvec', "w") as outFile:
    outFile.write(header)
    for line in nomiglinkedp1_5percent_TrainingSet:
        outFile.write(line)
    for line in p1p2linkedp1_5percent_TrainingSet:
        outFile.write(line)
    for line in p2p1linkedp1_5percent_TrainingSet:
        outFile.write(line)

# next, prep linked p1 10% dataset
header, nomiglinkedp1_10percent_TrainingSet = readAndLabelStats("%s/nomig_linkedp1_bgs_10percent.msOut" %(statDir), 1, 10000)
header, p1p2linkedp1_10percent_TrainingSet = readAndLabelStats("%s/p1_p2_linkedp1_bgs_10percent.msOut" %(statDir), 2, 10000)
header, p2p1linkedp1_10percent_TrainingSet = readAndLabelStats("%s/p2_p1_linkedp1_bgs_10percent.msOut" %(statDir), 3, 10000)
with open(trainingSetFileName+'linkedp1_10percent.fvec', "w") as outFile:
    outFile.write(header)
    for line in nomiglinkedp1_10percent_TrainingSet:
        outFile.write(line)
    for line in p1p2linkedp1_10percent_TrainingSet:
        outFile.write(line)
    for line in p2p1linkedp1_10percent_TrainingSet:
        outFile.write(line)

# next, prep linked p1 5% dataset
header, nomiglinkedp1_15percent_TrainingSet = readAndLabelStats("%s/nomig_linkedp1_bgs_15percent.msOut" %(statDir), 1, 10000)
header, p1p2linkedp1_15percent_TrainingSet = readAndLabelStats("%s/p1_p2_linkedp1_bgs_15percent.msOut" %(statDir), 2, 10000)
header, p2p1linkedp1_15percent_TrainingSet = readAndLabelStats("%s/p2_p1_linkedp1_bgs_15percent.msOut" %(statDir), 3, 10000)
with open(trainingSetFileName+'linkedp1_15percent.fvec', "w") as outFile:
    outFile.write(header)
    for line in nomiglinkedp1_15percent_TrainingSet:
        outFile.write(line)
    for line in p1p2linkedp1_15percent_TrainingSet:
        outFile.write(line)
    for line in p2p1linkedp1_15percent_TrainingSet:
        outFile.write(line)

# next, prep linked anc 5% dataset
header, nomiglinkedancestor_5percent_TrainingSet = readAndLabelStats("%s/nomig_linkedancestor_bgs_5percent.msOut" %(statDir), 1, 10000)
header, p1p2linkedancestor_5percent_TrainingSet = readAndLabelStats("%s/p1_p2_linkedancestor_bgs_5percent.msOut" %(statDir), 2, 10000)
header, p2p1linkedancestor_5percent_TrainingSet = readAndLabelStats("%s/p2_p1_linkedancestor_bgs_5percent.msOut" %(statDir), 3, 10000)
with open(trainingSetFileName+'linkedancestor_5percent.fvec', "w") as outFile:
    outFile.write(header)
    for line in nomiglinkedancestor_5percent_TrainingSet:
        outFile.write(line)
    for line in p1p2linkedancestor_5percent_TrainingSet:
        outFile.write(line)
    for line in p2p1linkedancestor_5percent_TrainingSet:
        outFile.write(line)

# next, prep linked ancestor 10% dataset
header, nomiglinkedancestor_10percent_TrainingSet = readAndLabelStats("%s/nomig_linkedancestor_bgs_10percent.msOut" %(statDir), 1, 10000)
header, p1p2linkedancestor_10percent_TrainingSet = readAndLabelStats("%s/p1_p2_linkedancestor_bgs_10percent.msOut" %(statDir), 2, 10000)
header, p2p1linkedancestor_10percent_TrainingSet = readAndLabelStats("%s/p2_p1_linkedancestor_bgs_10percent.msOut" %(statDir), 3, 10000)
with open(trainingSetFileName+'linkedancestor_10percent.fvec', "w") as outFile:
    outFile.write(header)
    for line in nomiglinkedancestor_10percent_TrainingSet:
        outFile.write(line)
    for line in p1p2linkedancestor_10percent_TrainingSet:
        outFile.write(line)
    for line in p2p1linkedancestor_10percent_TrainingSet:
        outFile.write(line)

# next, prep linked ancestor 15% dataset
header, nomiglinkedancestor_15percent_TrainingSet = readAndLabelStats("%s/nomig_linkedancestor_bgs_15percent.msOut" %(statDir), 1, 10000)
header, p1p2linkedancestor_15percent_TrainingSet = readAndLabelStats("%s/p1_p2_linkedancestor_bgs_15percent.msOut" %(statDir), 2, 10000)
header, p2p1linkedancestor_15percent_TrainingSet = readAndLabelStats("%s/p2_p1_linkedancestor_bgs_15percent.msOut" %(statDir), 3, 10000)
with open(trainingSetFileName+'linkedancestor_15percent.fvec', "w") as outFile:
    outFile.write(header)
    for line in nomiglinkedancestor_15percent_TrainingSet:
        outFile.write(line)
    for line in p1p2linkedancestor_15percent_TrainingSet:
        outFile.write(line)
    for line in p2p1linkedancestor_15percent_TrainingSet:
        outFile.write(line)

# next prep adaptive int 5%
header, nomigadaptiveint_5percent_TrainingSet = readAndLabelStats("%s/nomig_bgs.msOut" %(statDir), 1, 10000)
header, p1p2adaptiveint_5percent_TrainingSet = readAndLabelStats("%s/p1_p2_adaptiveint_bgs_5percent.msOut" %(statDir), 2, 10000)
header, p2p1adaptiveint_5percent_TrainingSet = readAndLabelStats("%s/p2_p1_bgs.msOut" %(statDir), 3, 10000)
with open(trainingSetFileName+'adaptiveint_5percent.fvec', "w") as outFile:
    outFile.write(header)
    for line in nomigadaptiveint_5percent_TrainingSet:
        outFile.write(line)
    for line in p1p2adaptiveint_5percent_TrainingSet:
        outFile.write(line)
    for line in p2p1adaptiveint_5percent_TrainingSet:
        outFile.write(line)

# next prep adaptive int 10%
header, nomigadaptiveint_10percent_TrainingSet = readAndLabelStats("%s/nomig_bgs.msOut" %(statDir), 1, 10000)
header, p1p2adaptiveint_10percent_TrainingSet = readAndLabelStats("%s/p1_p2_adaptiveint_bgs_10percent.msOut" %(statDir), 2, 10000)
header, p2p1adaptiveint_10percent_TrainingSet = readAndLabelStats("%s/p2_p1_bgs.msOut" %(statDir), 3, 10000)
with open(trainingSetFileName+'adaptiveint_10percent.fvec', "w") as outFile:
    outFile.write(header)
    for line in nomigadaptiveint_10percent_TrainingSet:
        outFile.write(line)
    for line in p1p2adaptiveint_10percent_TrainingSet:
        outFile.write(line)
    for line in p2p1adaptiveint_10percent_TrainingSet:
        outFile.write(line)

# next prep adaptive int 15%
header, nomigadaptiveint_15percent_TrainingSet = readAndLabelStats("%s/nomig_bgs.msOut" %(statDir), 1, 10000)
header, p1p2adaptiveint_15percent_TrainingSet = readAndLabelStats("%s/p1_p2_adaptiveint_bgs_15percent.msOut" %(statDir), 2, 10000)
header, p2p1adaptiveint_15percent_TrainingSet = readAndLabelStats("%s/p2_p1_bgs.msOut" %(statDir), 3, 10000)
with open(trainingSetFileName+'adaptiveint_15percent.fvec', "w") as outFile:
    outFile.write(header)
    for line in nomigadaptiveint_15percent_TrainingSet:
        outFile.write(line)
    for line in p1p2adaptiveint_15percent_TrainingSet:
        outFile.write(line)
    for line in p2p1adaptiveint_15percent_TrainingSet:
        outFile.write(line)


