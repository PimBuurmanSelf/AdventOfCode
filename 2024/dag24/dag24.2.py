import functools

total = 0
#problem = ('dag24ainput.txt',)
#problem = ('dag24binput.txt',)
problem = ('dag24input.txt',)

def andG(x, y):
    return 1 if x + y == 2 else 0

def orG(x, y):
    return 1 if x + y >= 1 else 0
    
def xorG(x, y):
    return 1 if x + y == 1 else 0
    
fmap = {'AND': andG, 'OR': orG, 'XOR': xorG}

@functools.cache
def calc(v):
    if v in vals:
        return vals[v]
        
    oper, (x, y) = conns[v]
    xv = calc(x)
    yv = calc(y)
    f = fmap[oper]
    return f(xv, yv)

def pow2(x):
    v = 1
    while x > 0:
        v *= 2
        x -= 1
    return v
    
with open(problem[0], encoding='ascii' ) as fp:
    data = fp.read().strip().split('\n')
    vals = {}
    conns = {}
    revcons = {}
    zs = set()
    tp = {}
    
    for line in data:
        if ':' in line:
            flds = line.split(':')
            vals[flds[0]] = int(flds[1].strip())
        elif '->' in line:
            flds = line.split()
            k = flds[4]
            if 'XOR x' in line or 'XOR y' in line:
                tp[k] = 1
            elif 'XOR' in line:
                tp[k] = 3
            elif '00 AND' in line:
                tp[k] = 5
            elif 'AND x' in line or 'AND y' in line:
                tp[k] = 2
            elif 'AND' in line:
                tp[k] = 4
            elif ' OR ' in line:
                tp[k] = 5
            conns[k] = (flds[1], sorted([flds[0], flds[2]]))
            if k[0] == 'z':
                zs.add(k)
    
    tp['x00'] = 4
    tp['y00'] = 2
    zlast = max(zs)
    toswap = {}
    for k in conns:
        if k[0] == 'z':
            if k == 'z00' and tp[k] != 1:
                toswap[k] = (tp[k], 1)
            elif k == zlast and tp[k] != 5:
                toswap[k] = (tp[k], 5)
            elif k not in ('z00', zlast) and tp[k] != 3:
                toswap[k] = (tp[k], 3)
        if tp[k] == 4:
            k1 = conns[k][1][0]
            k2 = conns[k][1][1]
            v1 = tp[conns[k][1][0]]
            v2 = tp[conns[k][1][1]]
            if v1 in (5, 1) and v2 in (5, 1) and v1 != v2:
                continue
            if v1 not in (5, 1):
                if v2 == 1:
                    toswap[k1] = (v1, 5)
                else:
                    toswap[k1] = (v1, 1)
            else:
                if v1 == 1:
                    toswap[k2] = (v2, 5)
                else:
                    toswap[k2] = (v2, 1)
        if tp[k] == 5:
            k1 = conns[k][1][0]
            k2 = conns[k][1][1]
            v1 = tp[conns[k][1][0]]
            v2 = tp[conns[k][1][1]]
            if v1 in (2, 4) and v2 in (2, 4) and v1 != v2:
                continue
            if v1 not in (2, 4):
                if v2 == 2:
                    toswap[k1] = (v1, 4)
                else:
                    toswap[k1] = (v1, 2)
            else:
                if v1 == 2:
                    toswap[k2] = (v2, 4)
                else:
                    toswap[k2] = (v2, 2)
                
    if len(toswap) != 8:
        print('XXX Error: len(toswap) is not 8, but', len(toswap), toswap)
    else:
        swap = {}
        for k, v in toswap.items():
            match = [k1 for k1 in toswap if toswap[k1] == (v[1], v[0])]
            if len(match) == 1:
                swap[k] = match[0]
        if len(swap) != 8:
            print('XXX Error: len(swap) is not 8, but', len(swap), 'toswap =', toswap, 'swap =', swap)
        else:
            print(','.join(sorted(toswap.keys())))
    
            
    
            
    
    
