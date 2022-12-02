# rock paper scissors
# X Y Z
# 1 2 3
# lose draw win
# 0 3 6

winnings = [
    [3, 0, 6], # X, I play rock
    [6, 3, 0], # Y
    [0, 6, 3] # Z
    ]
# if I play rock (index 0), I get 1 bonus point, etc..
winning_with_bonus = [[w + i + 1 for w in win]for (i,win) in enumerate(winnings)]

# # part 1
# with open('day2.in', 'r') as f:
#     score = 0
#     for line in f.read().strip().split('\n'):
#         opponent = ord(line[0])-ord('A')
#         me = ord(line[2])-ord('X')
#         score += winning_with_bonus[me][opponent]
#     print(score)

# part 2
with open('day2.in', 'r') as f:
    score = 0
    for line in f.read().strip().split('\n'):
        opponent = ord(line[0])-ord('A')
        result = ord(line[2])-ord('X')
        if result == 0: # lose
            me = (opponent - 1) % 3
        elif result == 1: # draw
            me = opponent
        else: # win
            assert(result == 2)
            me = (opponent + 1) % 3
        score += winning_with_bonus[me][opponent]
    print(score)