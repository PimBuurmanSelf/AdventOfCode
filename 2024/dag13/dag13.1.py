import re

total = 0
p1 = re.compile(r"^Button .: X\+(\d*), Y\+(\d*)")
p2 = re.compile(r"^Prize: X=(\d*), Y=(\d*)")

with open('dag13input.txt', encoding='ascii' ) as fp:
    data = fp.read().strip().split('\n')
    sc = []
    for i in range(len(data) // 4 + 1):
        r1 = [int(g) for g in p1.match(data[4*i]).group(1, 2)]
        r2 = [int(g) for g in p1.match(data[4*i+1]).group(1, 2)]
        t = [int(g) for g in p2.match(data[4*i+2]).group(1, 2)]
        for v1 in range(1, 101):
            s1, s2 = t[0] - v1 * r1[0], t[1] - v1 * r1[1]
            if s1 % r2[0] == 0 and s2 % r2[1] == 0 and s1 // r2[0] == s2 // r2[1]:
                if s1 // r2[0] <= 100:
                    sc.append(3 * v1 + s1 // r2[0])
                break
    total = sum(sc)
    
    print(total)
                