import sys;
import re;

input_path = sys.argv[1]

txt_file = open(input_path, "r")
content = txt_file.read()
txt_file.close()
maxCalories = 0
for txt_report in re.findall(r'(?>\d+\n)+', content):
    calories = 0
    for txt_number in re.findall(r'\d+', txt_report):
        calories += int(txt_number)
    maxCalories = max(maxCalories, calories)

sys.stdout.write(str(maxCalories))