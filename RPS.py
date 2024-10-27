# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random


options = ['R', 'P', 'S']

q_matrix = [[1,1,1],[1,1,1],[1,1,1]]

def player(prev_play, opponent_history=[]):
    if prev_play == "":
        #reset q matrix
        q_matrix[0] = [1,1,1]
        q_matrix[1] = [1,1,1]
        q_matrix[2] = [1,1,1]
        opponent_history = []

    if prev_play in options:
        opponent_history.append(prev_play)

    #notice the patterns betweenoppnents move.
    if len(opponent_history) > 3:
        #convert the moves to intergers
        prev = options.index(opponent_history[-2])
        curr = options.index(opponent_history[-1])
        q_matrix[prev][curr] = q_matrix[prev][curr] * 1.25
        q_matrix[curr][prev] = q_matrix[curr][prev] * 0.85


    
    guess = "R"
    if len(opponent_history) < 4:
        #guess = opponent_history[-2]
        guess = random.choice(options)

    else:
        #guess is the max value of the row corresponding to the last move of the opponent.
        guess = options[q_matrix[curr].index(max(q_matrix[curr]))]
    return guess 
