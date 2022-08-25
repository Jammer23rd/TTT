# tic tac toe by FE

# playing board
def board():
    print ("\n")
    print ("\033[47m"+ ttt1[0] +"|"+ ttt1[1] +"|"+ ttt1[2] +"\033[0m")
    print ("\033[47m"+ ttt[0] +"|"+ ttt[1] +"|"+ ttt[2] +"\033[0m")
    print ("\033[47m"+ ttt2[0] +"|"+ ttt2[1] +"|"+ ttt2[2] +"\033[0m")
    print ("\033[47m"+ ttt1[3] +"|"+ ttt1[4] +"|"+ ttt1[5] +"\033[0m")
    print ("\033[47m"+ ttt[3] +"|"+ ttt[4] +"|"+ ttt[5] +"\033[0m")
    print ("\033[47m"+ ttt2[3] +"|"+ ttt2[4] +"|"+ ttt2[5] +"\033[0m")
    print ("\033[47m"+ ttt1[6] +"|"+ ttt1[7] +"|"+ ttt1[8] +"\033[0m")
    print ("\033[47m"+ ttt[6] +"|"+ ttt[7] +"|"+ ttt[8] +"\033[0m")
    print ("\033[47m"+ ttt1[6] +"|"+ ttt1[7] +"|"+ ttt1[8] +"\033[0m")
    print ("\n")
    return

# player 1 and payer 2 plays
def play1():
    try:
        var = int(input ("Your turn \033[44m"+ p1 +"\033[0m!\n"))
        var = var - 1
        if (var in t): # used to check if play is valid and check box on board
            ttt[var] = ("\033[44m       \033[47m")
            ttt1[var] = ("\033[44m       \033[47m")
            ttt2[var] = ("\033[44m_______\033[47m")
            t[var] = ("null") # removes position from play
            xxx.append (var) # adds position to X(blue) played
        else: # screams invalid position of play
            board()
            print ("\n\n\nChoose a valid position \033[34m"+ p1 +"\033[0m!")
            play1()
        return
    except ValueError: # if not int input, ask for int input
        board()
        print("Incorrect input, Try again.")
        print("Choose an available position on the board.\n")
        play1()

def play2():
    try:
        var = int(input ("Your time to play \033[33m"+ p2 +"\033[0m!\n"))
        var = var - 1
        if (var in t):
            ttt[var] = ("\033[43m       \033[47m")
            ttt1[var] = ("\033[43m       \033[47m")
            ttt2[var] = ("\033[43m_______\033[47m")
            t[var] = ("null")
            ooo.append (var)
        else:
            board()
            print ("Choose a valid position \033[33m"+ p2 +"\033[0m!")
            play2()
    except ValueError:
        board()
        print("Incorrect input, Try again\n")
        play2()

# check win 
def win(xoro):
    array2  = [[0, 1, 2], [0, 4, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [3, 4, 5], [6, 7, 8], [2, 4, 6]] # winning plays
    x = y = qwerty = 0
    for x in range (8):
        count = 0
        for y in range (3):
            for qwerty in range (len(xoro)):
                if xoro[qwerty] == array2[x][y] :
                    count = count + 1
                    if count == 3: # a winning combination was inserted by one player
                        if xoro == xxx: # player 1 wins 
                            print ("\n\033[44mCongrats " + p1 + "!! You've won the game.\033[0m\n")
                            print ("\n\033[44mCongrats " + p1 + "!! You've won the game.\033[0m\n")
                            print ("\n\033[44mCongrats " + p1 + "!! You've won the game.\033[0m\n")
                            print ("\n\033[44mCongrats " + p1 + "!! You've won the game.\033[0m\n")
                            print ("\n\033[44mCongrats " + p1 + "!! You've won the game.\033[0m\n")
                            print ("\n\033[44mCongrats " + p1 + "!! You've won the game.\033[0m\n")
                            print ("\n\033[44mCongrats " + p1 + "!! You've won the game.\033[0m\n")
                            input("\033[44mPress any key to exit\033[0m")
                            print("\n\n\n\n\n\033[44mBye!\033[0m\n\n\n\n\n\n")
                            exit()
                        else: # player 2 wins
                            print ("\n\033[43mCongrats " + p2 + "!! You've won the game.\033[0m\n")
                            print ("\n\033[43mCongrats " + p2 + "!! You've won the game.\033[0m\n")
                            print ("\n\033[43mCongrats " + p2 + "!! You've won the game.\033[0m\n")
                            print ("\n\033[43mCongrats " + p2 + "!! You've won the game.\033[0m\n")
                            print ("\n\033[43mCongrats " + p2 + "!! You've won the game.\033[0m\n")
                            print ("\n\033[43mCongrats " + p2 + "!! You've won the game.\033[0m\n")
                            print ("\n\033[43mCongrats " + p2 + "!! You've won the game.\033[0m\n")
                            input("\033[43mPress any key to exit\033[0m")
                            print("\n\n\n\n\n\033[43mBye!\033[0m\n\n\n\n\n\n")
                            exit()
            qwerty = qwerty + 1
        y = y + 1    
    x = x + 1

# game
def game():
    board()
    play1()
    board()
    play2()
    board()
    play1()
    board()
    play2()
    board()
    play1()
    board()
    win(xxx)
    play2()
    board()
    win(ooo)
    play1()
    board()
    win(xxx)
    play2()
    board()
    win(ooo)
    play1()
    board()
    win(xxx)

# reset and start again
def reset():
    ttt = ['   1   ', '   2   ', '   3   ', '   4   ', '   5   ', '   6   ', '   7   ', '   8   ', '   9   ']
    ttt1 = ['       ', '       ', '       ', '       ', '       ', '       ', '       ', '       ', '       ']
    ttt2 = ['_______', '_______', '_______', '_______', '_______', '_______', '_______', '_______', '_______']
    t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    xxx = []
    ooo = []
    


# defining tables
ttt = ['   1   ', '   2   ', '   3   ', '   4   ', '   5   ', '   6   ', '   7   ', '   8   ', '   9   ']
ttt1 = ['       ', '       ', '       ', '       ', '       ', '       ', '       ', '       ', '       ']
ttt2 = ['_______', '_______', '_______', '_______', '_______', '_______', '_______', '_______', '_______']
t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
xxx = []
ooo = []

# defining players name, colours and welcome screen
p1 = input ("\n\n\n\033[34mPlayer One, Insert your Name: \033[0m\n  ") 
p2 = input ("\n\n\n\033[33mPlayer Two, Insert your Name: \033[0m\n  ") 
print ("\n\n\nWelcome \033[34m"+ p1 +"\033[0m!\n     You'll play with the \033[34mBlue\033[0m.\n") 
print ("\nHi there, \033[33m"+ p2 + "\033[0m.\n     You'll play with the \033[33mYellow\033[0m.\n\n")

# printing game rules
input("Press ENTER to see Game Rules\n")
board()
print ("\033[45mIt's a simple game. You have to place tic tac and toe in a line.\033[0m")
print ("\n\033[45mChoose the number of the square you want to play.\033[0m")

# continue and confirming fisrt play
print("\n\033[34m"+ p1 +"\033[0m will play first.\n")
print("\033[33m"+ p2 +"\033[0m will play last.\n\n")
input("\n\nPress ENTER to continue \n\n")

# start game
game() 