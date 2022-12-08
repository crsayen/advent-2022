import json

with open('./input', 'r') as f:
    tl = [[int(c) for c in r[:-1]] for r in f]

vis = set()


def getVis1d(s):
    mx = -1
    vals = []
    for i, x in enumerate(s):
        d = int(x)
        if d > mx:
            mx = d
            vals.append(i)
    return vals


def conv1d(s, other, xory, start, direction):
    vals = getVis1d(s)
    vals2d = []
    if xory == 'y':
        vals2d = [f'{start + (val * direction)},{other}' for val in vals]
    else:
        vals2d = [f'{other},{start + (val * direction)}' for val in vals]
    for e in vals2d:
        vis.add(e)


for y, row in enumerate(tl):
    conv1d(row, y, 'x', 0, 1)
    conv1d(row[::-1], y, 'x', len(row) - 1, -1)

for x, col in enumerate(list(zip(*tl[::-1]))):
    conv1d(col[::-1], x, 'y', 0, 1)
    conv1d(col, x, 'y', len(col) - 1, -1)

print('part 1:', len(vis))


def getHeight(x, y):
    return tl[y][x]


def getYs(x, y, asc):
    e, d = (len(tl), 1) if asc else (-1, -1)
    if y == e:
        return []
    return [getHeight(x, yy) for yy in range(y + d, e, d)]


def getXs(x, y, asc):
    e, d = (len(tl[0]), 1) if asc else (-1, -1)
    if x == e:
        return []
    return [getHeight(xx, y) for xx in range(x + d, e, d)]

def getScore(x, y):
    prd = 1
    val = getHeight(x, y)
    for view in [*[getXs(x, y, b) for b in [True, False]],*[getYs(x, y, b) for b in [True, False]]]:
        i = 0
        for tree in view:
            i += 1
            if tree >= val: break
        prd *= i
    return prd

highest = -1
for x in range(len(tl[0])):
    for y in range(len(tl)):
        score = getScore(x,y)
        if score > highest:
            highest = score

print('part 2:', highest)