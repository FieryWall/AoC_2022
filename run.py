import os
import re
import sys
from pathlib import Path

items_names = os.listdir('.')
days_folders_list = []
for item_name in items_names:
    if os.path.isdir(item_name):
        r = re.findall(r'day(?P<num>\d+)', item_name)
        if len(r):
            days_folders_list.append(int(r[0]))

days_folders_list = [f"day{n}" for n in sorted(days_folders_list)]

for day_folder in days_folders_list:
    exe_path = Path(day_folder, 'exe.py').absolute()
    if os.path.exists(exe_path):
        sys.argv = [exe_path.as_posix()]
        sys.stdout.write(day_folder + ': ')
        exec(open(exe_path).read())
        sys.stdout.write('\n')
    else:
        print('\033[91m' + exe_path + " folder doesn't include exe.py" + '\033[0m')