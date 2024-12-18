total = 0
with open('dag2input.txt', encoding='ascii' ) as fp:
    for line in fp:
        flds = [int(i) for i in line.split()]
        if len(flds) > 1:
            s = flds[0] - flds[1]
            old = flds[0]
            for i in range(len(flds) - 1):
                new = flds[i+1]
                if (old - new) * s <= 0 or abs(old - new) > 3:
                    break
                else:
                    old = new
            else:
                total += 1

print(total)