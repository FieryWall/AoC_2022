import sys
import re
import json

with open(sys.argv[1], 'r') as f:
    input_text = f.read()

def compare(l, r) -> int:
    for i in range(0, len(l)):
        if i == len(r):
            return -1

        if type(l[i]) == int and type(r[i]) == int:
            if l[i] < r[i]:
                return 1
            elif l[i] > r[i]:
                return -1
            continue

        ll = [l[i]] if type(l[i]) == int else l[i]
        rl = [r[i]] if type(r[i]) == int else r[i]
        c = compare(ll, rl)
        if c != 0:
            return c

    if len(l) == len(r):
        return 0
    return 1

pair = 0
sum = 0
rx = r"(?P<left>(\d|\[|\]|,)+)\n(?P<right>(\d|\[|\]|,)+)"
for group in re.finditer(rx, input_text):
    pair += 1
    dict = group.groupdict()
    l = json.loads(dict["left"])
    r = json.loads(dict["right"])
    if compare(l, r) > -1:
        sum += pair
            
sys.stdout.write(f"{sum}")