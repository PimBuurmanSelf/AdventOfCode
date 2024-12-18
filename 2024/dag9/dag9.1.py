total = 0
with open('dag9input.txt', encoding='ascii' ) as fp:
    data = fp.read()
    dm = []
    id0 = 0
    id1 = len(data) // 2
    ins = 0
    end = len(data) -1
    p = 0
    nEnd = int(data[end])
    end -= 2
    while id0 < id1:
        n = int(data[ins])
        for i in range(n):
            total += p * id0
            p += 1
        n = int(data[ins + 1])
        ins += 2
        id0 += 1
        i = 0
        while i < n:
            if nEnd <= 0:
                nEnd = int(data[end])
                end -= 2
                id1 -= 1
            total += p * id1
            p += 1
            i += 1
            nEnd -= 1
    while nEnd > 0:
        total += p * id1
        p += 1
        nEnd -= 1
        
print(total)