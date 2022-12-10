import sys
import re

with open(sys.argv[1], 'r') as f:
    input_text = f.read()

SYS_SIZE = 70000000
UPDATE_SIZE = 30000000

ls_counter = 0
path = 'root'
current_folder = 'root'
sizes_map = {'root': 0}
files = set()
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

root_size = sizes_map['root']
free_space = SYS_SIZE - root_size
required_space = UPDATE_SIZE - free_space
best_candidate = root_size
best_size = root_size
for size in sizes_map.values():
    oversize = size - required_space
    if oversize > 0 and oversize < best_candidate:
        best_candidate = oversize
        best_size = size

sys.stdout.write(str(best_size))