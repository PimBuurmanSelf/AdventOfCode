import operator
from collections import defaultdict

total = 0

def mix(v, s):
    return operator.xor(s, v)
    
def prune(s):
    return s % 16777216
    
def nextsecret(v):
    v = prune(mix(v * 64, v))
    v = prune(mix(int(v / 32), v))
    return prune(mix(v * 2048, v))
    
#problem = ('dag22ainput.txt', 2000)
problem = ('dag22input.txt', 2000)
nSteps = problem[1]
with open(problem[0], encoding='ascii' ) as fp:
    data = fp.read().strip().split('\n')
    diffs = defaultdict(int)
    for line in data:
        s = int(line)
        prev = s % 10
        dif = []
        has = set()
        for i in range(nSteps):
            s = nextsecret(s)
            curr = s % 10
            dif.append(curr - prev)
            if len(dif) >= 4:
                t = tuple(dif[-4:])
                if not t in has:
                    diffs[t] += curr
                    has.add(t)
            prev = curr
    mv = -1
    md = None
    for dif in diffs:
        if diffs[dif] > mv:
            md = dif
            mv = diffs[dif]
            
total = mv
print(total)
