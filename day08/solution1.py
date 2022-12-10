import sys
import re

with open(sys.argv[1], 'r') as f:
    input_text = f.read()

visible = 0
grid = [[]]
for ch in input_text:
    if ch == '\n':
        grid.append([])
        continue

    grid[len(grid) - 1].append([int(ch), int(ch), int(ch), int(ch), int(ch)])
    visible += 1

H = 0
L = 1
T = 2
R = 3
B = 4

grid_len = len(grid)
for l in range(1, grid_len):
    line_len = len(grid[l])
    for c in range(1, line_len):
        current = grid[l][c]
        left = grid[l][c - 1]
        top = grid[l - 1][c]

        current[L] = current[L] if left[L] < current[H] else left[L] 
        current[T] = current[T] if top[T] < current[H] else top[T]

grid_len = len(grid)
for l in range(grid_len - 2, 0, -1):
    line_len = len(grid[l])
    for c in range(line_len - 2, 0, -1):
        current = grid[l][c]
        left = grid[l][c - 1]
        top = grid[l - 1][c]
        right = grid[l][c + 1]
        bot = grid[l + 1][c]
 
        current[R] = current[R] if right[R] < current[H] else right[R]
        current[B] = current[B] if bot[B] < current[H] else bot[B]

        if current[L] <= left[L] and current[T] <= top[T] and current[R] <= right[R] and current[B] <= bot[B]:
            visible -= 1

sys.stdout.write(str(visible))