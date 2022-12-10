import sys
import re

with open(sys.argv[1], 'r') as f:
    input_text = f.read()

cycle = 0
l = 0
c = 0
X = 0
sys.stdout.write(f"       ")
for line in re.finditer(r"(?P<instruction>\w+) *(?P<value>[-|\d]+)*", input_text):
    group = line.groupdict()
    instruction = group["instruction"]
    value = int(group["value"]) if group["value"] is not None else 0
    
    for i in range(0, 2 if instruction == "addx" else 1):
        cycle += 1
        if c >= X and c <= X + 2:
            sys.stdout.write(f"#")
        else:
            sys.stdout.write(f" ")
        c += 1
        if l < 5 and cycle % 40 == 0:
            l += 1
            c = 0
            sys.stdout.write(f"\n       ")

    if instruction == "addx":
        X += value