import numpy as np
    
total = 0
ok = True
with open('dag15input.txt', encoding='ascii' ) as fp:
    data = fp.read().strip().split('\n')
    dd = []
    mv = ''
    for line in data:
        if line.startswith('#'):
            dd.append([c for c in line])
        elif len(line) > 0 and line[0] in '<>v^':
            mv = mv + line
    a = np.array(dd)
    #print(a, mv)
    nx = a.shape[0]
    ny = a.shape[1]
    for i in range(nx):
        for j in range(ny):
            if a[i,j] == '@':
                p0 = (i, j)
                a[i, j] = '.'
                break
                
    dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    p = p0
    for m in mv:
        d = dirs[m]
        pn = (p[0] + d[0], p[1] + d[1])
        if a[pn] == '.':
            p = pn
            continue
        if a[pn] == '#':
            continue
        p1 = pn
        while a[p1] == 'O':
            p1 = (p1[0] + d[0], p1[1] + d[1])
        if a[p1] == '#':
            continue
        while p1 != pn:
            a[p1] = 'O'
            p1 = (p1[0] - d[0], p1[1] - d[1])
        a[pn] = '.'
        p = pn

    for x in range(nx):
        for y in range(ny):
            if a[x,y] == 'O':
                total += 100 * x + y
    print(total)