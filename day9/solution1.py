import sys
import re

with open(sys.argv[1], 'r') as f:
    input_text = f.read()

class P:
    def __init__(self):
        self.x = 300
        self.y = 300

field = [[False for c in range(0, 600)] for l in range(0, 600)]
H = P()
T = P()

counter = 1
field[T.x][T.y] = True
for group in re.finditer(r"(?P<direction>\w) (?P<steps>\d+)", input_text):
    move = group.groupdict()
    direction = move["direction"]
    steps = int(move["steps"])
    
    if direction == "R":
        H.x += steps
    elif direction == "L":
        H.x -= steps
    elif direction == "D":
        H.y += steps
    elif direction == "U":
        H.y -= steps

    if abs(H.x - T.x) > 1:
        T.y = H.y
        sign = 1 if H.x > T.x else -1
        for T.x in range(T.x + sign, H.x, sign):
            if not field[T.y][T.x]:
                counter += 1
                field[T.y][T.x] = True

    elif abs(H.y - T.y) > 1:
        T.x = H.x
        sign = 1 if H.y > T.y else -1
        for T.y in range(T.y + sign, H.y, sign):
            if not field[T.y][T.x]:
                counter += 1
                field[T.y][T.x] = True

sys.stdout.write(f"{counter}")