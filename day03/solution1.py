import sys
import re

list_of_items_path = sys.argv[1]

list_of_items_file = open(list_of_items_path)
list_of_items_text = list_of_items_file.read()
list_of_items_file.close()

errors_priorities_sum = 0

def get_priority_of(char) -> int:
    char_code = ord(char)
    if char_code < ord('a'):
        return char_code - ord('A') + 27
    else:
        return char_code - ord('a') + 1

for rucksack_items in re.finditer(r'\w+', list_of_items_text):
    rucksack_items_txt = rucksack_items.group(0)
    count_per_compartment = int(len(rucksack_items_txt) / 2)
    compartmentA = rucksack_items_txt[:count_per_compartment]
    compartmentB = rucksack_items_txt[count_per_compartment:]
    error = (set(compartmentA) & set(compartmentB)).pop()
    errors_priorities_sum += get_priority_of(error)

sys.stdout.write(str(errors_priorities_sum))