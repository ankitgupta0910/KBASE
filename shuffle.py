import urllib, sys, tsp
import networkx as nx

def readDataFromFile(fileName):
    dicti = {}
    with open(fileName) as f:
        idx = 1
        for l in f:
            dicti[idx] = urllib.unquote(l[:-1])
            idx += 1
        return dicti

def meanLength(fileName):
    s = 0
    tot = 0
    data = readDataFromFile(fileName)
    for name, seq in data.items():
        s += len(seq)
        tot += 1
    return s / float(tot)


def getOverlap(left, right):
    for i in range(len(left)):
        if left[i:] == right[:len(left) - i]:
            return left[i:]
    return ''


def getAllOverlaps(reads):
    d = []
    for name1, seq1 in reads.items():
        for name2, seq2 in reads.items():
            if name1 == name2:
                continue
            # if name1 not in d:
            #     d[name1] = dict()
            if len(getOverlap(seq1, seq2)) > 2:
                # d[name1][name2] = len(getOverlap(seq1, seq2))
                d.append((name1, name2, len(getOverlap(seq1, seq2))))
    return d


def prettyPrint(d):
    print '   ',
    for j in sorted(d, key=int):
        print "% 3s" % j,
    print

    for i in sorted(d, key=int):
        print "% 3s" % i,
        for j in sorted(d, key=int):
            if i == j:
                s = '  -'
            else:
                s = "% 3s" % d[str(i)][str(j)]
            print s,
        print


def findFirstRead(overlaps):
    for i in overlaps:
        signifOverlaps = False
        for j in d[i]:
            if d[j][i] > 2:
                signifOverlaps = True
        if not signifOverlaps:
            return i


def findKeyForLargestValue(d):
    m = max(d.values())
    for k in d:
        if d[k] == m:
            return k


def findOrder(first, d):
    if max(d[first].values()) < 3:
        return [first]
    else:
        nextRead = findKeyForLargestValue(d[first])
        return [first] + findOrder(nextRead, d)


def assembleGenome(readOrder, reads, overlaps):
    genome = ''
    for readName in readOrder[:-1]:
        rightOverlap = max(x for x in overlaps[readName].values() if x >= 2)
        genome += reads[readName][:-rightOverlap]
    genome += reads[readOrder[-1]]
    return genome

#################################################################################################
## NB: do not include testing code when you and in your assignment. The code below is only
## included to help you see how you can test your own code.
#################################################################################################
if __name__ == "__main__":
    fileName = '/Users/ankitgupta/PycharmProjects/untitled1/sample_input'
    reads = readDataFromFile(fileName)

    d = getAllOverlaps(reads)
    print d
    G = nx.DiGraph()
    G.add_weighted_edges_from(d)

    print G.number_of_nodes()
    print G.number_of_edges()
    i = 1

    while i <= 21:
        j = 2
        while j <= 21:
            for path in nx.all_simple_paths(G, i, j):
                if len(path) is 21:
                    print path
            j += 1
        i += 1
