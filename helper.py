#setup
import tkinter as tk
from tkinter import messagebox

#def reset_board():
def check_winner(buttons):
    for i in range(3):
        #for rows
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"]!= "":
            return True
        #for columns
        if buttons[0][i]["text"] == buttons[i][1]["text"] == buttons[2][i]["text"]!= "":
            return True
        #diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"]!= "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"]!= "":
        return True
    return False

def check_draw(buttons):
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True

def reset_board(buttons,set_player_callback):
    for row in buttons:
        for button in row:
            button["text"] = ""
    set_player_callback("X")


def on_click(row, col, buttons, current_player, set_player_callback, reset_callback):
    # checks if box is already clicked
    if buttons[row][col]["text"] != "":
        return
    buttons[row][col]["text"] = current_player #set X or Y

    if check_winner(buttons):
        messagebox.showinfo(f"Game Over!\nPlayer {current_player} wins!")
        reset_callback()
        return
    
    if check_draw(buttons):
        messagebox.showinfo("Game Over! It's a draw!")
        reset_callback()
        return
    
    if current_player == "X":
        next_player = "O"
    else:
        next_player = "X"
    