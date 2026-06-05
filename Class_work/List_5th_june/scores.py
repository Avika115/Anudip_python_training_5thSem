#player score
player_score =[]
# input of score form user
for i in range(11):
    score = int(input("enter the score of player {}:"))
    player_score.append(score)

#display the scores of player
print("\n------Player Score-------")
print("score of 11 players",player_score)
#finding the highest score
max_score = player_score[0]
for index in range(1, len(player_score)):
    max_score = player_score[index]
print("The highest score is:", max_score)
