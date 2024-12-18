total = 0
rules = {}
with open('dag5input.txt', encoding='ascii' ) as fp:
    data = fp.readlines()
    for line in data:
        if '|' in line:
            f = [int(i) for i in line.strip().split('|')]
            r = rules.get(f[0], [])
            r.append(f[1])
            rules[f[0]] = r
        if ',' in line:
            f = [int(i) for i in line.strip().split(',')]
            ok = True
            for i in range(len(f)):
                p = f[i]
                pre = f[:i]
                for q in rules.get(p, []):
                    if q in pre:
                        ok = False
                        break
                else:
                    continue
                break
                
            if not ok:
                a = {}
                for p in f:
                    a[p] = 0
                for p in f:
                    for q in rules.get(p, []):
                        if q in a:
                            a[q] += 1
                d = [(a[p], p) for p in f]
                d.sort()
                total += d[len(d) // 2][1]
                
            
print(total)