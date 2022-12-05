f = open(r'C:\Users\alanp\Documents\python\advent_of_code_2_input.txt')
content = f.readlines()

choice_dict = { "X": 1, "Y": 2, "Z": 3 }
game_score_dict = { "AX": 3, "BX": 0, "CX": 6, "AY": 6, "BY": 3, "CY": 0, "AZ": 0, "BZ": 6, "CZ": 3}
my_choice_dict = { "AX": "Z", "BX": "X", "CX": "Y", "AY": "X", "BY": "Y", "CY": "Z", "AZ": "Y", "BZ": "Z", "CZ": "X"}
game_scores = []

for line in content:
    choices = line.split(' ')
    opponent_choice = choices[0]
    game_outcome = choices[1].replace('\n','')
    my_choice = my_choice_dict[opponent_choice + game_outcome]
    choice_score = choice_dict[my_choice]
    combined_choice = opponent_choice + my_choice
    game_score = game_score_dict[combined_choice]
    game_scores.append(choice_score + game_score)

print(sum(game_scores))
