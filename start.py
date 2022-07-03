from cgitb import text
from xmlrpc.client import Boolean
from playsound import playsound 
from strategy import Strategy_Name
import tkinter as tk
from turtle import color
import board
from tkinter import messagebox
 
class Options():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x300")
        self.window.configure(bg="black")
        self.window.title("Play Options")

        self.options_list = ["Farm", "Come", "Cross", "Parley"]

        self.o_strat = tk.StringVar()
        self.label_strat = tk.StringVar()
        self.label_betting_amount = tk.StringVar()
        self.label_rounds = tk.StringVar()
        self.bet_amount = tk.StringVar()
        self.rounds = tk.StringVar()
        self.disable_sound = tk.IntVar()
        
        self.label_strat.set("Betting Strategy: ")
        self.l_strategy = tk.Label(self.window, textvariable=self.label_strat, height=4)
        self.l_strategy.configure(bg="black", fg="green")
        self.l_strategy.grid(row=1,column=1)
        
        self.o_strat.set("Select an Option")
        self.q_menu = tk.OptionMenu(self.window, self.o_strat, *self.options_list)
        self.q_menu.configure(bg="black", fg="green")
        self.q_menu.grid(row=1, column=2)

        self.label_betting_amount.set("  Set amount to bet: ")
        self.l_bet = tk.Label(self.window, textvariable=self.label_betting_amount, height=4)
        self.l_bet.configure(bg="black", fg="green")
        self.l_bet.grid(row=2,column=1)
        
        self.e_amount = tk.Entry(text=self.bet_amount)
        self.e_amount.configure(bg="black", fg="green")
        self.e_amount.grid(row=2,column=2)
        self.e_amount.delete(0, 'end')

        self.label_rounds.set("  Set number of rounds: ")
        self.l_round = tk.Label(self.window, textvariable=self.label_rounds, height=4)
        self.l_round.configure(bg="black", fg="green")
        self.l_round.grid(row=3,column=1)
        
        self.e_rounds = tk.Entry(text=self.rounds)
        self.e_rounds.configure(bg="black", fg="green")
        self.e_rounds.grid(row=3,column=2)
        self.e_rounds.delete(0, 'end')

        self.c_disable_sound = tk.Checkbutton(self.window, text="Disable Sound",variable=self.disable_sound, onvalue=1, offvalue=0)
        self.c_disable_sound.configure(bg="black",fg="green")
        self.c_disable_sound.grid(row=4,column=2)
       
        self.b_continue = tk.Button(self.window, text ="PLAY!", width = 2, height=1, command = self.start)
        self.b_continue.configure(bg="black",fg="green")
        self.b_continue.grid(row=7,column=1)

        self.window.mainloop()
    
    def start(self):
        if(self.validate(self.bet_amount) and self.validate(self.rounds)):
            self.window.destroy()
            board.Board(self.rounds.get(), self.bet_amount.get(), self.strat_enum(), self.disable_sound.get())

    def strat_enum(self):
        val = self.o_strat.get()
        if val == "Farm":
            return Strategy_Name.FARM
        if val == "Come":
            return Strategy_Name.COME
        if val == "Cross":
            return Strategy_Name.CROSS
        if val == "Parley":
            return Strategy_Name.FARM

    def validate(self, var) -> Boolean:
        value = str(var.get())
        if not value.isdigit():
            return False
        return True

Options()        
