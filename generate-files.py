import os

for i in range(1, 26):
    d = f'./{"" if i // 10 else 0}{i}'
    os.mkdir(d)
    with open(f'{d}/__main__.py', 'w') as f:
        f.write("with open('./input', 'r') as f:\n    lines = [l.strip() for l in f]")
