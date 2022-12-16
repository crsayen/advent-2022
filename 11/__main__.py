import json
import math
partone = False
infile = './input'
# infile = './example'


def factors(x):
    return [i for i in range(1, x + 1) if x % i == 0]


def parse_operation(operation):
    operation = operation.replace('Operation: new = old ', '')
    return lambda old: eval(f"{old} {operation}")


assert parse_operation('Operation: new = old * 3')(3) == 9


def parse_test(test, if_true, if_false):
    divisor = int(test.split('by ')[1])
    true_monkey, false_monkey = [int(x.split('monkey ')[1])
                                 for x in [if_true, if_false]]
    return lambda x: false_monkey if x % divisor else true_monkey


test_true = parse_test('Test: divisible by 20',
                       'If true: throw to monkey 1', 'If false: throw to monkey 2')(40)
test_false = parse_test('Test: divisible by 20',
                        'If true: throw to monkey 1', 'If false: throw to monkey 2')(39)
assert test_true == 1, f'expected 1, got {test_true}'
assert test_false == 2, f'expected 1, got {test_false}'


def parse_input_chunk(chunk):
    name_line, item_line, op_line, test_line, if_true, if_false = chunk.split(
        '\n')
    return (int(name_line.split(' ')[1][:-1]), {
        'items': [int(x) for x in item_line.split(': ')[1].split(', ')],
        'operation': parse_operation(op_line),
        'test': parse_test(test_line, if_true, if_false),
        'modulo': int(test_line.split('by ')[1]),
        'tally': 0
    })


test_chunk = '''Monkey 0:
  Starting items: 1, 2
  Operation: new = old * 2
  Test: divisible by 2
    If true: throw to monkey 1
    If false: throw to monkey 2'''

n, test_parsed = parse_input_chunk(test_chunk)
assert n == 0
assert test_parsed['items'] == [1, 2]
assert test_parsed['operation'](2) == 4
assert test_parsed['test'](3) == 2

with open(infile, 'r') as f:
    chunks = f.read().split('\n\n')
    monkeys = dict([parse_input_chunk(chunk) for chunk in chunks])

maxworry = math.prod([m['modulo'] for _, m in monkeys.items()])

for round in range(20 if partone else 10000):
    for n, stuff in monkeys.items():
        while stuff['items']:
            stuff['tally'] += 1
            item = stuff['items'].pop(0)
            item = stuff['operation'](item)
            if partone:
                item = item // 3
            item = item % maxworry
            target = stuff['test'](item)
            monkeys[target]['items'].append(item)

sorted_monkeys = sorted([m['tally'] for _, m in monkeys.items()], reverse=True)

print(f'part {1 if partone else 2}:', math.prod(sorted_monkeys[:2]))
