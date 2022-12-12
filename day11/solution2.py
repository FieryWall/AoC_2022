import math
import re
import sys

with open(sys.argv[1], 'r') as f:
    input_text = f.read()

class Monkey:
    def __init__(self, id, items, operation_params, denominator):
        self.id = id
        self.items = items
        self.a = operation_params[0]
        self.b = operation_params[2]
        self.s = operation_params[1]
        self.den = denominator

        self.monkey_true: Monkey = None
        self.monkey_false: Monkey = None
        self.inspectations_amount = 0

def do_operation(monkey: Monkey, old: int) -> int:
    a = old if monkey.a == "old" else int(monkey.a)
    b = old if monkey.b == "old" else int(monkey.b)
    return a + b if monkey.s == "+" else a * b

monkeys = []
relations = []
monkey_rx = r"""Monkey (?P<id>\d+):
  Starting items: (?P<items>(\d|,| )+)
  Operation: new = (?P<operand_a>old|\d+) (?P<sign>(\*|\+)) (?P<operand_b>old|\d+)
  Test: divisible by (?P<denominator>\d+)
    If true: throw to monkey (?P<monkey_true>\d+)
    If false: throw to monkey (?P<monkey_false>\d+)"""
for group in re.finditer(monkey_rx, input_text):
    dict = group.groupdict()

    monkeys.append(Monkey(
        dict["id"],
        [int(n) for n in re.findall(r"\d+", dict["items"])],
        (dict["operand_a"], dict["sign"], dict["operand_b"]),
        int(dict["denominator"])
    ))
    relations.append((int(group["monkey_true"]), int(group["monkey_false"])))

for i in range(0, len(relations)):
    ralation = relations[i]
    monkeys[i].monkey_true = monkeys[ralation[0]]
    monkeys[i].monkey_false = monkeys[ralation[1]]

round = 0
while round < 10000:
    pr = math.prod([m.den for m in monkeys])
    for monkey in monkeys:
        for worry_level in monkey.items:
            monkey.inspectations_amount += 1
            worry_level = do_operation(monkey, worry_level)
            worry_level = worry_level % pr
            if worry_level % monkey.den == 0:
                monkey.monkey_true.items.append(worry_level)
            else:
                monkey.monkey_false.items.append(worry_level)
        monkey.items.clear()
    round += 1

first_active = 0
second_active = 0
for monkey in monkeys:
    if first_active < second_active and monkey.inspectations_amount > first_active:
        first_active = monkey.inspectations_amount
    elif monkey.inspectations_amount > second_active:
        second_active = monkey.inspectations_amount

sys.stdout.write(str(first_active * second_active))