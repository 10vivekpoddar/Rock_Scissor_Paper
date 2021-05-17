# Rock Scissor Paper game!
"""
write a program in which user and computer will choose thier options 
and they will win according to the rules:
  - rock beats scissor
  - scissor beats paper
  - paper beats rocks
there will be 3 rounds
"""
import random

# defining the constant
N_GAME = 3

# main function
def main():
    total_score = 0
    # printing the welcome message and rules
    print_rules()
    # running the game for 3 round
    for i in range(N_GAME):
        # getting the moves
        ai_move = get_ai_move()
        human_move = get_human_move()
        # getting the winner
        winner = get_winner(ai_move,human_move)
        # getting the total score
        total_score += calc_score(winner,total_score)
        # declaring the result
        announce_result(winner,ai_move)
    # printing the total score
    print("Your score: ",total_score)

# function to print the rules
def print_rules():
    print("Welcome to the Rock Paper Scissor")
    print("You will play 3 games against AI")
    print("Rules:")
    print("rock beats scissor")
    print("scissor beats paper")
    print("paper beats rocks")
    print("-------------------------------------------")
# function to get the ai move
def get_ai_move():
    value = random.randint(1,3)
    if value == 1:
        return 'rock'
    elif value == '2':
        return 'paper'
    else:
        return 'scissor'
# function to get the human move
def get_human_move():
    while True:
        human_move = input("Enter your move: ")
        if is_move_valid(human_move):
            return human_move
        print("Invalid entry!")
        print()
# function to check whether human move is valid or not
def is_move_valid(human_move):
    if human_move == 'rock':
        return True
    elif human_move == 'paper':
        return True
    elif human_move == 'scissor':
        return True
# function to get the winner
def get_winner(ai_move,human_move):

    if ai_move == human_move:
        return 'tie'

    if ai_move == 'rock':
        if human_move == 'paper':
            return 'human'
        elif human_move == 'scissor':
            return 'ai'

    if ai_move == 'paper':
        if human_move == 'rock':
            return 'ai'
        elif human_move == 'scissor':
            return 'human'

    if ai_move == 'scissor':
        if human_move == 'paper':
            return 'ai'
        elif human_move == 'rock':
            return 'human'
# fiunction for updating total score
def calc_score(winner,total_score):
    if winner == 'ai':
        return -1
    elif winner == 'human':
        return +1
    else:
        return 0
# function for announcing the result
def announce_result(winner,ai_move):
        print("A.I move:",ai_move)
        print("Winner:",winner)
        print()
# telling the python to call main function when program runs
if __name__=="__main__":
    main()