import numpy as np
    
total = 0
ok = True
with open('dag6input.txt', encoding='ascii' ) as fp:
    data = fp.readlines()
    dd = []
    for line in data:
        dd.append([c for c in line.strip()])
    a = np.array(dd)
    
    nx = a.shape[0]
    ny = a.shape[1]
    for i in range(nx):
        for j in range(ny):
            if a[i,j] == '^':
                p = (i, j)
                
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1), ]
    di = 0
    d = dirs[di]
    a[p] = 'X'
    total += 1
    while True:
        pn = (p[0] + d[0], p[1] + d[1])
        if pn[0] < 0 or pn[0] >= nx or pn[1] < 0 or pn[1] >= ny:
            break
        if a[pn] == '#':
            di = (di + 1) % 4
            d = dirs[di]
            pn = (p[0] + d[0], p[1] + d[1])
            if pn[0] < 0 or pn[0] >= nx or pn[1] < 0 or pn[1] >= ny:
                break
            if a[pn] == '#':
                di = (di + 1) % 4
                d = dirs[di]
                pn = (p[0] + d[0], p[1] + d[1])
                if pn[0] < 0 or pn[0] >= nx or pn[1] < 0 or pn[1] >= ny:
                    break
                if a[pn] == '#':
                    di = (di + 1) % 4
                    d = dirs[di]
                    pn = (p[0] + d[0], p[1] + d[1])
                    if pn[0] < 0 or pn[0] >= nx or pn[1] < 0 or pn[1] >= ny:
                        break
                    if a[pn] == '#':
                        break
        p = pn
        if a[p] != 'X':
            a[p] = 'X'
            total += 1

    
    print(total)