import sys
import re

with open(sys.argv[1], 'r') as f:
    input_text = f.read()

MAX_SIZE = 100000

ls_counter = 0
path = '/'
current_folder = '/'
sizes_map = {'/': 0}
files = set()
limit = 10
for record in re.finditer(r'\$ cd (?P<cd>(\w+|\.\.))|(?P<size>\d+) (?P<file>[\w.]+)', input_text):
    dic = record.groupdict()

    cd_kind = dic["cd"]
    if cd_kind is not None:
        if cd_kind == "..":
            path = path[:-len(current_folder)-1]
            current_folder = path[path.rfind('/') + 1:]
        else:
            current_folder = cd_kind
            path += f"/{current_folder}"
            if path not in sizes_map:
                sizes_map[path] = 0
    elif dic["size"] is not None:
        file_path = f"{path}/{dic['file']}"
        if file_path not in files:
            files.add(file_path)
            for folder in sizes_map.keys():
                if folder in path:
                    sizes_map[folder] += int(dic["size"])

total_size = 0
for size in sizes_map.values():
    if size <= MAX_SIZE:
        total_size += size

sys.stdout.write(str(total_size))