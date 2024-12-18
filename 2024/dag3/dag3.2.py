import re
patt = re.compile(r"ul\((\d{1,3}),(\d{1,3})\)")
dp = re.compile(r"(do(n't)?\(\))")
total = 0
ok = True
with open('dag3input.txt', encoding='ascii' ) as fp:
    data = fp.read()
    f = data.split('m')
    for p in f:
        r = patt.match(p)
        if r != None and ok:
            v1 = int(r.group(1))
            v2 = int(r.group(2))
            total += v1 * v2
        m = dp.split(p)
        if None in m[-3:]:
            ok = True
        if "n't" in m[-3:]:
            ok = False
            
print(total)