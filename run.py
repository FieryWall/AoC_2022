import os
import sys
from pathlib import Path

days = os.listdir('puzzles')
for day in days:
    exe_path = Path('puzzles', day, 'exe.py').absolute()
    if os.path.exists(exe_path):
        sys.argv = [exe_path.as_posix()]
        sys.stdout.write(day + ': ')
        exec(open(exe_path).read())
        sys.stdout.write('\n')
    else:
        print('\033[91m' + day + " folder doesn't include exe.py" + '\033[0m')