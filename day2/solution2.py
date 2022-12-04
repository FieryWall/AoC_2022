import sys
import re

rules = { 
    'A': ['Y', 'Z', 'X'],
    'B': ['X', 'Y', 'Z'],
    'C': ['Z', 'X', 'Y'],
}

scores = ['X', 'Y', 'Z']

def rock_paper_scissors(elf_choice: str, result: str) -> int:
    choice_score = rules[elf_choice].index(result)
    return scores.index(result) * 3 + choice_score + 1

input_path = sys.argv[1]

txt_file = open(input_path, "r")
content = txt_file.read()
txt_file.close()

score = 0
for groups in re.finditer(r'(?P<elf>[ABC]) (?P<result>[XYZ])', content):
    score += rock_paper_scissors(groups['elf'], groups['result'])

sys.stdout.write(str(score))