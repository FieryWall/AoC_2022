import sys
import re

rules = { 
    'A': ['Z', 'X', 'Y'],
    'B': ['X', 'Y', 'Z'],
    'C': ['Y', 'Z', 'X'],
}

win_scores = [0, 3, 6]
choice_scores = ['X', 'Y', 'Z']

def rock_paper_scissors(elf_choice: str, my_choice: str) -> int:
    result = rules[elf_choice].index(my_choice)
    return win_scores[result] + choice_scores.index(my_choice) + 1

input_path = sys.argv[1]

txt_file = open(input_path, "r")
content = txt_file.read()
txt_file.close()

score = 0
for groups in re.finditer(r'(?P<elf>[ABC]) (?P<me>[XYZ])', content):
    score += rock_paper_scissors(groups['elf'], groups['me'])

sys.stdout.write(str(score))