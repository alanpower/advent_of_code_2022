f = open(r'C:\Users\alanp\git\advent_of_code_2022\advent_of_code_8_input.txt')
content = f.readlines()

i = 0
num_visible = 0
for line in content:
    line = line.replace('\n', '')
    j = 0
    while j <= len(line) - 1:
        visible_from_left = True
        visible_from_top = True
        visible_from_right = True
        visible_from_bottom = True
        if i == 0 or j == 0 or i == len(content) - 1 or j == len(line) - 1: # edge trees are visible
            num_visible = num_visible + 1
        else:
            current_tree_size = content[i][j]
            for k in range(i-1, -1, -1): # go up from current tree to edge
                if content[k][j] >= current_tree_size:
                    visible_from_top = False
                    break
            for k in range(j-1, -1, -1): # go left from current tree to edge
                if content[i][k] >= current_tree_size:
                    visible_from_left = False
                    break
            for k in range(i+1, len(content), 1): # go down from current tree to edge
                if content[k][j] >= current_tree_size:
                    visible_from_bottom = False
                    break
            for k in range(j+1, len(line), 1): # go right from current tree to edge
                if content[i][k] >= current_tree_size:
                    visible_from_right = False
                    break
            if visible_from_top or visible_from_bottom or visible_from_left or visible_from_right:
                num_visible = num_visible + 1
        j = j + 1
    i = i + 1

print(num_visible)