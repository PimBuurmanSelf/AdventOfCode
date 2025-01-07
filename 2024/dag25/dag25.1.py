from collections import defaultdict

total = 0
#problem = ('dag25ainput.txt', 2000)
problem = ('dag25input.txt', 2000)
nSteps = problem[1]
with open(problem[0], encoding='ascii' ) as fp:
    data = fp.read().strip().split('\n')
    keys = []
    locks = []
    s = 0
    for line in data:
        if not line:
            s = 0
            continue
        if s == 0:
            v = [0] * 5
            n = 0
            if line == '#####':
                s = 1
            else:
                s = 2
            continue
        n += 1
        if n == 6:
            if s == 1:
                keys.append(v)
            else:
                locks.append(v)
            continue
        for i in range(5):
            if line[i] == '#':
                v[i] += 1
                
    for k in keys:
        for lk in locks:
            for i in range(5):
                if k[i] + lk[i] > 5:
                    break
            else:
                total += 1
    print(total)
