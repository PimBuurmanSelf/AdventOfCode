import sys
import functools

total = 0
#problem = ('dag19ainput.txt',)
problem = ('dag19input.txt',)

@functools.cache
def can(t):
    if len(t) == 0:
        return True
    for i in range(len(t), -1, -1):
        if t[:i] in tps:
            if can(t[i:]):
                break
    else:
        return False
    return True
        
with open(problem[0], encoding='ascii' ) as fp:
    data = fp.read().strip().split('\n')
    tps = set(data[0].split(', '))
    
    for t in data[2:]:
        if can(t):
            total += 1

    print(total)