# input = [
#     'addx 15',
#     'addx -11',
#     'addx 6',
#     'addx -3',
#     'addx 5',
#     'addx -1',
#     'addx -8',
#     'addx 13',
#     'addx 4',
#     'noop',
#     'addx -1',
#     'addx 5',
#     'addx -1',
#     'addx 5',
#     'addx -1',
#     'addx 5',
#     'addx -1',
#     'addx 5',
#     'addx -1',
#     'addx -35',
#     'addx 1',
#     'addx 24',
#     'addx -19',
#     'addx 1',
#     'addx 16',
#     'addx -11',
#     'noop',
#     'noop',
#     'addx 21',
#     'addx -15',
#     'noop',
#     'noop',
#     'addx -3',
#     'addx 9',
#     'addx 1',
#     'addx -3',
#     'addx 8',
#     'addx 1',
#     'addx 5',
#     'noop',
#     'noop',
#     'noop',
#     'noop',
#     'noop',
#     'addx -36',
#     'noop',
#     'addx 1',
#     'addx 7',
#     'noop',
#     'noop',
#     'noop',
#     'addx 2',
#     'addx 6',
#     'noop',
#     'noop',
#     'noop',
#     'noop',
#     'noop',
#     'addx 1',
#     'noop',
#     'noop',
#     'addx 7',
#     'addx 1',
#     'noop',
#     'addx -13',
#     'addx 13',
#     'addx 7',
#     'noop',
#     'addx 1',
#     'addx -33',
#     'noop',
#     'noop',
#     'noop',
#     'addx 2',
#     'noop',
#     'noop',
#     'noop',
#     'addx 8',
#     'noop',
#     'addx -1',
#     'addx 2',
#     'addx 1',
#     'noop',
#     'addx 17',
#     'addx -9',
#     'addx 1',
#     'addx 1',
#     'addx -3',
#     'addx 11',
#     'noop',
#     'noop',
#     'addx 1',
#     'noop',
#     'addx 1',
#     'noop',
#     'noop',
#     'addx -13',
#     'addx -19',
#     'addx 1',
#     'addx 3',
#     'addx 26',
#     'addx -30',
#     'addx 12',
#     'addx -1',
#     'addx 3',
#     'addx 1',
#     'noop',
#     'noop',
#     'noop',
#     'addx -9',
#     'addx 18',
#     'addx 1',
#     'addx 2',
#     'noop',
#     'noop',
#     'addx 9',
#     'noop',
#     'noop',
#     'noop',
#     'addx -1',
#     'addx 2',
#     'addx -37',
#     'addx 1',
#     'addx 3',
#     'noop',
#     'addx 15',
#     'addx -21',
#     'addx 22',
#     'addx -6',
#     'addx 1',
#     'noop',
#     'addx 2',
#     'addx 1',
#     'noop',
#     'addx -10',
#     'noop',
#     'noop',
#     'addx 20',
#     'addx 1',
#     'addx 2',
#     'addx 2',
#     'addx -6',
#     'addx -11',
#     'noop',
#     'noop',
#     'noop'
# ]

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
        print(clock, getXpos(clock), getYpos(clock - 1))
        if isLit(x, clock):
            screen[getYpos(clock)][getXpos(clock) - 1] = '#'
        if clock in interesting:
            print('cycle:', clock, '\tX:', x)
            sum += x * clock
    x += delta

print('part 1:', sum)
print('part 2:')
print('\n'.join([''.join(row) for row in screen]))