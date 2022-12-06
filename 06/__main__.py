with open('./input', 'r') as f:
    inp = f.read()


def findseq(s, l):
    for i, _ in enumerate(s):
        if len(set(s[i:i+l])) == l:
            return i + l


print('part 1:', findseq(inp, 4))
print('part 2:', findseq(inp, 14))
