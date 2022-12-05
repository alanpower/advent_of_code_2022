f = open(r'C:\Users\alanp\Documents\python\advent_of_code_5_input.txt')
content = f.readlines()

stacks = [
            ["D", "T", "W", "F", "J", "S", "H", "N"],
            ["H", "R", "P", "Q", "T", "N", "B", "G"],
            ["L", "Q", "V"],
            ["N", "B", "S", "W", "R", "Q"],
            ["N", "D", "F", "T", "V", "M", "B"],
            ["M", "D", "B", "V", "H", "T", "R"],
            ["D", "B", "Q", "J"],
            ["D", "N", "J", "V", "R", "Z", "H", "Q"],
            ["B", "N", "H", "M", "S"]
         ]

for line in content:
    line = line.replace('\n', '')
    words = line.split(' ')
    crates_to_move = int(words[1])
    stack_from = int(words[3]) - 1
    stack_to = int(words[5]) - 1
    i = 0
    crates = []
    while i < crates_to_move:
        crates.append(stacks[stack_from].pop())
        print(crates)
        i = i + 1
    crates.reverse()
    for crate in crates:
        stacks[stack_to].append(crate)

top_crates=[]
for stack in stacks:
    top_crates.append(stack.pop())

print(top_crates)
