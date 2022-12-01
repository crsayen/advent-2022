with open('./input', 'r') as f:
    elves = [[]]
    for line in f:
        if line == '\n':
            elves.append([])
        else:
            elves[-1].append(int(line.strip()))

srtd = sorted([sum(elf) for elf in elves])
print('part 1:', srtd[-1])
print('part 2:', sum(srtd[-1:-4:-1]))
