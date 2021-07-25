"""

Game design by Ryker Gogolkiewicz (rykergogo.com)

"""




import webbrowser
import tkinter as tk
from tkinter.constants import CENTER
from tkinter.ttk import *
import tkinter.font as font
from tkinter import PhotoImage, messagebox
import pygame


def callback():
    webbrowser.open_new('rykergogo.com')


def start_game():
    root.destroy()
    run_game()

def run_game():

    #The game ends and restarts once someone wins.
    def game_win(player):
        if player == 'x':
            win = tk.messagebox.showinfo('Good game','X Wins!',icon = 'info')
            root.destroy()
            run_game()
        elif player == 'o':
            win = tk.messagebox.showinfo('Good game','O Wins!',icon = 'info')
            root.destroy()
            run_game()


    def check():
        #Column Winning
        if grid_0['text'] == 'x' and grid_1['text'] == 'x' and grid_2['text'] == 'x' and grid_3['text'] == 'x' and grid_4['text'] == 'x':
            game_win('x')
        elif grid_0['text'] == 'o' and grid_1['text'] == 'o' and grid_2['text'] == 'o' and grid_3['text'] == 'o' and grid_4['text'] == 'o':
            game_win('o')
        elif grid_5['text'] == 'x' and grid_6['text'] == 'x' and grid_7['text'] == 'x' and grid_8['text'] == 'x' and grid_9['text'] == 'x':
            game_win('x')
        elif grid_5['text'] == 'o' and grid_6['text'] == 'o' and grid_7['text'] == 'o' and grid_8['text'] == 'o' and grid_9['text'] == 'o':
            game_win('o')
        elif grid_10['text'] == 'x' and grid_11['text'] == 'x' and grid_12['text'] == 'x' and grid_13['text'] == 'x' and grid_14['text'] == 'x':
            game_win('x')
        elif grid_10['text'] == 'o' and grid_11['text'] == 'o' and grid_12['text'] == 'o' and grid_13['text'] == 'o' and grid_14['text'] == 'o':
            game_win('o')
        elif grid_15['text'] == 'x' and grid_16['text'] == 'x' and grid_17['text'] == 'x' and grid_18['text'] == 'x' and grid_19['text'] == 'x':
            game_win('x')
        elif grid_15['text'] == 'o' and grid_16['text'] == 'o' and grid_17['text'] == 'o' and grid_18['text'] == 'o' and grid_19['text'] == 'o':
            game_win('o')
        elif grid_20['text'] == 'x' and grid_21['text'] == 'x' and grid_22['text'] == 'x' and grid_23['text'] == 'x' and grid_24['text'] == 'x':
            game_win('x')
        elif grid_20['text'] == 'o' and grid_21['text'] == 'o' and grid_22['text'] == 'o' and grid_23['text'] == 'o' and grid_24['text'] == 'o':
            game_win('o')
        
        #Row Winning
        elif grid_0['text'] == 'x' and grid_5['text'] == 'x' and grid_10['text'] == 'x' and grid_15['text'] == 'x' and grid_20['text'] == 'x':
            game_win('x')
        elif grid_0['text'] == 'o' and grid_5['text'] == 'o' and grid_10['text'] == 'o' and grid_15['text'] == 'o' and grid_20['text'] == 'o':
            game_win('o')
        elif grid_1['text'] == 'x' and grid_6['text'] == 'x' and grid_11['text'] == 'x' and grid_16['text'] == 'x' and grid_21['text'] == 'x':
            game_win('x')
        elif grid_1['text'] == 'o' and grid_6['text'] == 'o' and grid_11['text'] == 'o' and grid_16['text'] == 'o' and grid_21['text'] == 'o':
            game_win('o')
        elif grid_2['text'] == 'x' and grid_7['text'] == 'x' and grid_12['text'] == 'x' and grid_17['text'] == 'x' and grid_22['text'] == 'x':
            game_win('x')
        elif grid_2['text'] == 'o' and grid_7['text'] == 'o' and grid_12['text'] == 'o' and grid_17['text'] == 'o' and grid_22['text'] == 'o':
            game_win('o')
        elif grid_3['text'] == 'x' and grid_8['text'] == 'x' and grid_13['text'] == 'x' and grid_18['text'] == 'x' and grid_23['text'] == 'x':
            game_win('x')
        elif grid_3['text'] == 'o' and grid_8['text'] == 'o' and grid_13['text'] == 'o' and grid_18['text'] == 'o' and grid_23['text'] == 'o':
            game_win('o')
        elif grid_4['text'] == 'x' and grid_9['text'] == 'x' and grid_14['text'] == 'x' and grid_19['text'] == 'x' and grid_24['text'] == 'x':
            game_win('x')
        elif grid_4['text'] == 'o' and grid_9['text'] == 'o' and grid_14['text'] == 'o' and grid_19['text'] == 'o' and grid_24['text'] == 'o':
            game_win('o')
        
        #Diagonal left to right Winning
        elif grid_0['text'] == 'x' and grid_6['text'] == 'x' and grid_12['text'] == 'x' and grid_18['text'] == 'x' and grid_24['text'] == 'x':
            game_win('x')
        elif grid_0['text'] == 'o' and grid_6['text'] == 'o' and grid_12['text'] == 'o' and grid_18['text'] == 'o' and grid_24['text'] == 'o':
            game_win('o')
        
        #Diagonal right to left Winning
        elif grid_20['text'] == 'x' and grid_16['text'] == 'x' and grid_12['text'] == 'x' and grid_8['text'] == 'x' and grid_4['text'] == 'x':
            game_win('x')
        elif grid_20['text'] == 'o' and grid_16['text'] == 'o' and grid_12['text'] == 'o' and grid_8['text'] == 'o' and grid_4['text'] == 'o':
            game_win('o')

    #grid() didn't end up getting used, I used the built in grid function from tkinter to create the game board.
    #def grid(event = None):
        #Get window size
        #w = canvas.winfo_width()
        #h = canvas.winfo_height()

        #Vertical grid lines
        #for i in range(0, w, 100):
            #canvas.create_line([(i, 0), (i, h)], tag='grid_line', fill='white')

        #Horizontal grid lines
        #for i in range(0, h, 100):
            #canvas.create_line([(0, i), (w, i)], tag='grid_line', fill='white')

    #This class tells the game whos turn it is.
    class Turn:
        def __init__(self, switch):
            self.switch = switch

    #X will always go first because why not.
    player = Turn(0)
    player.switch = 0
    
    
    
    def test():
        print('Hello')
    
    #0 creates an X and 1 creates an O.
    def click(square, turn):
        if player.switch == 0:
            if square == 'grid_0' and grid_0['text'] != 'x' and grid_0['text'] != 'o':
                grid_0['font'] = gridFont
                grid_0['text'] = 'x'
                player.switch += 1
            elif square == 'grid_1' and grid_1['text'] != 'x' and grid_1['text'] != 'o':
                grid_1['font'] = gridFont
                grid_1['text'] = 'x'
                player.switch += 1
            elif square == 'grid_2' and grid_2['text'] != 'x' and grid_2['text'] != 'o':
                grid_2['font'] = gridFont
                grid_2['text'] = 'x'
                player.switch += 1
            elif square == 'grid_3' and grid_3['text'] != 'x' and grid_3['text'] != 'o':
                grid_3['font'] = gridFont
                grid_3['text'] = 'x'
                player.switch += 1
            elif square == 'grid_4' and grid_4['text'] != 'x' and grid_4['text'] != 'o':
                grid_4['font'] = gridFont
                grid_4['text'] = 'x'
                player.switch += 1
            elif square == 'grid_5' and grid_5['text'] != 'x' and grid_5['text'] != 'o':
                grid_5['font'] = gridFont
                grid_5['text'] = 'x'
                player.switch += 1
            elif square == 'grid_6' and grid_6['text'] != 'x' and grid_6['text'] != 'o':
                grid_6['font'] = gridFont
                grid_6['text'] = 'x'
                player.switch += 1
            elif square == 'grid_7' and grid_7['text'] != 'x' and grid_7['text'] != 'o':
                grid_7['font'] = gridFont
                grid_7['text'] = 'x'
                player.switch += 1
            elif square == 'grid_8' and grid_8['text'] != 'x' and grid_8['text'] != 'o':
                grid_8['font'] = gridFont
                grid_8['text'] = 'x'
                player.switch += 1
            elif square == 'grid_9' and grid_9['text'] != 'x' and grid_9['text'] != 'o':
                grid_9['font'] = gridFont
                grid_9['text'] = 'x'
                player.switch += 1
            elif square == 'grid_10' and grid_10['text'] != 'x' and grid_10['text'] != 'o':
                grid_10['font'] = gridFont
                grid_10['text'] = 'x'
                player.switch += 1
            elif square == 'grid_11' and grid_11['text'] != 'x' and grid_11['text'] != 'o':
                grid_11['font'] = gridFont
                grid_11['text'] = 'x'
                player.switch += 1
            elif square == 'grid_12' and grid_12['text'] != 'x' and grid_12['text'] != 'o':
                grid_12['font'] = gridFont
                grid_12['text'] = 'x'
                player.switch += 1
            elif square == 'grid_13' and grid_13['text'] != 'x' and grid_13['text'] != 'o':
                grid_13['font'] = gridFont
                grid_13['text'] = 'x'
                player.switch += 1
            elif square == 'grid_14' and grid_14['text'] != 'x' and grid_14['text'] != 'o':
                grid_14['font'] = gridFont
                grid_14['text'] = 'x'
                player.switch += 1
            elif square == 'grid_15' and grid_15['text'] != 'x' and grid_15['text'] != 'o':
                grid_15['font'] = gridFont
                grid_15['text'] = 'x'
                player.switch += 1
            elif square == 'grid_16' and grid_16['text'] != 'x' and grid_16['text'] != 'o':
                grid_16['font'] = gridFont
                grid_16['text'] = 'x'
                player.switch += 1
            elif square == 'grid_17' and grid_17['text'] != 'x' and grid_17['text'] != 'o':
                grid_17['font'] = gridFont
                grid_17['text'] = 'x'
                player.switch += 1
            elif square == 'grid_18' and grid_18['text'] != 'x' and grid_18['text'] != 'o':
                grid_18['font'] = gridFont
                grid_18['text'] = 'x'
                player.switch += 1
            elif square == 'grid_19' and grid_19['text'] != 'x' and grid_19['text'] != 'o':
                grid_19['font'] = gridFont
                grid_19['text'] = 'x'
                player.switch += 1
            elif square == 'grid_20' and grid_20['text'] != 'x' and grid_20['text'] != 'o':
                grid_20['font'] = gridFont
                grid_20['text'] = 'x'
                player.switch += 1
            elif square == 'grid_21' and grid_21['text'] != 'x' and grid_21['text'] != 'o':
                grid_21['font'] = gridFont
                grid_21['text'] = 'x'
                player.switch += 1
            elif square == 'grid_22' and grid_22['text'] != 'x' and grid_22['text'] != 'o':
                grid_22['font'] = gridFont
                grid_22['text'] = 'x'
                player.switch += 1
            elif square == 'grid_23' and grid_23['text'] != 'x' and grid_23['text'] != 'o':
                grid_23['font'] = gridFont
                grid_23['text'] = 'x'
                player.switch += 1
            elif square == 'grid_24' and grid_24['text'] != 'x' and grid_24['text'] != 'o':
                grid_24['font'] = gridFont
                grid_24['text'] = 'x'
                player.switch += 1
            check()
        else:
            if square == 'grid_0' and grid_0['text'] != 'x' and grid_0['text'] != 'o':
                grid_0['font'] = gridFont
                grid_0['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_1' and grid_1['text'] != 'x' and grid_1['text'] != 'o':
                grid_1['font'] = gridFont
                grid_1['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_2' and grid_2['text'] != 'x' and grid_2['text'] != 'o':
                grid_2['font'] = gridFont
                grid_2['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_3' and grid_3['text'] != 'x' and grid_3['text'] != 'o':
                grid_3['font'] = gridFont
                grid_3['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_4' and grid_4['text'] != 'x' and grid_4['text'] != 'o':
                grid_4['font'] = gridFont
                grid_4['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_5' and grid_5['text'] != 'x' and grid_5['text'] != 'o':
                grid_5['font'] = gridFont
                grid_5['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_6' and grid_6['text'] != 'x' and grid_6['text'] != 'o':
                grid_6['font'] = gridFont
                grid_6['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_7' and grid_7['text'] != 'x' and grid_7['text'] != 'o':
                grid_7['font'] = gridFont
                grid_7['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_8' and grid_8['text'] != 'x' and grid_8['text'] != 'o':
                grid_8['font'] = gridFont
                grid_8['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_9' and grid_9['text'] != 'x' and grid_9['text'] != 'o':
                grid_9['font'] = gridFont
                grid_9['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_10' and grid_10['text'] != 'x' and grid_10['text'] != 'o':
                grid_10['font'] = gridFont
                grid_10['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_11' and grid_11['text'] != 'x' and grid_11['text'] != 'o':
                grid_11['font'] = gridFont
                grid_11['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_12' and grid_12['text'] != 'x' and grid_12['text'] != 'o':
                grid_12['font'] = gridFont
                grid_12['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_13' and grid_13['text'] != 'x' and grid_13['text'] != 'o':
                grid_13['font'] = gridFont
                grid_13['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_14' and grid_14['text'] != 'x' and grid_14['text'] != 'o':
                grid_14['font'] = gridFont
                grid_14['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_15' and grid_15['text'] != 'x' and grid_15['text'] != 'o':
                grid_15['font'] = gridFont
                grid_15['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_16' and grid_16['text'] != 'x' and grid_16['text'] != 'o':
                grid_16['font'] = gridFont
                grid_16['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_17' and grid_17['text'] != 'x' and grid_17['text'] != 'o':
                grid_17['font'] = gridFont
                grid_17['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_18' and grid_18['text'] != 'x' and grid_18['text'] != 'o':
                grid_18['font'] = gridFont
                grid_18['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_19' and grid_19['text'] != 'x' and grid_19['text'] != 'o':
                grid_19['font'] = gridFont
                grid_19['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_20' and grid_20['text'] != 'x' and grid_20['text'] != 'o':
                grid_20['font'] = gridFont
                grid_20['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_21' and grid_21['text'] != 'x' and grid_21['text'] != 'o':
                grid_21['font'] = gridFont
                grid_21['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_22' and grid_22['text'] != 'x' and grid_22['text'] != 'o':
                grid_22['font'] = gridFont
                grid_22['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_23' and grid_23['text'] != 'x' and grid_23['text'] != 'o':
                grid_23['font'] = gridFont
                grid_23['text'] = 'o'
                player.switch -= 1
            elif square == 'grid_24' and grid_24['text'] != 'x' and grid_24['text'] != 'o':
                grid_24['font'] = gridFont
                grid_24['text'] = 'o'
                player.switch -= 1
            check()



    root = tk.Tk()

    root.title('Tic-tac-toe')

    root.geometry('470x530')

    root.resizable(False, False)

    icon = PhotoImage(file = 'icon.png')
    root.iconphoto(False, icon)

    pygame.mixer.init()
    pygame.mixer.music.load('song.mp3')
    pygame.mixer.music.play(-1)


    #Background Color of Title Screen
    #canvas = tk.Canvas(root, height=500, width=500, bg='black')
    #canvas.pack(fill = tk.BOTH, expand = True)
    #canvas.bind('<Configure>')

    #Frame for game (Decided to only use canvas for the game board)
    #frame = tk.Frame(root, bg='black')
    #frame.place(relwidth=1, relheight=1)

    gridFont = font.Font(family='Times New Roman')


    grid_0 = tk.Button(root, text='.', fg='white', bg='black', command = lambda square = 'grid_0' : click(square, player.switch), padx=38, pady=38)
    grid_1 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_1' : click(square, player.switch))
    grid_2 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_2' : click(square, player.switch))
    grid_3 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_3' : click(square, player.switch))
    grid_4 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_4' : click(square, player.switch))
    grid_5 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_5' : click(square, player.switch))
    grid_6 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_6' : click(square, player.switch))
    grid_7 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_7' : click(square, player.switch))
    grid_8 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_8' : click(square, player.switch))
    grid_9 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_9' : click(square, player.switch))
    grid_10 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_10' : click(square, player.switch))
    grid_11 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_11' : click(square, player.switch))
    grid_12 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_12' : click(square, player.switch))
    grid_13 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_13' : click(square, player.switch))
    grid_14 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_14' : click(square, player.switch))
    grid_15 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_15' : click(square, player.switch))
    grid_16 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_16' : click(square, player.switch))
    grid_17 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_17' : click(square, player.switch))
    grid_18 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_18' : click(square, player.switch))
    grid_19 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_19' : click(square, player.switch))
    grid_20 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_20' : click(square, player.switch))
    grid_21 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_21' : click(square, player.switch))
    grid_22 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_22' : click(square, player.switch))
    grid_23 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_23' : click(square, player.switch))
    grid_24 = tk.Button(root, text='.', fg='white', bg='black', padx=38, pady=38, command = lambda square = 'grid_24' : click(square, player.switch))


    grid_0.grid(row=0, column=0, sticky='NSEW')
    grid_1.grid(row=1, column=0, sticky='NSEW')
    grid_2.grid(row=2, column=0, sticky='NSEW')
    grid_3.grid(row=3, column=0, sticky='NSEW')
    grid_4.grid(row=4, column=0, sticky='NSEW')
    grid_5.grid(row=0, column=1, sticky='NSEW')
    grid_6.grid(row=1, column=1, sticky='NSEW')
    grid_7.grid(row=2, column=1, sticky='NSEW')
    grid_8.grid(row=3, column=1, sticky='NSEW')
    grid_9.grid(row=4, column=1, sticky='NSEW')
    grid_10.grid(row=0, column=2, sticky='NSEW')
    grid_11.grid(row=1, column=2, sticky='NSEW')
    grid_12.grid(row=2, column=2, sticky='NSEW')
    grid_13.grid(row=3, column=2, sticky='NSEW')
    grid_14.grid(row=4, column=2, sticky='NSEW')
    grid_15.grid(row=0, column=3, sticky='NSEW')
    grid_16.grid(row=1, column=3, sticky='NSEW')
    grid_17.grid(row=2, column=3, sticky='NSEW')
    grid_18.grid(row=3, column=3, sticky='NSEW')
    grid_19.grid(row=4, column=3, sticky='NSEW')
    grid_20.grid(row=0, column=4, sticky='NSEW')
    grid_21.grid(row=1, column=4, sticky='NSEW')
    grid_22.grid(row=2, column=4, sticky='NSEW')
    grid_23.grid(row=3, column=4, sticky='NSEW')
    grid_24.grid(row=4, column=4, sticky='NSEW')


    root.mainloop()




root = tk.Tk()

root.title('Welcome to Tic-tac-toe!')

root.resizable(False, False)

icon = PhotoImage(file = 'icon.png')
root.iconphoto(False, icon)

#Background Color of Title Screen
canvas = tk.Canvas(root, height=500, width=500, bg='black')
canvas.pack()

#Frame for start button
frame = tk.Frame(root, bg='black')
frame.place(relwidth=0.5, relheight=0.5, relx=0.1, rely=0.1)

#Start Button
start = tk.Button(root, text='Start Game', padx=50, pady=50, fg='white', bg='black', command = start_game)
start.pack()
start.place(relx=0.5, rely=0.5, anchor=CENTER)

#Credit to me
credit = tk.Button(root, text='Credit', padx=40, pady=40, fg='white', bg='black', command = callback)
credit.pack()
credit.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()