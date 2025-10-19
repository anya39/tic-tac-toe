#setup
import tkinter as tk
from tkinter import messagebox

def reset_board():


def on_click(row, column, buttons, current_player):
    # checks if box is already clicked
    if buttons[row][column]["text"] != "":
        return
    buttons[row][column]["text"] = current_player

    if check_winner():
        messagebox.showinfo(f"Game Over!\nPlayer {current_player} wins!")
        reset_board()
        return
    
    if check_draw():
        

