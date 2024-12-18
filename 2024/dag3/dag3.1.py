import re
patt = re.compile(r"ul\((\d{1,3}),(\d{1,3})\)")
total = 0
with open('dag3input.txt', encoding='ascii' ) as fp:
    data = fp.read()
    f = data.split('m')
    for p in f:
        r = patt.match(p)
        if r != None:
            v1 = int(r.group(1))
            v2 = int(r.group(2))
            total += v1 * v2
            
print(total)