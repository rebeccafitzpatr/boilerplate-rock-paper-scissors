# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random


options = ['R', 'P', 'S']

q_matrix = [[1,1,1],[1,1,1],[1,1,1]]
opponent = [0]
play_history=[0,0,0]

def player(prev_play, opponent_history=[]):
    opponent[0] +=1
    if prev_play in options:
        opponent_history.append(prev_play)


    if opponent[0] % 1000 == 0:
        print("reset")
        #reset q matrix
        q_matrix[0] = [1,1,1]
        q_matrix[1] = [1,1,1]
        q_matrix[2] = [1,1,1]
        opponent_history = []
        play_order=[{
            "RR": 0,
            "RP": 0,
            "RS": 0,
            "PR": 0,
            "PP": 0,
            "PS": 0,
            "SR": 0,
            "SP": 0,
            "SS": 0,
        }]
   
    
    if opponent[0] > 2000 and opponent[0] < 3000:

        return player2(prev_play,0, opponent_history)

    elif opponent[0] <2000 and opponent[0] > 1000:
        return player2(prev_play,2, opponent_history)

    elif opponent[0] <1000:
        return player3(prev_play, play_history)
    
    
    

    

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


play_order=[{
        "RR": 0,
        "RP": 0,
        "RS": 0,
        "PR": 0,
        "PP": 0,
        "PS": 0,
        "SR": 0,
        "SP": 0,
        "SS": 0,
    }]

def player3(prev_play, player_history):
    if len(player_history) <3:

        guess = random.choice(options)
        #increment the index of the quess in play_history
        play_history[options.index(guess)] += 1
        return guess
    else:
        #returhn the least played move
        guess = options[play_history.index(max(play_history))]
        

        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        play = ideal_response[guess]
        play_history[options.index(play)] += 1
        return play


def player2(prev_play,opp, opponent_history=[]):
    

    if not prev_play:
        prev_play = 'R'
    opponent_history.append(prev_play)

    last_two = "".join(opponent_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1

    potential_plays = [
        prev_play + "R",
        prev_play + "P",
        prev_play + "S",
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }

    prediction1 = min(sub_order, key=sub_order.get)[-1:]
    prediction2 = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    #return ideal_response[prediction]
    if opp == 0 and len(opponent_history) >2:
        return ideal_response[opponent_history[-2]]
    elif opp == 1 and len(opponent_history) >4:
        return ideal_response[opponent_history[-3]]
    

    elif opp == 2 and len(opponent_history) >4:

        return ideal_response[ideal_response[prediction1]]
    else: 
        return ideal_response[prediction2]