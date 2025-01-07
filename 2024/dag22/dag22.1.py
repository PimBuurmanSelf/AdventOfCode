import operator

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
    for line in data:
        s = int(line)
        for i in range(nSteps):
            s = nextsecret(s)
        total += s
        
print(total)
