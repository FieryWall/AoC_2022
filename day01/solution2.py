import sys;
import re;

input_path = sys.argv[1]

txt_file = open(input_path, "r")
content = txt_file.read()
txt_file.close()

top_three = [0, 0, 0]
top_order = [0, 1, 2]

for txt_report in re.findall(r'(?>\d+\n)+', content):

    calories = 0
    for txt_number in re.findall(r'\d+', txt_report):
        calories += int(txt_number)

    for index in top_order:
        temporary_top_calories = top_three[index]
        if calories > temporary_top_calories:
            top_three[index] = calories
            top_order = [t[0] for t in sorted(enumerate(top_three), key=lambda t: t[1])]
            break

sys.stdout.write(str(sum(top_three)))