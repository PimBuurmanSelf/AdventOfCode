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
    nt = 100
    newpos = [((r[0] + nt * r[2]) % nx, (r[1] + nt * r[3]) % ny) for r in rs]
    q1 = [(x, y) for x, y in newpos if x < nxb2 and y < nyb2]
    q2 = [(x, y) for x, y in newpos if x < nxb2 and y > nyb2]
    q3 = [(x, y) for x, y in newpos if x > nxb2 and y < nyb2]
    q4 = [(x, y) for x, y in newpos if x > nxb2 and y > nyb2]
    
    total = len(q1) * len(q2) * len(q3) * len(q4)
    print(total)
                