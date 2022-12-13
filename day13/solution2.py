import sys
import re
import json
import functools

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
pairs = []
rx = r"(?P<left>(\d|\[|\]|,)+)\n(?P<right>(\d|\[|\]|,)+)"
for group in re.finditer(rx, input_text):
    pair += 1
    dict = group.groupdict()
    pairs.append(json.loads(dict["left"]))
    pairs.append(json.loads(dict["right"]))

devider_a = [[2]]
devider_b = [[6]]
pairs.append(devider_a)
pairs.append(devider_b)

pairs = sorted(pairs, key=functools.cmp_to_key(compare), reverse=True)
decoder_key = (pairs.index(devider_a) + 1) * (pairs.index(devider_b) + 1)

sys.stdout.write(f"{decoder_key}")