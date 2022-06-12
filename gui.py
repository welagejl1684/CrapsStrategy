from cgitb import text
from tkinter import simpledialog, Scrollbar
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
        self.time = 3000
        self.craps = craps.Craps(10)
        self.table = "pass: {0}, 4: {1}, 5: {2}, 6: {3}, 8: {4}, 9: {5}, 10: {6}, field: {7} \n\t\t\t ROLL: {8}"
        self.stats = "bankroll: {0}, point: {1}, win: {2}, bet: {3}, rounds left: {4}"
        
        self.textbox_table = tk.Text(self.window, width=75, height=20, bg='black', fg='green')
        self.textbox_table.insert(tk.INSERT, self.table.format(*self.craps.get_table() + [0]))
        self.textbox_table.pack()

        self.text_stats = tk.Text(self.window,  width=75, height=10, bg='black', fg='green')
        self.text_stats.insert(tk.INSERT, self.stats.format(*self.craps.get_stats()))
        self.text_stats.pack()
        
        self.window.after(self.time, self.display_game)
        self.window.mainloop()

    def display_game(self):
        self.craps.play_hand()
        self.textbox_table.delete(1.0, tk.END)
        self.textbox_table.insert(tk.INSERT, self.table.format(*self.craps.get_table() + [self.craps.get_roll()]))
        self.textbox_table.see(tk.END)
                
        self.text_stats.delete(1.0, tk.END)
        self.text_stats.insert(tk.INSERT, self.stats.format(*self.craps.get_stats()))
        self.text_stats.pack()
        
        self.window.after(self.time, self.display_game)
    

Client()

