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
        gameBoard, condition = player1Turn(gameBoard)
        # check for win
        if condition:
            print(f"Congratulations! {players['player1']} won!")
            playing = False
            continue

        # player2 turn
        gameBoard, condition = player2Turn(gameBoard)
        # check for win
        if condition:
            print(f"Congratulations! {players['player2']} won!")
            playing = False
        

def player1Turn(gameBoard, condition=False):
    print(f"{players['player1']}, it's your turn!")
    print("Please enter the column number you want to place your piece in:")
    
    # Ensure column is converted to an integer
    column = int(input())
    
    # place piece
    for i in range(5, -1, -1):
        if gameBoard[i][column] == 0:
            gameBoard[i][column] = 1
            break

    print(pd.DataFrame(gameBoard))
    return gameBoard, condition


def player2Turn(gameBoard, condition=False):
    print(f"{players['player2']}, it's your turn!")
    print("Please enter the column number you want to place your piece in:")
    
    # Ensure column is converted to an integer
    column = int(input())
    
    # place piece
    for i in range(5, -1, -1):
        if gameBoard[i][column] == 0:
            gameBoard[i][column] = 2
            break

    print(pd.DataFrame(gameBoard))
    return gameBoard, condition

players = {"player1": 0, "player2": 0}

start()
