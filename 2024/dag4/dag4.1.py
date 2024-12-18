import numpy as np

def xmas(arr):
    n = 0
    for i in range(len(arr) - 3):
        if arr[i] == 'X' and arr[i+1] == 'M' and arr[i+2] == 'A' and arr[i+3] == 'S':
            n += 1
        if arr[i+3] == 'X' and arr[i+2] == 'M' and arr[i+1] == 'A' and arr[i] == 'S':
            n += 1
    return n
    
total = 0
ok = True
with open('dag4input.txt', encoding='ascii' ) as fp:
    data = fp.readlines()
    dd = []
    for line in data:
        dd.append([c for c in line.strip()])
    a = np.array(dd)
    #hor
    htotal = 0
    for r in a:
        htotal += xmas(r)
      
    #diag
    dtotal = 0
    for i in range(-a.shape[0], a.shape[0]):
        r = a.diagonal(i)
        dtotal += xmas(r)

    #vert
    b = np.rot90(a)
    vtotal = 0
    for r in b:
        vtotal += xmas(r)
        
    #transposed diag
    ptotal = 0
    nn = b.shape[0]
    for i in range(-b.shape[0], b.shape[0]):
        r = b.diagonal(i)
        ptotal += xmas(r)

    print(htotal, dtotal, vtotal, ptotal, htotal + dtotal + vtotal + ptotal)