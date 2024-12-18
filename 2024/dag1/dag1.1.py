total = 0
with open('dag1input.txt', encoding='ascii' ) as fp:
    r1 = []
    r2 = []
    for line in fp:
        flds = line.split()
        r1.append(int(flds[0]))
        r2.append(int(flds[1]))
    r1.sort()
    r2.sort()
    total = sum([abs(r2[i] - r1[i]) for i in range(len(r1))])
    print(total)