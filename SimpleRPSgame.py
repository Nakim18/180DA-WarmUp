#simple rock paper scissors game

import random

moveOptions = ["R", "P", "S"]

play = True
while play == True:
    move = input("Choose R, P, or S\n")
    oppMove = random.choice(moveOptions)
    if(move == "R"):
        if(oppMove == "R"):
            print("Opponent played rock\nYou tied\n")
        elif(oppMove == "P"):
            print("Opponent played paper\nYou lost\n")
        else:
            print("Opponent played scissor\nYou won\n")
    elif(move == "P"):
        if(oppMove == "R"):
            print("Opponent played rock\nYou won\n")
        elif(oppMove == "P"):
            print("Opponent played paper\nYou tied\n")
        else:
            print("Opponent played scissor\nYou lost\n")
    elif(move == "S"):
        if(oppMove == "R"):
            print("Opponent played rock\nYou lost\n")
        elif(oppMove == "P"):
            print("Opponent played paper\nYou won\n")
        else:
            print("Opponent played scissor\nYou tied\n")
    else:
        print("Select valid move\n")
        continue
    outcome = input("Play again?\n")
    if(outcome == "Yes" or outcome == "yes"):
        continue
    else:
        play = False
    
