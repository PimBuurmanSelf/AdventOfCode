import functools

total = 0
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
        
    oper, x, y = conns[v]
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
    zs = set()
    for line in data:
        if ':' in line:
            flds = line.split(':')
            vals[flds[0]] = int(flds[1].strip())
        elif '->' in line:
            flds = line.split()
            conns[flds[4]] = (flds[1], flds[0], flds[2])
            if flds[4][0] == 'z':
                zs.add(flds[4])
      
    for z in zs:
        zv = calc(z)
        if zv == 1:
            p = int(z[1:])
            total += pow2(p)
            
print(total)
    
            
    
            
    
    
