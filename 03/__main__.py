def getp(ch):
    alpha = ''.join([chr(i) for i in range(97, 97 + 26)])
    p = '.' + alpha + alpha.upper()
    return p.index(ch)


with open('./input', 'r') as f:
    packl = list([list(line.strip()) for line in f])


sum1 = 0
for pack in packl:
    s = len(pack) // 2
    sum1 += getp((set(pack[:s]) & set(pack[s:])).pop())

print('part 1:', sum1)


sum2 = 0
for i in range(0, len(packl), 3):
    a, b, c = [set(p) for p in packl[i:i+3]]
    sum2 += getp((a & b & c).pop())


print('part 2:', sum2)
