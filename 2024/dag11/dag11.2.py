import math
import functools

total = 0

@functools.cache
def doit(s, n):
    if n == 0:
        return 1
    n -= 1
    if s == 0:
        return doit(1, n)
    p = math.floor(math.log10(s)) + 1
    if p % 2 == 0:
        f = int(math.pow(10, p // 2))
        v1 = s // f
        return doit(v1, n) + doit(s - v1 * f, n)
    return doit(2024 * s, n)
    


with open('dag11input.txt', encoding='ascii' ) as fp:
    data = [int(v) for v in fp.read().split()]
    cache = {}
    for d in data:
        total += doit(d, 75)
    
    print(total)
                