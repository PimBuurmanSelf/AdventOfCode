import sys
total = 0
with open('dag9input.txt', encoding='ascii' ) as fp:
    data = fp.read()
    dm = []
    id0 = 0
    for i in range(len(data) // 2):
        dm.append((int(data[2*i]), id0))
        dm.append((int(data[2*i+1]), -1))
        id0 += 1
    dm.append((int(data[-1]), id0))
    
    last = 0
    i = len(dm) - 1
    while i > 0:
        n, v = dm[i]
        if n > 0 and v >= 0:
            for j in range(i):
                if dm[j][1] == -1 and dm[j][0] >= n:
                    last = i
                    dm[j] = (dm[j][0] - n, -1)
                    dm[i] = (n, -1)
                    if dm[j][0] == 0:
                        dm[j] = (n, v)
                    else:
                        dm.insert(j, (n, v))
                        i += 1
                    break
        i -= 1

    p = 0
    for i in range(len(dm)):
        n, v = dm[i]
        if v >= 0:
            for j in range(n):
                total += p * v
                p += 1
        else:
            p += n

    print(total)
