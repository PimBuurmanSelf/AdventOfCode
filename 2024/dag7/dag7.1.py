total = 0
with open('dag7input.txt', encoding='ascii' ) as fp:
    for line in fp:
        t = int(line.split(':')[0])
        f = [int(i) for i in line.split()[1:]]
        v = [f[0]]
        for i in range(1, len(f)):
            nv = []
            for x in v:
                nv.append(x * f[i])
                nv.append(x + f[i])
            v = nv
        if t in v:
            total += t

print(total)