f = open(r'C:\Users\alanp\git\advent_of_code_2022\advent_of_code_8_input.txt')
content = f.readlines()

i = 0
scenic_scores = []
for line in content:
    line = line.replace('\n', '')
    j = 0
    while j <= len(line) - 1:
        visible_to_left = 0
        visible_to_top = 0
        visible_to_right = 0
        visible_to_bottom = 0
        current_tree_size = content[i][j]
        for k in range(i-1, -1, -1): # go up from current tree to edge
            visible_to_top = visible_to_top + 1
            if content[k][j] >= current_tree_size:
                break
        for k in range(j-1, -1, -1): # go left from current tree to edge
            visible_to_left = visible_to_left + 1
            if content[i][k] >= current_tree_size:
                break
        for k in range(i+1, len(content), 1): # go down from current tree to edge
            visible_to_bottom = visible_to_bottom + 1
            if content[k][j] >= current_tree_size:
                break
        for k in range(j+1, len(line), 1): # go right from current tree to edge
            visible_to_right = visible_to_right + 1
            if content[i][k] >= current_tree_size:
                break
        scenic_score = visible_to_top * visible_to_bottom * visible_to_left * visible_to_right
        scenic_scores.append(scenic_score)
        j = j + 1
    i = i + 1

print(max(scenic_scores))