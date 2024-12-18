import numpy as np
    
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1), ]

def walk(a, p0, di0, check):
    di = di0
    d = dirs[di]
    p = p0
    seen = set()
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
                    print(-2, p, d)
                    di = (di + 1) % 4
                    d = dirs[di]
                    pn = (p[0] + d[0], p[1] + d[1])
                    if pn[0] < 0 or pn[0] >= nx or pn[1] < 0 or pn[1] >= ny:
                        break
                    if a[pn] == '#':
                        break
        p = pn
        if check and (p, di) in seen:
            return True
        seen.add((p, di))
    if check:
        return False
    return seen

total = 0
ok = True
with open('dag6input.txt', encoding='ascii' ) as fp:
    data = fp.readlines()
    dd = []
    for line in data:
        dd.append([c for c in line.strip()])
    a = np.array(dd)
    
    nx, ny = a.shape
    for i in range(nx):
        for j in range(ny):
            if a[i,j] == '^':
                p0 = (i, j)
               
    seen0 = walk(a, p0, 0, False)
    obs = set()
    done = set([p0])
    for p, d in seen0:
        if p not in done:
            done.add(p)
            a[p] = '#'
            if walk(a, p0, 0, p):
                total += 1
                obs.add(p)
            a[p] = '.'
#    for p, d in seen0:
#        if p in obs:
#            a[p] = 'X'
#        elif p != p0:
#            a[p] = str(d)
#    for r in a:
#        print(''.join(r))
    print(total)
