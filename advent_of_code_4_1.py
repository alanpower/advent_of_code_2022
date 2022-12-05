f = open(r'C:\Users\alanp\Documents\python\advent_of_code_4_input.txt')
content = f.readlines()

fully_contains = []
for line in content:
    line = line.replace('\n', '')
    assignments = line.split(',')
    assignment_one = assignments[0].split('-')
    assignment_two = assignments[1].split('-')
    if ((int(assignment_one[0]) <= int(assignment_two[0]) and int(assignment_one[1]) >= int(assignment_two[1])) 
            or (int(assignment_two[0]) <= int(assignment_one[0]) and int(assignment_two[1]) >= int(assignment_one[1]))):
        fully_contains.append(line)
        print(f'{assignment_one[0]}\t{assignment_one[1]}\t{assignment_two[0]}\t{assignment_two[1]}')

print(len(fully_contains))

