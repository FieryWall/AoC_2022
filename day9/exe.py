import sys
from pathlib import Path

exe_path = sys.argv[0]
day_folder = Path(exe_path).parent

INPUT_NAME = 'series_of_motions.txt'

input_path = Path(day_folder, INPUT_NAME)
solution_1_path = Path(day_folder, 'solution1.py')
sys.argv = [solution_1_path.as_posix(), input_path.as_posix()]
exec(open(solution_1_path).read())

sys.stdout.write(', ')

input_path = Path(day_folder, INPUT_NAME)
solution_2_path = Path(day_folder, 'solution2.py')
sys.argv = [solution_2_path.as_posix(), input_path.as_posix()]
exec(open(solution_2_path).read())