from collections import defaultdict

total = 0
#problem = ('dag23ainput.txt', 2000)
problem = ('dag23input.txt', 2000)
nSteps = problem[1]
with open(problem[0], encoding='ascii' ) as fp:
    data = fp.read().strip().split('\n')
    conns = [line.split('-') for line in data]
    
    gr = defaultdict(set)
    
    for n1, n2 in conns:
        gr[n1].add(n2)
        gr[n2].add(n1)
        
    grp = set()
    for n1, n2 in conns:
        g1 = gr[n1]
        for n3 in gr[n2]:
            if n3 in g1:
                p = sorted([n1, n2, n3])
                grp.add(tuple(p))
     
    while len(grp) > 1:
        ngrp = set()
        for gs in grp:
            for k in gr:
                if not k in gs:
                    for n in gs:
                        if not n in gr[k]:
                            break
                    else:
                        p = sorted(list(gs) + [k])
                        ngrp.add(tuple(p))
        grp = ngrp
    
    for g in grp:
        total = ','.join(sorted(list(g)))
        break
    print(total)
    
