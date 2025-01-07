import numpy as np
    
total = 0
ok = True
#problem = ('dag18ainput.txt', 7, 12)
problem = ('dag18input.txt', 71, 1024)
nx = ny = problem[1] + 2
nBytes = problem[2]
with open(problem[0], encoding='ascii' ) as fp:
    data = fp.read().strip().split('\n')
    a = np.zeros((nx, ny), dtype=int) 
    for line in data[:nBytes]:
        print(line)
        x, y = line.split(',')
        a[int(x)+1, int(y)+1] = 1
    for x in range(nx):
        a[x,0] = 1
        a[x,ny-1] = 1
        a[0,x] = 1
        a[nx-1,x] = 1
    p0 = (1, 1)
    pE = (nx-2, ny-2)
                
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    cost = np.ones((nx, ny), dtype=int)
    cost *= -1
    p = p0
    cost[p0] = 0
    front = [(0, p0)]
    found = False
    while front:
        nf = []
        for c0, p in front:
            for d in dirs:
                pn = (p[0] + d[0], p[1] + d[1])
                if a[pn] == 1:
                    continue
                c = c0 + 1
                if cost[pn] == -1 or c < cost[pn]:
                    cost[pn] = c
                    if pn != pE:
                        nf.append((c, pn))
                    if pn == pE:
                        found = True
        #print(nf)
        nf.sort()
        front = nf
        if not front:
            break

    #print(a)
    for r in a:
        print(''.join(['%d' % v for v in r]))
    #print(cost)
    #for r in cost:
    #    print(' '.join(['% 4d' % v for v in r]))
    total = cost[pE]
    print(total)