import pandas as pd

def start():
    print("Welcome to Connect Four!")
    print("Player 1, please enter your name:")
    players["player1"] = input()
    print("Player 2, please enter your name:")
    players["player2"] = input()
    print("Let's start the game!")
    
    playing = True
    gameBoard = [[0 for _ in range(7)] for _ in range(6)]
    print(pd.DataFrame(gameBoard))
    
    while playing:
        # player1 turn
        gameBoard,condition = player1Turn(gameBoard)
        # check for win
        if condition == True:
            print("Congratulations! You Player1 won!")
            playing = False

        # player2 turn
        gameBoard,condition = player2Turn(gameBoard)
        # check for win
        if condition == True:
            print("Congratulations! You Player2 won!")
            playing = False
        

def player1Turn(gameBoard,condition = False):
    print(players["player1"] + ", it's your turn!")
    print("Please enter the column number you want to place your piece in:")
    column = input()
    # place piece
    for i in range(5, -1, -1):
        if gameBoard[i][column] == 0:
            gameBoard[i][column] = 1
            break

    print(pd.DataFrame(gameBoard))
    
    return gameBoard,condition




def player2Turn(gameBoard,condition = False):
    print(players["player2"] + ", it's your turn!")
    print("Please enter the column number you want to place your piece in:")
    column = input()
    # place piece
    gameBoard[0][column] = 1
    print(gameBoard)
    return gameBoard,condition

players = {"player1": 0, "player2": 0}

start()