def within(s1,e1,s2,e2):
    return s1 <= e2 and s1 >= s2 and e1 <= e2 and e1 >= s2

def minDist(s1,e1,s2,e2):
    if overlap(s1,e1,s2,e2):
        return 0
    else:
        return min([abs(s1-e2),abs(s2-e1)])

def overlap(x1,y1,x2,y2):
    r = 0
    if (y2 < x2 or y1 < x1):
        raise Exception
    elif (y1 <= y2 and y1 >= x2):
        if (x1 > x2):
            r = (x1,y1);
        else:
            r = (x2,y1)
    elif (x1 <= y2 and x1 >= x2):
        if (y1 < y2):
            r = (x1,y1)
        else:
            r = (x1,y2)
    elif (y2 <= y1 and y2 >= x1):
        if (x2 > x1):
            r = (x2,y2)
        else:
            r = (x1,y2)
    elif (x2 <= y1 and x2 >= x1):
        if (y2 < y1):
            r = (x2,y2)
        else:
            r = (x2,y1)
    return r

def mergeOverlappingElements(elements):
    elements.sort()
    i = 0
    while i < len(elements):
        c,s,e = elements[i]
        assert s <= e
        j = i+1
        while j < len(elements):
            currc,currs,curre = elements[j]
            assert currs <= curre
            if c == currc and overlap(currs,curre,s,e):
                elements.pop(j)
                s,e = min(currs,s),max(curre,e)
            else:
                j += 1
        elements[i] = (c,s,e)
        i += 1
    return elements

def mergeOverlappingOrAdjacentElements(elements):
    elements.sort()
    i = 0
    while i < len(elements):
        c,s,e = elements[i]
        assert s <= e
        j = i+1
        while j < len(elements):
            currc,currs,curre = elements[j]
            assert currs <= curre
            if c == currc and overlap(currs-1,curre+1,s,e):
                elements.pop(j)
                s,e = min(currs,s),max(curre,e)
            else:
                j += 1
        elements[i] = (c,s,e)
        i += 1
    return elements

def sumElementSizes(elements):
    l = 0
    for c,s,e in elements:
        l += (e-s+1)
    return l

def readBedCoordsIntoList(bedFileName):
    coordLs = []
    with open(bedFileName) as bedFile:
        for line in bedFile:
            if not line.startswith("track"):
                line = line.strip()
                c, s, e = line.split("\t")[:3]
                s, e = int(s)+1, int(e)
                coordLs.append((c, s, e))
    return coordLs
