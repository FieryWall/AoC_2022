import sys

COUNT_OF_UNIQUE = 14

with open(sys.argv[1], 'r') as f:
    input_text = f.read()

i = 0
while i < len(input_text):
    chars_set = set(input_text[i:i+COUNT_OF_UNIQUE])
    if(len(chars_set) == COUNT_OF_UNIQUE):
        break
    i += 1
    
sys.stdout.write(str(i + COUNT_OF_UNIQUE))