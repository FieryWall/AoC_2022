import sys
import re

with open(sys.argv[1], 'r') as f:
    input_text = f.read()

checkpoints = [i for i in range(20, 260, 40)]

X = 1
cycle = 0
signal_strength = 0
for line in re.finditer(r"(?P<instruction>\w+) *(?P<value>[-|\d]+)*", input_text):
    group = line.groupdict()
    instruction = group["instruction"]
    value = int(group["value"]) if group["value"] is not None else 0
    
    for i in range(0, 2 if instruction == "addx" else 1):
        cycle += 1
        if cycle in checkpoints:
            signal_strength += cycle * X

    if instruction == "addx":
        X += value
    

sys.stdout.write(f"{signal_strength}")