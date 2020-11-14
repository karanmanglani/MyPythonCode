############################################## Game Logic #######################################################
# Initialization
    # Board 
    # Player Class
    # gameStillGoing
    # posLeft = 9
    # currentPlayer

# Loop 

    # handleTurn
        # Print the symbol in required position and flip player
        # Display board and posLeft -= 1
        
    
    # checkIfWin
        # Checkrows
        # checkcolumns
        # checkdiagonals

        # if any true print winner and gameStillGoing = false

    # checkiftie
        # if posLeft == 0 and gameStillGoing 
########################################### Programming the game ###############################################

# Initializing the variables
board = ["-"]*9
gameStillGoing = True
posLeft = 9
currentPlayer = None
player1 = player2 = None
winnerSymbol = None

# Initializing the class and adding player
class player(object):
    def __init__(self,symbol):
        self.symbol = symbol

symbol = input("Enter symbol for player 1 (X or O): ")
if symbol == "X" or symbol == "O":
    player1 = player(symbol)
else:
    while not(symbol == "X" or symbol == "O"): 
        symbol = input("Enter symbol for player 1 (X or O): ")

if symbol == "X":
    player2 = player("O")
else:
    player2 = player("X")

currentPlayer = player1

# writing the required function
def displayBoard():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    return None

def flipPlayer(currentPlayer):
    if currentPlayer.symbol == "X":
        currentPlayer.symbol = "O"
    else:
        currentPlayer.symbol = "X"
    return None

def handleTurn(currentPlayer,posLeft):
    pos = int(input("Enter the postion for " + currentPlayer.symbol +  " :")) - 1
    if (board[pos] == "-" and pos <= 9):
        board[pos] = currentPlayer.symbol
        displayBoard()
        flipPlayer(currentPlayer)
        posLeft -= 1
    else:
        print("Position not avialable!! Please Try again")
    return None

def checkIfWin():
    if (checkRows() or checkDiagonals() or checkColumns()):
        gameStillGoing = False
        print("Executed")
        return True
    else:
        return False

def checkRows():
    if(board[0] == board[3] == board[6] and not(board[0] == "-")):
        winnerSymbol = board[0]
        print(winnerSymbol + " Wins!!")
        return True
    elif(board[1] == board[4] == board[7] and not(board[1] == "-")):
        winnerSymbol = board[1]
        print(winnerSymbol + " Wins!!")
        return True
    elif (board[2] == board[5] == board[8] and not(board[2] == "-")):
        winnerSymbol = board[2]
        print(winnerSymbol + " Wins!!")
        return True
    else:
        return False

def checkColumns():
    if(board[0] == board[1] == board[2] and not(board[0] == "-")):
        winnerSymbol = board[0]
        print(winnerSymbol + " Wins!!")
        return True
    elif(board[3] == board[4] == board[5] and not(board[3] == "-")):
        winnerSymbol = board[3]
        print(winnerSymbol + " Wins!!")
        return True
    elif (board[6] == board[7] == board[8] and not(board[6] == "-")):
        winnerSymbol = board[6]
        print(winnerSymbol + " Wins!!")
        return True
    else:
        return False

def checkDiagonals():
    if(board[0] == board[4] == board[8] and not(board[0] == "-")):
        winnerSymbol = board[0]
        print(winnerSymbol + " Wins!!")
        return True
    elif(board[2] == board[4] == board[6] and not(board[2] == "-")):
        winnerSymbol = board[2]
        print(winnerSymbol + " Wins!!")
        return True
    else:
        return False

def checkIfTie(posLeft):
    if(posLeft == 0 and not checkIfWin()):
        print("It's a tie!!")
        gameStillGoing = False
        return True
    else:
        return False

# Game Loop
displayBoard()
while gameStillGoing:
    handleTurn(currentPlayer,posLeft)
    checkIfWin()
    checkIfTie(posLeft)
        
