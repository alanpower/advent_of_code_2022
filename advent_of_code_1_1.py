f = open(r'C:\Users\alanp\Documents\python\advent_of_code_1_input.txt')
content = f.readlines()

elf_list = []
current_elf_total = 0
for line in content:
    if line != "\n":
        current_elf_total = current_elf_total + int(line)
    else:
        elf_list.append(current_elf_total)
        current_elf_total = 0

heaviest = max(elf_list)
print(heaviest)