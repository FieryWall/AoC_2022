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

    grid[len(grid) - 1].append([int(ch)])
    visible += 1

H = 0

grid_len = len(grid)
for l in range(1, grid_len):
    line_len = len(grid[l])
    for c in range(1, line_len):
        current = grid[l][c]

best_scenic_score = 0
grid_len = len(grid)
for l in range(0, grid_len):
    line_len = len(grid[l])
    for c in range(0, line_len):
        current = grid[l][c]

        scenic_score = 1
        multiplier = 0
        for i in range(c - 1, -1, -1):
            t = grid[l][i]
            multiplier += 1
            if t[H] >= current[H]:
                break
        if multiplier > 0:
            scenic_score *= multiplier

        multiplier = 0
        for i in range(c + 1, line_len):
            t = grid[l][i]
            multiplier += 1
            if t[H] >= current[H]:
                break
        if multiplier > 0:
            scenic_score *= multiplier

        multiplier = 0
        for i in range(l - 1, -1, -1):
            t = grid[i][c]
            multiplier += 1
            if t[H] >= current[H]:
                break
        if multiplier > 0:
            scenic_score *= multiplier

        multiplier = 0
        for i in range(l + 1, grid_len):
            t = grid[i][c]
            multiplier += 1
            if t[H] >= current[H]:
                break
        if multiplier > 0:
            scenic_score *= multiplier

        if scenic_score > best_scenic_score:
            best_scenic_score = scenic_score

sys.stdout.write(str(best_scenic_score))