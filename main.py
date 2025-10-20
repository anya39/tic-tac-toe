#setup
import tkinter as tk
from tkinter import messagebox
from helper import on_click

#main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("405x410")
root.resizable(0,0) #disables resizing

#setup for board and playing
current_player = "X"
x_score = 0
o_score = 0
buttons = [[None for i in range (3)] for i in range (3)]

#define callback to update the current player
def set_player_callback(new_player):
    global current_player
    current_player = new_player

#define callback to reset the board (placeholder)
def reset_callback(current_player):
    global x_score, o_score
    if current_player=="X":
        x_score+=1
    elif current_player=="O":
        o_score+=1
    
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
    set_player_callback("X")

    #updates score label
    score_label.config(text=f"Player X Score: {x_score} | Player O Score: {o_score}")

#creates buttons and places them in grid
for i in range(3):
    for j in range(3):
        button = tk.Button(
            root,
            text="",
            font=("Arial", 24),
            width=7, height=4,
            command = lambda row=i, col=j: on_click(row, col, buttons, current_player, set_player_callback, reset_callback)
        )
        button.grid(row=i, column=j)
        buttons[i][j] = button

#adds score label
score_label = tk.Label(root, text=f"Player X Score: {x_score} | Player O Score: {o_score}")
score_label.grid(row=3, column= 0, columnspan=3, pady=10)

#goes at end of program to keep window open
root.mainloop()