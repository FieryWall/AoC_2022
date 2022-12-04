import os
import re
import sys
from pathlib import Path

items_names = os.listdir('.')
for item_name in items_names:
    if os.path.isdir(item_name) and re.search(r'day\d', item_name):
        exe_path = Path(item_name, 'exe.py').absolute()
        if os.path.exists(exe_path):
            sys.argv = [exe_path.as_posix()]
            sys.stdout.write(item_name + ': ')
            exec(open(exe_path).read())
            sys.stdout.write('\n')
        else:
            print('\033[91m' + day + " folder doesn't include exe.py" + '\033[0m')