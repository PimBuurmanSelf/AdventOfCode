import numpy as np
    
def mas(a, i, j):
    if a[i, j] != 'A':
        return 0
    d1 = (a[i-1, j-1] == 'M' and a[i+1, j+1] == 'S') or (a[i-1, j-1] == 'S' and a[i+1, j+1] == 'M')
    d2 = (a[i+1, j-1] == 'M' and a[i-1, j+1] == 'S') or (a[i+1, j-1] == 'S' and a[i-1, j+1] == 'M')
    if d1 and d2:
        return 1
    return 0
    
total = 0
ok = True
with open('dag4input.txt', encoding='ascii' ) as fp:
    data = fp.readlines()
    dd = []
    for line in data:
        dd.append([c for c in line.strip()])
    a = np.array(dd)
    
    for i in range(1, a.shape[0] - 1):
        for j in range(1, a.shape[1] - 1):
            total += mas(a, i, j)

    print(total)