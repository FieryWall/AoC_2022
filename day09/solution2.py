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
TS = [P() for t in range(1, 10)]

counter = 1
field[H.x][H.y] = True
for group in re.finditer(r"(?P<direction>\w) (?P<steps>\d+)", input_text):
    move = group.groupdict()
    direction = move["direction"]
    steps = int(move["steps"])
    
    while steps > 0:
        if direction == "R":
            H.x += 1
        elif direction == "L":
            H.x -= 1
        elif direction == "D":
            H.y += 1
        elif direction == "U":
            H.y -= 1
        steps -= 1

        F = H
        for i in range(0, len(TS)):
            T = TS[i]
            if abs(F.x - T.x) > 1:
                T.x += 1 if F.x > T.x else -1
                if abs(F.y - T.y) > 0:
                    T.y += 1 if F.y > T.y else -1

            elif abs(F.y - T.y) > 1:
                T.y += 1 if F.y > T.y else -1
                if abs(F.x - T.x) > 0:
                    T.x += 1 if F.x > T.x else -1
            
            if i == len(TS) - 1 and not field[T.y][T.x]:
                counter += 1
                field[T.y][T.x] = True
            F = T

sys.stdout.write(f"{counter}")