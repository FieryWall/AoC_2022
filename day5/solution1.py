import sys
import re

input_path = sys.argv[1]

input_file = open(input_path)
input_text = input_file.read()
input_file.close()

creates = []
stack_index = 0
for record in re.finditer(r'((?P<empty> {4})|\[(?P<create>\w)\]|(?P<newline>\n)|(?P<break>\d))', input_text):
    record_dic = record.groupdict()
    
    if record_dic["empty"] is not None:
        stack_index += 1
    elif record_dic["create"] is not None:
        while(len(creates) <= stack_index):
            creates.append([])
        creates[stack_index].insert(0, record["create"])
        stack_index += 1
    elif record_dic["newline"] is not None:
        stack_index = 0
    elif record_dic["break"] is not None:
        break

for record in re.finditer(r'move (?P<count>\d+) from (?P<position>\d+) to (?P<destination>\d+)', input_text):
    count, position, destination = [int(record[k]) for k in ("count", "position", "destination")]
    position -= 1
    destination -= 1

    while count > 0:
        create = creates[position].pop()
        creates[destination].append(create)
        count -= 1

sys.stdout.write(''.join([stack[-1] for stack in creates]))