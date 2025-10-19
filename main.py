#setup
import tkinter as tk
from tkinter import messagebox
from helper import on_click

#main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("410x385")
root.resizable(0,0) #disables resizing

current_player = "X"
buttons = [[None for i in range (3)] for i in range (3)]

for i in range(3):
    for j in range(3):
        button = tk.Button(
            root,
            text="",
            font=("Arial", 24),
            width=7, height=4,
            command = lambda row=i, col=j: on_click(row, col, buttons, current_player)
        )
        button.grid(row=i, column=j)
        buttons[i][j] = button

#goes at end
root.mainloop()