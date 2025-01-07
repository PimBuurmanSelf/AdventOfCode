import numpy as np
from heapq import heappush, heappop
import sys
import functools
    
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d2a = {(-1, 0): '^', (0, 1): '>', (1, 0): 'v', (0, -1): '<'}
numpad = {'7': (0,0), '8': (0, 1), '9': (0, 2), '4': (1,0), '5': (1, 1), '6': (1, 2), '1': (2,0), '2': (2, 1), '3': (2, 2), '0': (3, 1), 'A': (3, 2)}
dirpad = {'^': (0, 1), 'A': (0, 2), '<': (1, 0), 'v': (1, 1), '>': (1, 2)}

numpaths = {}
dirpaths = {}

def getpath(p0, pE, cost):
    if pE == p0:
        return [(0,2)]
    paths = []
    for d in dirs:
        pn = (pE[0] + d[0], pE[1] + d[1])
        if pn == p0:
            return [[d],]
        if cost[pn] == cost[pE] - 1:
            np = []
            for pp in getpath(p0, pn, cost):
                ppp = pp.copy()
                ppp.append(d)
                paths.append(ppp)
    return paths         

def get_paths(k1, k2, pad):
    a = np.zeros((6, 5))
    for x, y in pad.values():
        a[x+1, y+1] = 1
    nx, ny = a.shape
    cost = np.ones((nx, ny), dtype=int)
    cost *= -2
    p0 = (pad[k1][0] + 1, pad[k1][1] + 1)
    pE = (pad[k2][0] + 1, pad[k2][1] + 1)
    p = p0
    cost[p0] = 0
    front = []
    heappush(front, (0, p0))
    while front:
        c0, p = heappop(front)
        for d in dirs:
            pn = (p[0] + d[0], p[1] + d[1])
            if a[pn] == 0:
                continue
            c = c0 + 1
            if cost[pn] == -2:
                cost[pn] = c
                if pn != pE:
                    heappush(front, (c, pn))
    return getpath(p0, pE, cost)
    
revmap = {'<': '>', '>': '<', 'v': '^', '^': 'v', 'A': 'A'}
def revpath(p):
    r = []
    for c in p[:-1][::-1]:
        r.append(revmap[c])
    if p and p[-1] == 'A':
        r.append('A')
    return ''.join(r)
    
for k1 in numpad:
    for k2 in numpad:
        if k1 == k2:
            numpaths[(k1, k2)] = 'A'
        else:
            paths = get_paths(k1, k2, numpad)
            revpaths = []
            pp2 = []
            for pp in paths:
                rp = []
                p2 = []
                for dx, dy in pp:
                    p2.insert(0, d2a[(dx, dy)])
                    rp.append(d2a[(-dx, -dy)])
                pp2.append(''.join(p2) + 'A')
                revpaths.append(''.join(rp) + 'A')
            #print('x', k1, k2, revpaths, paths)
            numpaths[(k1, k2)] = revpaths
            numpaths[(k2, k1)] = pp2
            
for k1 in dirpad:
    for k2 in dirpad:
        if k1 == k2:
            dirpaths[(k1, k2)] = 'A'
        else:
            paths = get_paths(k1, k2, dirpad)
            revpaths = []
            pp2 = []
            for pp in paths:
                rp = []
                p2 = []
                for dx, dy in pp:
                    p2.insert(0, d2a[(dx, dy)])
                    rp.append(d2a[(-dx, -dy)])
                pp2.append(''.join(p2) + 'A')
                revpaths.append(''.join(rp) + 'A')
            dirpaths[(k1, k2)] = revpaths
            dirpaths[(k2, k1)] = pp2

@functools.cache
def chain(k1, k2, level):
    if level == 1:
        return min([len(v) for v in dirpaths[(k1, k2)]])
    minlen = 100000000000000000
    for line in dirpaths[(k1, k2)]:
        pos = 'A'
        # dirpad
        s = 0
        for c in line:
            s += chain(pos, c, level - 1)
            pos = c
        if s < minlen:
            minlen = s
    return minlen

total = 0
ok = True
problem = ('dag21ainput.txt', )
problem = ('dag21input.txt', )
with open(problem[0], encoding='ascii' ) as fp:
    data = fp.read().strip().split('\n')
    for line in data:
        # numpad
        minlen = 100000000000000
        pos = 'A'
        ppp = []
        for c in line:
            newppp = []
            for pp in numpaths[(pos, c)]:
                if not ppp:
                    newppp.append(pp)
                else:
                    for p in ppp:
                        newppp.append(p + pp)
            pos = c
            ppp = newppp
        for pline in ppp:
            s = 0
            pk = 'A'
            for k in pline:
                s += chain(pk, k, 25)
                pk = k
            
            if s < minlen:
                minlen = s
                
            
        val = int(line[:-1])
        total += val * minlen

    print(total)