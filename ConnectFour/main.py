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
        condition = checkWin(gameBoard)
        if condition:
            print(f"Congratulations! {players['player1']} won!")
            playing = False
            continue

        # player2 turn
        gameBoard, condition = player2Turn(gameBoard)
        # check for win
        condition = checkWin(gameBoard)
        if condition:
            print(f"Congratulations! {players['player2']} won!")
            playing = False


def player1Turn(gameBoard, condition=False):
    print(f"{players['player1']}, it's your turn!")

    while True:
        print("Please enter the column number you want to place your piece in (0-6):")
        try:
            column = int(input())
            if 0 <= column <= 6:
                break
            else:
                print("Invalid column. Please enter a number between 0 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 6.")

    # place piece
    for i in range(5, -1, -1):
        if gameBoard[i][column] == 0:
            gameBoard[i][column] = 1
            break

    print(pd.DataFrame(gameBoard))
    return gameBoard, condition


def player2Turn(gameBoard, condition=False):
    print(f"{players['player2']}, it's your turn!")
    while True:
        print("Please enter the column number you want to place your piece in (0-6):")
        try:
            column = int(input())
            if 0 <= column <= 6:
                break
            else:
                print("Invalid column. Please enter a number between 0 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 6.")

    # place piece
    for i in range(5, -1, -1):
        if gameBoard[i][column] == 0:
            gameBoard[i][column] = 2
            break

    print(pd.DataFrame(gameBoard))
    return gameBoard, condition


def checkWin(gameBoard):
    if (
        checkHorizontal(gameBoard)
        or checkVertical(gameBoard)
        or checkDiagonal(gameBoard)
    ):
        return True

    return False


def checkHorizontal(gameBoard):
    for i in range(6):
        for j in range(4):
            if (
                gameBoard[i][j]
                == gameBoard[i][j + 1]
                == gameBoard[i][j + 2]
                == gameBoard[i][j + 3]
                != 0
            ):
                return True
    return False


def checkVertical(gameBoard):
    for i in range(3):
        for j in range(7):
            if (
                gameBoard[i][j]
                == gameBoard[i + 1][j]
                == gameBoard[i + 2][j]
                == gameBoard[i + 3][j]
                != 0
            ):
                return True
    return False


def checkDiagonal(gameBoard):
    for i in range(3):
        for j in range(4):
            if (
                gameBoard[i][j]
                == gameBoard[i + 1][j + 1]
                == gameBoard[i + 2][j + 2]
                == gameBoard[i + 3][j + 3]
                != 0
            ):
                return True
    for i in range(3):
        for j in range(6, 2, -1):
            if (
                gameBoard[i][j]
                == gameBoard[i + 1][j - 1]
                == gameBoard[i + 2][j - 2]
                == gameBoard[i + 3][j - 3]
                != 0
            ):
                return True
    return False


players = {"player1": 0, "player2": 0}

start()
