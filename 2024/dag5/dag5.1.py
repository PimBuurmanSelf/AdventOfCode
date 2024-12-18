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
            for i in range(len(f)):
                p = f[i]
                pre = f[:i]
                for q in rules.get(p, []):
                    if q in pre:
                        break
                else:
                    continue
                break
            else:
                total += f[len(f) // 2]
            
print(total)