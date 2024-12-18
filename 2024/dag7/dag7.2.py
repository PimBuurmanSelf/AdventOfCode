import math
total = 0
        
with open('dag7input.txt', encoding='ascii' ) as fp:
    for line in fp:
        t = int(line.split(':')[0])
        f = [int(i) for i in line.split()[1:]]
        v = [f[0]]
        for i in range(1, len(f)):
            nv = []
            for x in v:
                y = x * f[i]
                if y <= t: nv.append(y)
                y = x + f[i]
                if y <= t: nv.append(y)
                p = math.floor(math.log10(f[i])) + 1
                y = x * math.floor(math.pow(10, p)) + f[i]
                if y <= t: nv.append(y)
            v = nv
        if t in v:
            total += t

print(total)