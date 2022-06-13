from cgitb import text
from tkinter import simpledialog, Scrollbar
from playsound import playsound

import tkinter as tk
import threading
from turtle import color
import schedule
import craps
import time 

class Client():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x450")
        self.time = 3000
        self.craps = craps.Craps(10)
        self.table = "pass: {0}, 4: {1}\n5: {2}, 6:{3}\n8: {4}, 9: {5}\n10: {6}, field: {7}\n\t\t ROLL: {8}"
        self.stats = "bankroll: {0}\npoint: {1}\nwin: {2}\nbet: {3}\nrounds left: {4}"
        self.win_tracker = 0

        self.textbox_table = tk.Text(self.window, width=75, height=20, bg='black', fg='green')
        self.textbox_table.insert(tk.INSERT, self.table.format(*self.craps.get_table() + [0]))
        self.textbox_table.pack()

        self.text_stats = tk.Text(self.window,  width=75, height=10, bg='black', fg='green')
        self.text_stats.insert(tk.INSERT, self.stats.format(*self.craps.get_stats()))
        self.text_stats.pack()
        
        self.update()
        playsound('sounds/diceroll.wav')
        self.craps.play_hand()

        self.window.after(self.time, self.display_game)
        self.window.mainloop()

    def display_game(self):  
        playsound('sounds/diceroll.wav')
        self.craps.play_hand()
        
        win_amt = self.craps.get_stats()[2]
        if(win_amt > self.win_tracker):
            self.win_tracker = win_amt
            playsound('sounds/burr.wav')
        

        if(self.craps.get_roll() == 7):
            playsound('sounds/bigred.mp3')

        self.update()

        self.window.after(self.time, self.display_game)
    
    def update(self):   
        self.textbox_table.delete(1.0, tk.END)
        self.textbox_table.insert(tk.INSERT, self.table.format(*self.craps.get_table() + [self.craps.get_roll()]))
        self.textbox_table.see(tk.END)
        self.textbox_table.pack()

        self.text_stats.delete(1.0, tk.END)
        self.text_stats.insert(tk.INSERT, self.stats.format(*self.craps.get_stats()))
        self.text_stats.pack()

Client()

