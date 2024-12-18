import numpy as np

total = 0
with open('dag8input.txt', encoding='ascii' ) as fp:
    data = fp.readlines()
    dd = []
    for line in data:
        dd.append([c for c in line.strip()])
    a = np.array(dd)
    b = {}
    
    nx = a.shape[0]
    ny = a.shape[1]
    for i in range(nx):
        for j in range(ny):
            if a[i,j] != '.':
                v = b.get(a[i,j], [])
                v.append((i,j))
                b[a[i,j]] = v
    
    u = {}
    nx, ny = a.shape
    for k in b:
        c = b[k]
        for i in range(len(c)):
            x1, y1 = c[i]
            for j in range(i + 1, len(c)):
                x2, y2 = c[j]
                dx = x1 - x2
                dy = y1 - y2
                u[(x2,y2)] = k
                x3 = x2 - dx
                y3 = y2 - dy
                while x3 >= 0 and x3 < nx and y3 >= 0 and y3 < ny:
                    u[(x3,y3)] = k
                    x3 = x3 - dx
                    y3 = y3 - dy
                x3 = x2 + dx
                y3 = y2 + dy
                while x3 >= 0 and x3 < nx and y3 >= 0 and y3 < ny:
                    u[(x3,y3)] = k
                    x3 = x3 + dx
                    y3 = y3 + dy
        
    total = len(u)

print(total)