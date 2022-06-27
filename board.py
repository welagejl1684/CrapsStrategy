from cgitb import text
from playsound import playsound
import tkinter as tk
import craps

class Board():
    def __init__(self, rounds, bankroll, strategy, sound):
        self.window = tk.Tk()
        self.window.geometry("1000x500")
        self.window.configure(background="black")
        self.colors = ["pink", "green", "yellow", "red"]

        self.time = 2500
        self.craps = craps.Craps(rounds, bankroll, strategy)
        self.disable_sound = sound
        
        self.rolls_var = tk.StringVar()
        self.stats_var = tk.StringVar()
        self.win_tracker = 0
        self.bet_var = []
        self.board_gui = []
        self.rolls_tracker = {
            2: [],3: [],4: [],5: [],6: [],7: [],
            8: [],9: [],10: [],11: [],12: []
        }

        self.rolls_string = "2: {0}\n 3: {1}\n 4: {2}\n 5: {3}\n 6: {4}\n 7: {5}\n 8: {6}\n 9: {7}\n 10: {8}\n 11: {9}\n 12: {10}"
        self.board_var = ["PASS:","4:","5:","6:","8:","9:","10:","FIELD:","COME:"]
        self.stats = "BANKROLL: {0} \nPOINT: {1}\n WIN: {2}\n BET: {3}\n ROUNDS LEFT: {4}"
        
        self.create_frames()
        self.set_board()
        self.update()
        
        if(not self.disable_sound):
            playsound('sounds/diceroll.wav')
        
        if(self.craps.get_is_done()):
            return

        self.craps.play_hand()

        self.window.after(self.time, self.display_game)
        self.window.mainloop()

    def display_game(self):  
        if(not self.disable_sound):
            playsound('sounds/diceroll.wav')
        
                
        if(self.craps.get_is_done()):
            return
        self.craps.play_hand()
        
        win_amt = self.craps.get_stats()[2]
        if(win_amt > self.win_tracker):
            self.win_tracker = win_amt
            if(not self.disable_sound):
                playsound('sounds/burr.wav')
        

        if(self.craps.get_roll() == 7 and win_amt < self.win_tracker):
            if(not self.disable_sound):
                playsound('sounds/bigred.mp3')

        self.update()

        self.window.after(self.time, self.display_game)
    
    def update(self):   
        table = self.craps.get_table()
        is_resesting = self.craps.get_is_reseting()

        for idx in range(0, len(self.board_gui)):
            place, bet = self.board_gui[idx]
            bet.set(table[idx])

        self.update_roll_tracker()
        self.update_stats(is_resesting)
        return

    def update_roll_tracker(self):
        temp = []
        reset = False

        for idx in self.rolls_tracker:
            if(len(self.rolls_tracker[idx]) >= 25):
                reset = True

        if reset:
            for idx in self.rolls_tracker:
                self.rolls_tracker[idx] = []
            for idx in self.rolls_tracker:
                temp.append(''.join(self.rolls_tracker[idx])) 
        else:
            self.rolls_tracker[self.craps.get_roll()].append("*")
            for idx in self.rolls_tracker:
                temp.append(''.join(self.rolls_tracker[idx])) 
            
        rolls = self.rolls_string.format(*temp)
        self.rolls_var.set(rolls)

    def update_stats(self, reset):
        if reset:
            self.win_tracker = 0

        stat = self.stats.format(*self.craps.get_stats())
        self.stats_var.set(stat)

    def set_board(self):
        count = 0
        for idx in self.board_var: 
            place = tk.StringVar()
            bet_v = tk.IntVar(value=0)
            place.set(idx)
            
            l = tk.Label(self.table_frame, textvariable=place, height=3, width=5)
            l.configure(bg="black", fg=self.colors[3])
            l.grid(row=1,column=count)
            
            l2 = tk.Label(self.table_frame, textvariable=bet_v, height=3,width=3)
            l2.configure(bg="black", fg="green")
            l2.grid(row=1,column=count + 1)
            
            count = count + 2
            self.board_gui.append((place, bet_v))
            
        self.textbox_rolls = tk.Label(self.roll_frame, textvariable=self.rolls_var, bg='black', fg='green')
        self.textbox_rolls.grid(row=1, column=1)
        self.update_roll_tracker()

        self.text_stats = tk.Label(self.stats_frame, textvariable = self.stats_var, bg='black', fg='green')
        self.text_stats.grid(row=1, column=1)
        self.update_stats(False)

    def create_frames(self):
        self.table_frame = tk.Frame(self.window)
        self.table_frame.pack()
        self.roll_frame = tk.Frame(self.window)
        self.roll_frame.pack()
        self.stats_frame = tk.Frame(self.window)
        self.stats_frame.pack()

