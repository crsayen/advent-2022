contain = 0
overlap = 0


with open('./input', 'r') as f:
    for line in f:
        print(line)
        A, B = [[int(ch) for ch in h.split('-')] for h in line.strip().split(',')]       

        al = list(range(A[0], A[1] + 1))
        bl = list(range(B[0], B[1] + 1))
        if len(set([*al, *bl])) == max([len(al), len(bl)]):
            contain += 1
        if len(set(al) & set(bl)):
            overlap += 1

print('part 1:', contain)
print('part 2:', overlap)
