with open('./input', 'r') as f:
    input = [line[:-1] for line in f]

inst = []
for line in input:
    if line == 'noop':
        inst.append([1, 0])
    else:
        inst.append([2, int(line.split(' ')[1])])


def getXpos(n): return n % 40

def getYpos(n): return n // 40

def isLit(x, clock):
    s = getXpos(clock)
    return x in [s - 2, s - 1, s]

screen = [['.'] * 40 for _ in range(6)]

clock = 0
x = 1
sum = 0

interesting = list(range(-20, 221, 40)[1:])

for instruction in inst:
    cycles, delta = instruction
    for cycle in range(cycles):
        clock += 1
        if isLit(x, clock):
            screen[getYpos(clock)][getXpos(clock) - 1] = '#'
        if clock in interesting:
            sum += x * clock
    x += delta

print('part 1:', sum)
print('part 2:')
print('\n'.join([''.join(row) for row in screen]))