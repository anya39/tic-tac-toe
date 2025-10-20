#setup
import tkinter as tk
from tkinter import messagebox

#checks for win function
def check_winner(buttons):
    for i in range(3):
        #for rows
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"]!= "":
            return True
        #for columns
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"]!= "":
            return True
        #diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"]!= "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"]!= "":
        return True
    return False

#checks for draw function
def check_draw(buttons):
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True

#reset board function
def reset_board(buttons,set_player_callback):
    for row in buttons:
        for button in row:
            button["text"] = ""
    set_player_callback("X")

#when a button is clicked, checks if box is empty, checks for win, checks for draw, sets up next move
def on_click(row, col, buttons, current_player, set_player_callback, reset_callback):
    # checks if box is already clicked
    if buttons[row][col]["text"] != "":
        return
    buttons[row][col]["text"] = current_player #set X or Y

    if check_winner(buttons):
        messagebox.showinfo("Game Over",f"Game Over!\nPlayer {current_player} Wins!")
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
    set_player_callback(next_player)