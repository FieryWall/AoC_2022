import sys
import re

list_of_items_path = sys.argv[1]

list_of_items_file = open(list_of_items_path)
list_of_items_text = list_of_items_file.read()
list_of_items_file.close()

badges_priorities_sum = 0

def get_priority_of(char) -> int:
    char_code = ord(char)
    if char_code < ord('a'):
        return char_code - ord('A') + 27
    else:
        return char_code - ord('a') + 1

elves_group = []
for rucksack_items in re.finditer(r'\w+', list_of_items_text):
    rucksack_items_txt = rucksack_items.group(0)
    if len(elves_group) < 3:
        elves_group.append(rucksack_items_txt)
        if len(elves_group) < 3:
            continue
    
    group_badge = (set(elves_group[0]) & set(elves_group[1]) & set(elves_group[2])).pop()
    badges_priorities_sum += get_priority_of(group_badge)
    elves_group.clear()

sys.stdout.write(str(badges_priorities_sum))