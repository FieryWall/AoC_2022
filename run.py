import os
from pathlib import Path
import sys

days = os.listdir('puzzles')
for day in days:
    day_path = Path('puzzles', day)
    solution_path = Path(day_path, 'solution.py')
    input_path = Path(day_path, 'input.txt')
    sys.argv = [solution_path.as_posix(), input_path.as_posix()]
    exec(open(solution_path).read())