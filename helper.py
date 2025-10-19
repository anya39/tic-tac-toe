#setup
import tkinter as tk
from tkinter import messagebox

#def reset_board():


def on_click(row, col, buttons, current_player, set_player_callback, reset_callback):
    # checks if box is already clicked
    if buttons[row][col]["text"] != "":
        return
    buttons[row][col]["text"] = current_player #set X or Y

    if check_winner():
        messagebox.showinfo(f"Game Over!\nPlayer {current_player} wins!")
        reset_callback()
        return
    
    if check_draw():
        messagebox.showinfo("Game Over! It's a draw!")
        reset_callback()
        return
    
    if current_player == "O":
        next_player = "O"
        set_player_callback = next_player
    else:
        next_player = "X"
        set_player_callback = next_player
    