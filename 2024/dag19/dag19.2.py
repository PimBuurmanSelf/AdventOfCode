import functools

total = 0
#problem = ('dag19ainput.txt',)
problem = ('dag19input.txt',)

@functools.cache
def can(t):
    if len(t) == 0:
        return 1
    s = 0
    for i in range(len(t), -1, -1):
        if t[:i] in tps:
            s += can(t[i:])
    return s
        
with open(problem[0], encoding='ascii' ) as fp:
    data = fp.read().strip().split('\n')
    tps = set(data[0].split(', '))
    
    for t in data[2:]:
        total += can(t)

    print(total)