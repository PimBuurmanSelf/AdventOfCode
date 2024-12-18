import numpy as np
        
def inNextRow(a, ps, d):
    nl = set()
    for p in ps:
        if a[p] == '#':
            return -1
        if a[p] == '.':
            continue
        q = (p[0] + d[0], p[1] + d[1])
        nl.add(q)
        if a[p] == '[' and a[q] == ']':
            nl.add((q[0], q[1] - 1))
        elif a[p] == ']' and a[q] == '[':
            nl.add((q[0], q[1] + 1))
    return list(nl)
    
total = 0
with open('dag15input.txt', encoding='ascii' ) as fp:
    data = fp.read().strip().split('\n')
    dd = []
    mv = ''
    for line in data:
        if line.startswith('#'):
            nline = []
            for c in line:
                if c == '#':
                    nline.append('#')
                    nline.append('#')
                elif c == '.':
                    nline.append('.')
                    nline.append('.')
                elif c == '@':
                    nline.append('@')
                    nline.append('.')
                elif c == 'O':
                    nline.append('[')
                    nline.append(']')
            dd.append(nline)
        elif len(line) > 0 and line[0] in '<>v^':
            mv = mv + line
    a = np.array(dd)
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
        if d[0] == 0:
            p1 = pn
            while a[p1] in '[]':
                p1 = (p1[0] + d[0], p1[1] + d[1])
            if a[p1] == '#':
                continue
            while p1 != pn:
                p2 = (p1[0] - d[0], p1[1] - d[1])
                a[p1] = a[p2]
                p1 = p2
            a[pn] = '.'
        else:
            p1 = pn
            p2 = pn
            if a[p1] == '[':
                p2 = (p1[0], p1[1] + 1)
            if a[p1] == ']':
                p1 = (p1[0], p1[1] - 1)
            pr = inNextRow(a, [p1, p2], d)
            push = []
            push.append([p1, p2])
            while pr != -1:
                if not pr:
                    break
                push.append(pr)
                pr = inNextRow(a, pr, d)
            if pr == -1:
                continue
            push = push[:-1]
            push.reverse()
            for pr in push:
                for p1 in pr:
                    v1 = a[p1]
                    if v1 not in '[]':
                        continue
                    q1 = (p1[0] + d[0], p1[1] + d[1])
                    a[q1] = v1
                    a[p1] = '.'
        p = pn

#    a[p] = '@'
#    for r in a:
#        print(''.join(r))
#    a[p] = '.'
    for x in range(nx):
        for y in range(ny):
            if a[x,y] == '[':
                total += 100 * x + y
    print(total)