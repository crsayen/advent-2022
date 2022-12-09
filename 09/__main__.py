with open('./input', 'r') as f:
    lines = [line[:-1] for line in f]
    pl = [line.split(' ') for line in lines]
    moves = [[d.lower(), int(m)] for d, m in pl]

tx = {
    'r': [1, 0],
    'l': [-1, 0],
    'u': [0,-1],
    'd': [0, 1]
}

def add(a, b):
    return [a[0] + b[0], a[1] + b[1]]

def delta(a, b):
    return [b[0] - a[0], b[1] - a[1]]

def mv(t, h2):
    t2 = t
    dx, dy = delta(t, h2)
    if dx != 0 and dy != 0:
        if abs(dx) + abs(dy) > 2:
            if abs(dx) > 1:
                dx = 1 % dx
            if abs(dy) > 1:
                dy = 1 % dy
            t2 = add(t, [dx, dy])
    if dx == 0 or dy == 0:
        if abs(dx) + abs(dy) > 1:
            if dx:
                dx = 1 % dx
            if dy:
                dy = 1 % dy
            t2 = add(t, [dx, dy])
    return t2, h2


knots = {i: [0,0] for i in range(10)}
visits1 = set()
visits2 = set()

for d, m in moves:
    for i in range(m):
        knots[9] = add(knots[9], tx[d])
        for kn in range(8, -1, -1):
            knots[kn], knots[kn + 1] = mv(knots[kn], knots[kn + 1])
        visits1.add(f'{knots[8]}')
        visits2.add(f'{knots[0]}')
        
print('part 1:', len(visits1))
print('part 2:', len(visits2))