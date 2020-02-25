# Tic Tac Toe gui game
# @Author: Mohammed Marwan Mostafa


from tkinter import *
Turn = ""
gameType = 1
listOfButtons = {}
count = 0

# starting function to start game or reset a new game
def reset(window1=None, window2=None):
    if window1 == None and window2 == None:
        first()

    else:
        window1.destroy()
        window2.destroy()
        first()


# tk function display option for the game 
def first():

    def XorO():
        global Turn
        Turn = v1.get()

    def AIor2P():
        global gameType
        gameType = v2.get()
    top = Tk()
    v1 = StringVar()
    v2 = IntVar()

    Widget1 = Label(top, text='Select X or O for the first player').grid(
        column=2, row=0)

    r1 = Radiobutton(top, text='X', variable=v1,
                     value="X", command=lambda: XorO()).grid(column=2, row=1)

    r2 = Radiobutton(top, text='O', variable=v1,
                     value="O", command=lambda: XorO()).grid(column=2, row=2)

    Widget2 = Label(top, text='Select Type of game').grid(
        column=2, row=4)

    r3 = Radiobutton(top, text='AI', variable=v2,
                     value=1, command=lambda: AIor2P()).grid(column=2, row=5)

    r4 = Radiobutton(top, text='Two Players', variable=v2,
                     value=2, command=lambda: AIor2P()).grid(column=2, row=6)

    button = Button(top, text='Ok', command=lambda: Bord(top)).grid(
        column=2, row=7)
    button2 = Button(top, text='Cancel', command=lambda: quit()).grid(
        column=2, row=8)

    top.mainloop()

# tk fuction to display the tic tac toe bord
def Bord(window):
    global listOfButtons
    window.destroy()
    BordG = Tk()
    BordG.title('Tic_Tac_Toe')
    rows = 0
    columns = 0
    for i in range(9):
        if i == 3 or i == 6:
            rows += 1
            columns = 0
        listOfButtons[i] = Button(BordG, text=i+1, height=6, width=10)
        listOfButtons[i].grid(column=columns, row=rows)
        columns += 1
    listOfButtons[0].config(command=lambda: play(0, BordG))
    listOfButtons[1].config(command=lambda: play(1, BordG))
    listOfButtons[2].config(command=lambda: play(2, BordG))
    listOfButtons[4].config(command=lambda: play(4, BordG))
    listOfButtons[3].config(command=lambda: play(3, BordG))
    listOfButtons[5].config(command=lambda: play(5, BordG))
    listOfButtons[6].config(command=lambda: play(6, BordG))
    listOfButtons[7].config(command=lambda: play(7, BordG))
    listOfButtons[8].config(command=lambda: play(8, BordG))

    BordG.mainloop()

# tk function display to the user (the winner, option to reset the game or exit)
def endgame(player, window):

    winWindow = Tk()
    Widget1 = Label(winWindow, text="      The Winner is "+player, height=3)
    Widget1.grid(row=0, column=0, columnspan=2, sticky='nsew')
    button = Button(winWindow, text='Play Again',
                    command=lambda: reset(window, winWindow))
    button.grid(row=1, column=0, columnspan=2)
    button2 = Button(winWindow, text='Exit', command=lambda: quit())
    button2.grid(row=3, column=0, columnspan=2)
    winWindow.mainloop()

# this function test the bord to find out if there is a winner or not
def checkwin(listToCheck):
    return (listToCheck[0]['text'] == listToCheck[1]['text'] and listToCheck[0]['text'] == listToCheck[2]['text']) or (listToCheck[3]['text'] == listToCheck[4]['text'] and listToCheck[3]['text'] == listToCheck[5]['text']) or (listToCheck[6]['text'] == listToCheck[7]['text'] and listToCheck[6]['text'] == listToCheck[8]['text']) or (listToCheck[0]['text'] == listToCheck[3]['text'] and listToCheck[0]['text'] == listToCheck[6]['text']) or (listToCheck[1]['text'] == listToCheck[4]['text'] and listToCheck[1]['text'] == listToCheck[7]['text']) or (listToCheck[2]['text'] == listToCheck[5]['text'] and listToCheck[2]['text'] == listToCheck[8]['text']) or (listToCheck[0]['text'] == listToCheck[4]['text'] and listToCheck[0]['text'] == listToCheck[8]['text']) or (listToCheck[2]['text'] == listToCheck[4]['text'] and listToCheck[2]['text'] == listToCheck[6]['text'])

# this function swip the players wither X or O and call checkwin function every turn
def turnchange(window):
    global Turn
    global listOfButtons
    global count
    count+=1

    if count == 9:
        endgame("None", window)
    temp = Turn
    if Turn == 'X':
        Turn = 'O'
    else:
        Turn = 'X'
    if checkwin(listOfButtons):
        endgame(temp, window)

# this function change the postion to the charecter to X or O >depend on the player turn<
# and have functionality to play aginst AI if gameType is 1  
def play(position, window):
    global gameType
    global listOfButtons
    global Turn

    if gameType == 1:
        if listOfButtons[position]['text'] != 'X' and listOfButtons[position]['text'] != 'O':
            listOfButtons[position]['text'] = Turn
            turnchange(window)
        else:
            return
        for j in range(0, 9):
            if listOfButtons[j]['text'] != 'X' and listOfButtons[j]['text'] != 'O':
                listOfButtons[j]['text'] = Turn
                if checkwin(listOfButtons):
                    listOfButtons[j]['text'] = Turn
                    turnchange(window)
                    return
                else:
                    listOfButtons[j]['text'] = j+1

        if Turn=='X':
            test='O'
        else:
            test='X'
        for j in range(0, 9):     
            if listOfButtons[j]['text'] != 'X' and listOfButtons[j]['text'] != 'O':
                listOfButtons[j]['text'] = test
                if checkwin(listOfButtons):
                    listOfButtons[j]['text'] = Turn
                    turnchange(window)
                    return
                else:
                    listOfButtons[j]['text'] = j+1

        if listOfButtons[4]['text'] != 'X' and listOfButtons[4]['text'] != 'O':
            listOfButtons[4]['text'] = Turn
            turnchange(window)
            return

        for i in range(0, 9, 2):
            if listOfButtons[i]['text'] != 'X' and listOfButtons[i]['text'] != 'O':
                listOfButtons[i]['text'] = Turn
                turnchange(window)
                return

        for i in range(1, 9, 1):
            if listOfButtons[i]['text'] != 'X' and listOfButtons[i]['text'] != 'O':
                listOfButtons[i]['text'] = Turn
                turnchange(window)
                return

    if gameType == 2:
        if listOfButtons[position]['text'] != 'X' and listOfButtons[position]['text'] != 'O':
            listOfButtons[position]['text'] = Turn
            turnchange(window)


reset()
