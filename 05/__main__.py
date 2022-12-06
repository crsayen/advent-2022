from copy import deepcopy
crates = [[],[],[],[],[],[],[],[],[]]

with open('./input', 'r') as fe:
    content = fe.read()
    
top, bot = [x.split('\n')[:-1] for x in content.split('\n\n')]

for l in top:
    for i in range(9):
        cargo = l[i * 4 + 1]
        if cargo != ' ': crates[i].append(cargo)
        
crates2 = deepcopy(crates)

for l in bot:
    a,b = l.split(' from ')
    f,t = b.split(' to ')
    m = a.split(' ')[1]
    m,f,t = [int(h) - 1 for h in (m,f,t)]
    stuff = [crates[f].pop(0) for _ in range(m+1)][::-1]
    stuff2 = [crates2[f].pop(0) for _ in range(m+1)]
    crates[t] = [*stuff, *crates[t]]
    crates2[t] = [*stuff2, *crates2[t]]

print('part 1:', ''.join([c[0] for c in crates]))
print('part 2:', ''.join([a[0] for a in crates2]))
                