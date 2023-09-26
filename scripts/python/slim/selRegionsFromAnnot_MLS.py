import sys
import gzip
import numpy as np
import overlapper

def readChrLens(chrLenFileName):
    chrLens = {}
    with open(chrLenFileName, "rt") as chrLenFile:
        for line in chrLenFile:
            c, l = line.strip().split()
            chrLens[c] = int(l)
    return chrLens

def truncateChrLensByL(chrLens, L):
    newChrLens = {}
    for c in chrLens:
        l = chrLens[c]
        assert l > L
        newChrLens[c] = l-L+1
    return newChrLens

def pickRandomWindowAnyStart(L, chrLens, state=None):
    L = int(L)
    chrLensTrunc = truncateChrLensByL(chrLens, L)
    chrs = sorted(chrLensTrunc)
    denom = float(sum(chrLensTrunc.values()))
    weights = [chrLensTrunc[x]/denom for x in chrs]
    if state:
        np.random.set_state(state)
    winC = np.random.choice(chrs, p=weights)
    winStart = np.random.randint(1, chrLens[winC]+1)
    return winC, winStart, winStart+L-1

def countTotalPossibleWinStarts(chrLens, L, subWinSize, gapData):
    counts = {}
    assert L % subWinSize == 0
    numSubWins = int(L/subWinSize)
    for c in chrLens:
        lastWinEnd = chrLens[c]-(chrLens[c]%L)
        if c in gapData:
            counts[c] = 0
            for winEnd in range(L, lastWinEnd+1, subWinSize):
                winStart = winEnd-L+1
                if winNotTooGappy(c, winStart, winEnd, gapData):
                    counts[c] += 1
        else:
            counts[c] = int(lastWinEnd/subWinSize)-(numSubWins-1)
    return counts

def readGapFile(gapFileName, chrLens, L, subWinSize):
    gapData = {}
    if gapFileName:
        with open(gapFileName, "rt") as gapFile:
            for line in gapFile:
                c, s, e = line.strip().split()
                if c in chrLens:
                    if not c in gapData:
                        gapData[c] = np.zeros(chrLens[c], dtype=bool)
                    for posMinusOne in range(int(s), int(e)):
                        gapData[c][posMinusOne] = True
    for c in gapData:
        gapFracsForC = {}
        lastWinEnd = chrLens[c]-(chrLens[c]%L)
        for winEnd in range(L, lastWinEnd+1, subWinSize):
            winStart = winEnd-L+1
            gapFracsForC[(winStart, winEnd)] = np.count_nonzero(gapData[c][winStart-1:winEnd])/float(L)
        gapData[c] = gapFracsForC
    return gapData

def winNotTooGappy(winC, winStart, winEnd, gapData, gapThreshold=0.75):
    if winC in gapData:
        return gapData[winC][(winStart, winEnd)] < gapThreshold
    else:
        return True

def pickRandomWindow(L, chrLens, gapFileName=None, numSubWins=1, state=None):
    subWinSize=int(L/numSubWins)
    L = int(L)
    gapData = readGapFile(gapFileName, chrLens, L, subWinSize)
    totalPossibleWinStartsPerChr = countTotalPossibleWinStarts(chrLens, L, subWinSize, gapData)
    chrs = sorted(totalPossibleWinStartsPerChr)
    denom = sum(totalPossibleWinStartsPerChr.values())
    weights = [totalPossibleWinStartsPerChr[x]/denom for x in chrs]

    if state:
        np.random.set_state(state)

    goodWinChosen = False
    tries = 0
    while not goodWinChosen:
        if tries > 100:
            sys.exit("Tried 100 times to pick a window that wasn't too gappy and failed. Something must be wrong. AAARRRGHHHHH!!!")
        winC = np.random.choice(chrs, p=weights)
        winStart = 1 + subWinSize*np.random.randint(0, totalPossibleWinStartsPerChr[winC])
        winEnd = winStart+L-1
        if winNotTooGappy(winC, winStart, winEnd, gapData):
            goodWinChosen = True
        else:
            sys.stderr.write("Rejecting %s:%d-%d because it had too many damn gaps!\n" %(winC, winStart, winEnd))
        tries += 1
    sys.stderr.write("Succeeding in finding a region after %d attempts\n" %(tries))
    return winC, winStart, winStart+L-1

def readRecRegionsInWinFromWig(recRateFileName, winC, winStart, winEnd, rRescale=1.0):
    if recRateFileName.endswith(".gz"):
        openFunc = gzip.open
    else:
        openFunc = open
    L=winEnd-winStart+1

    totalRecRateInMorgans = 0
    rregionCoords = []
    with openFunc(recRateFileName, "rt") as recRateFile:
        for line in recRateFile:
            if not line.startswith("#"):
                c, s, e, ratePerBp = line.strip().split()
                if c == winC:
                    s, e = int(s)+1, int(e)
                    overRange = overlapper.overlap(s, e, winStart, winEnd)
                    if overRange:
                        overS, overE = overRange
                        overS, overE = overS-winStart, overE-winStart
                        rateInRegion = float(ratePerBp)*rRescale#*(overE-overS+1) #changed to be per bp
                        rregionCoords.append((overS, overE, rateInRegion))
                        totalRecRateInMorgans += rateInRegion
    return rregionCoords, totalRecRateInMorgans

def readSelRegionsInWinFromGtf(geneAnnotFileName, winC, winStart, winEnd, cncSelRatio, phastConsFileName=None, codingSelFrac=0.75, nonCodingSelFrac=0.75):
    """Note that I altered this so that it would write neutral regions to the same list that it wrote cne and coding regions because it is easier to input into slim."""
    if geneAnnotFileName.endswith(".gz"):
        openFunc = gzip.open
    else:
        openFunc = open
    L=winEnd-winStart+1
    isSel=[0]*L

    if phastConsFileName:
        if phastConsFileName.endswith(".gz"):
            openFunc = gzip.open
        else:
            openFunc = open
        if phastConsFileName.rstrip(".gz").endswith(".bed"):
            coordIndices = (0, 1, 2)
        else:
            coordIndices = (1, 2, 3)
        with openFunc(phastConsFileName, "rt") as phastConsFile:
            for line in phastConsFile:
                if not line.startswith("#"):
                    line = line.strip().split()
                    c, s, e = [line[x] for x in coordIndices]
                    if c == winC:
                        overRange = overlapper.overlap(int(s)+1, int(e), winStart, winEnd)
                        if overRange:
                            overS, overE = overRange
                            overS, overE = overS-winStart, overE-winStart
                            for pos in range(overS, overE+1):
                                isSel[pos-1] = 1

    with openFunc(geneAnnotFileName, "rt") as geneAnnotFile:
        for line in geneAnnotFile:
            if not line.startswith("#"):
                c, source, annotType, s, e = line.strip().split()[:5]
                if c == winC and annotType == "exon":
                    overRange = overlapper.overlap(int(s), int(e), winStart, winEnd)
                    if overRange:
                        overS, overE = overRange
                        overS, overE = overS-winStart, overE-winStart
                        for pos in range(overS, overE+1):
                            isSel[pos-1] = 2

    nregionCoords = []
    sregionCoords = []
    prevState = isSel[0]
    runStart = 1
    totSelRegionSize = 0
    for i in range(1,L):
        if isSel[i] == prevState:
            pass
        else:
            runEnd = i
            if prevState == 2:
                sregionCoords.append((runStart, runEnd, codingSelFrac, 1))
                totSelRegionSize += (runEnd-runStart+1)*codingSelFrac
            elif prevState == 1:
                sregionCoords.append((runStart, runEnd, nonCodingSelFrac, cncSelRatio))
                totSelRegionSize += (runEnd-runStart+1)*nonCodingSelFrac
            else:
                sregionCoords.append((runStart, runEnd, 0, 0))
            prevState = isSel[i]
            runStart = i+1
    runEnd = L
    if prevState == 2:
        sregionCoords.append((runStart, runEnd, codingSelFrac, 1))
        totSelRegionSize += (runEnd-runStart+1)*codingSelFrac
    elif prevState == 1:
        sregionCoords.append((runStart, runEnd, nonCodingSelFrac, cncSelRatio))
        totSelRegionSize += (runEnd-runStart+1)*nonCodingSelFrac
    else:
        sregionCoords.append((runStart, runEnd, 0, 0))
    return sregionCoords, totSelRegionSize

def readCncCoordsInTargRegion(cncAnnotFileName, targC, targS, targE):
    cncCoords = []
    if cncAnnotFileName.endswith(".gz"):
        fopen = gzip.open
    else:
        fopen = open
    with fopen(cncAnnotFileName, 'rt') as cncAnnotFile:
        for line in cncAnnotFile:
            if not line.startswith("#"):
                binId, c, s, e, name, score = line.strip().split()
                s, e = int(s), int(e)
                if c == targC and overlapper.overlap(s, e, targS, targE):
                    s = max(targS, s)
                    e = min(targE, e)
                    cncCoords.append((s, e))
    return cncCoords

def readGeneCoordsInTargRegion(geneAnnotFileName, targC, targS, targE):
    geneCoords = []
    if geneAnnotFileName.endswith(".gz"):
        fopen = gzip.open
    else:
        fopen = open
    with fopen(geneAnnotFileName, 'rt') as geneAnnotFile:
        for line in geneAnnotFile:
            if not line.startswith("#"):
                c, source, annotType, s, e, blah1, strand, blah2, info = line.strip().split("\t")
                s, e = int(s), int(e)
                if c == targC and annotType == "exon" and overlapper.overlap(s, e, targS, targE):
                    s = max(targS, s)
                    e = min(targE, e)
                    geneCoords.append((s, e))
    return geneCoords

def coordsToWindowedDensities(cncCoords, targS, targE, winSize=10000):
    cncBases = {}
    for s, e in cncCoords:
        for pos in range(s, e+1):
            cncBases[pos] = 1

    cncDensities = {}
    for pos in cncBases:
        winStart = pos - (pos%winSize) + 1
        if not winStart in cncDensities:
            cncDensities[winStart] = 0
        cncDensities[winStart] += 1

    xvals, yvals = [], []
    winStart = targS - (targS % winSize) + 1
    winEnd = winStart + winSize - 1
    while winEnd <= targE:
        winMidpt = (winStart+winEnd+1)/2
        xvals.append(winMidpt)
        yvals.append(cncDensities.get(winStart,0))
        winStart += winSize
        winEnd += winSize
    return xvals, yvals
