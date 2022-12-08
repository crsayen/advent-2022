import dpath
max = 100000
disk = 70000000
needed = 30000000

with open('./input', 'r') as f:
    lines = [line[:-1] for line in f]

sizes = {}
counted = []
wd = ''
fs = {'root': {'_size': 0}}


def get(p):
    return dpath.get(fs, p)


def sets(p, v):
    dpath.new(fs, p, v)


def cd(p):
    global wd
    if p == '..':
        wd = '/'.join(wd.split('/')[:-1])
    elif p == '/':
        wd = 'root'
    else:
        wd = wd + '/' + p


def cont(p):
    a, b = p.split(' ')
    if a == 'dir':
        try:
            dpath.get(wd + '/' + b)
        except:
            sets(wd + '/' + b, {'_size': 0})
    else:
        if wd + '/' + b in counted:
            return
        counted.append(wd + '/' + b)
        recursiz(wd + '/' + p, int(a))


def recursiz(p, n):
    pth = 'root'
    for chnk in p.split('/')[1:]:
        sz = get(pth + '/_size') + n
        sets(pth + '/_size', sz)
        sizes[pth] = sz
        pth += '/' + chnk


for line in lines:
    if line == 'ls':
        continue
    if line.startswith('$ cd'):
        cd(line.split(' ')[2])
    elif line[0] == '$':
        continue
    else:
        cont(line)

total = 0
for k, v in sizes.items():
    if v <= max:
        total += v
print('part 1:', total)


for sois in sorted(sizes.values()):
    if sois >= needed - (disk - get('root/_size')):
        print('part 2:', sois)
        break