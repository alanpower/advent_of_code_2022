from collections import Counter
f = open(r'C:\Users\alanp\git\advent_of_code_2022\advent_of_code_6_input.txt')
content = f.read()

i = 4
start_char = 1

while i < len(content) - 4:
    print(f'{i}\t{content[i-1]}\t{content[i-4:i-1]}')
    if len(Counter(content[i-4:i])) == 4:
        start_char = i
        break
        
    i = i + 1

print(f'Start char is {start_char}')