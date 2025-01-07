import re
from collections import defaultdict

total = 0
p1 = re.compile(r"^p=(\d*),(\d*) v=(-?\d*),(-?\d*)")

with open('dag14input.txt', encoding='ascii' ) as fp:
    data = fp.read().strip().split('\n')
    rs = []
    for line in data:
        rs.append([int(g) for g in p1.match(line).groups()])
        
    nx = 101
    ny = 103
    nxb2 = nx // 2
    nyb2 = ny // 2
    
    for nt in range(20000):
        robots = set()
        for r in rs:
            x, y = ((r[0] + nt * r[2]) % nx, (r[1] + nt * r[3]) % ny)
            robots.add((x, y))
        if len(robots) == len(rs):
            total = nt
            break
            
    dd = defaultdict(list)
    for x, y in robots:
        dd[x].append(y)
    for k in sorted(dd):
        print(''.join(['+' if i in dd[k] else ' ' for i in range(ny)]))
    print(total)
                