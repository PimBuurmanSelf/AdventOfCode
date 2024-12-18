import re
import numpy as np

total = 0
p1 = re.compile(r"^Button .: X\+(\d*), Y\+(\d*)")
p2 = re.compile(r"^Prize: X=(\d*), Y=(\d*)")

with open('dag13input.txt', encoding='ascii' ) as fp:
    data = fp.read().strip().split('\n')
    sc = []
    for i in range(len(data) // 4 + 1):
        r1 = [int(g) for g in p1.match(data[4*i]).group(1, 2)]
        r2 = [int(g) for g in p1.match(data[4*i+1]).group(1, 2)]
        t = [10000000000000 + int(g) for g in p2.match(data[4*i+2]).group(1, 2)]
        det = r1[0] * r2[1] - r1[1] * r2[0]
        va = -(r2[0] * t[1] - r2[1] * t[0]) / det
        var = int(va + 0.5)
        vb = (r1[0] * t[1] - r1[1] * t[0]) / det
        vbr = int(vb + 0.5)
        if va > 0 and vb > 0 and  va - var < 1e-7 and vb - vbr / 1e-7:
            sc.append(3*var + vbr)
    total = sum(sc)
    
    print(total)
                