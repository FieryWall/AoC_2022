import sys
import re

blotsafep_path = sys.argv[1]

blotsafep_file = open(blotsafep_path)
blotsafep_text = blotsafep_file.read()
blotsafep_file.close()

range_regex = r'(?P<from>\d+)-(?P<to>\d+)'
def get_elf_range(elf_record):
    elf_a_range = re.match(range_regex, elf_record)
    return [int(elf_a_range[k]) for k in ('from', 'to')]

fully_overlaped_count = 0

for pair in re.finditer(r'(?P<elf_a>\d+-\d+),(?P<elf_b>\d+-\d+)', blotsafep_text):

    f, t = get_elf_range(pair['elf_a'])
    elf_a_range = set(range(f, t + 1))
    f, t = get_elf_range(pair['elf_b'])
    elf_b_range = set(range(f, t + 1))
    
    if elf_a_range & elf_b_range:
        fully_overlaped_count += 1

sys.stdout.write(str(fully_overlaped_count))