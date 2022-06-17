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
        self.window.geometry("500x500")
        self.time = 2500
        self.craps = craps.Craps(10)
        self.rolls = []
        self.win_tracker = 0
        
        self.table = "pass: {0}\t\t 4: {1}\n5: {2}\t\t 6: {3}\n8: {4}\t\t 9: {5}\n10: {6}\t\t field: {7}\n\t ROLL: {8}"
        self.stats = "bankroll: {0}\npoint: {1}\nwin: {2}\nbet: {3}\nrounds left: {4}"
        self.rolls_tracker = " " 
        
        self.textbox_table = tk.Text(self.window, font="Helvetica 12", width=75, height=15, bg='black', fg='green')
        self.textbox_table.tag_configure("bold")
        self.textbox_table.insert(tk.INSERT, self.table.format(*self.craps.get_table() + [0]))
        self.textbox_table.pack()

        self.textbox_rolls = tk.Text(self.window, font="Helvetica 12", width=75, height=5, bg='black', fg='green')
        self.textbox_rolls.tag_configure("bold")
        self.textbox_rolls.insert(tk.INSERT, self.rolls_tracker.format(self.rolls))
        self.textbox_rolls.pack()

        self.text_stats = tk.Text(self.window, font="Helvetica 12", width=75, height=10, bg='black', fg='green')
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
        

        if(self.craps.get_roll() == 7 and win_amt < self.win_tracker):
            playsound('sounds/bigred.mp3')

        self.update()

        self.window.after(self.time, self.display_game)
    
    def update(self):   
        self.textbox_table.delete(1.0, tk.END)
        self.textbox_table.insert(tk.INSERT, self.table.format(*self.craps.get_table() + [self.craps.get_roll()]))
        self.textbox_table.see(tk.END)
        self.textbox_table.pack()
        
        self.rolls.append(self.craps.get_roll())
       
        self.textbox_rolls.delete(1.0, tk.END)
        self.textbox_rolls.insert(tk.INSERT, self.rolls_tracker.join(map(str, [*self.rolls])))
        self.textbox_rolls.pack()

        self.text_stats.delete(1.0, tk.END)
        self.text_stats.insert(tk.INSERT, self.stats.format(*self.craps.get_stats()))
        self.text_stats.pack()

Client()

