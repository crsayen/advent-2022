xtoa = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

wtol = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

ltow = {v: k for (k, v) in wtol.items()}


def shapescore(s):
    return ['A', 'B', 'C'].index(s) + 1


def fromresult(me, opp):
    return {
        'X': wtol[opp],
        'Y': opp,
        'Z': ltow[opp]
    }.get(me)


def roundscore(me, opp):
    return 3 if me == opp else 0 if ltow[me] == opp else 6


def totalscore(me, opp):
    return shapescore(me) + roundscore(me, opp)


with open('./input', 'r') as f:
    p1total = 0
    p2total = 0
    for line in f:
        opp, me = line.strip().split(' ')
        p1total += totalscore(xtoa[me], opp)
        p2total += totalscore(fromresult(me, opp), opp)


print('part 1:', p1total)
print('part 2:', p2total)
