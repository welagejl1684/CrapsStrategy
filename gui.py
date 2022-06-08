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
        self.table = []
        self.time = 1000
        self.craps = craps.Craps(2)
        
        print(self.craps.get_table())
        self.textbox_table = tk.Text(self.window, width=75, height=25, bg='black', fg='green')
        self.textbox_table.insert(tk.INSERT, "pass: {0}, 4: {1}, 5: {2}, 6: {3}, 8: {4}, 9: {5}, 10: {6}, field: {7}".format(*self.craps.get_table()))
        self.textbox_table.pack()

        self.text_stats = tk.Text(self.window,  width=75, height=25, bg='black', fg='green')
        self.text_stats.insert(tk.INSERT, "bankroll: {0}, point: {1}, win: {2}, bet: {3}, rounds left: {4}".format(*self.craps.get_stats()))
        self.text_stats.pack()
        
        self.text_roll = tk.Text(self.window, width=75, height=25, bg='black', fg='green')
        self.text_roll.insert(tk.INSERT, "roll: {}".format(self.craps.get_roll()))
        self.text_roll.pack()
        
        self.window.after(self.time, self.display_game)
        self.window.mainloop()

    def display_game(self):
        self.craps.play_hand()
        print(self.craps.get_table())
        self.textbox_table.delete(1.0, tk.END)
        self.textbox_table.insert(tk.INSERT, "pass: {0}, 4: {1}, 5: {2}, 6: {3}, 8: {4}, 9: {5}, 10: {6}, field: {7}".format(*self.craps.get_table()))
        self.textbox_table.see(tk.END)
                
        self.text_stats.delete(1.0, tk.END)
        self.text_stats.insert(tk.INSERT, "bankroll: {0}, point: {1}, win: {2}, bet: {3}, rounds left: {4}".format(*self.craps.get_stats()))
        self.text_stats.pack()
        
        self.text_roll.delete(1.0, tk.END)
        self.text_roll.insert(tk.INSERT, "roll: {}".format(self.craps.get_roll()))
        self.text_roll.pack()
        
        self.window.after(self.time, self.display_game)
    

Client()

