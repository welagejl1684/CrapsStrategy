import sys 
import random
import time

class Craps(): 
    def __init__(self, rounds):
        self.table = {
            'pass': 0, '4':0, '5':0, '6':0, '8':0, 
            '9':0, '10':0, 'field':0
        }

        self.bank_roll = 100 
        self.point = 0
        self.win = 0
        self.bet = 0 
        self.roll = 0
        self.rounds = rounds 
        self.coverage = False
        self.field_hit = False 

        seed_value = random.randrange(sys.maxsize)
        random.seed(seed_value)
        self.play_hand()

    def place_bet(self, pos, amount):
        for idx in pos:  
            self.table[idx] = self.table[idx] + amount 
            self.bank_roll = self.bank_roll - amount 
            self.bet = self.bet + amount 

    roll_dice = lambda self: random.randint(2, 12)  
    
    get_table = lambda self: [self.table[idx] for idx in self.table]
    
    get_roll = lambda self: self.roll

    def get_stats(self):
        return [self.bank_roll, self.point, self.win, self.bet, self.rounds]

    def before_point(self):
        self.place_bet(['pass'], 10)
        self.roll = self.roll_dice()
        print("start")
        if(self.roll in [7,11]):
            self.bank_roll = self.bank_roll + self.table['pass']
        if(self.roll not in [2,3,7,11,12]):
            self.point = self.roll  
            self.place_strat()
        
        self.table['pass'] = 0 

    def after_point(self): 
        self.next_roll = False
        
        self.roll = self.roll_dice()
        self.payout(self.roll)
        if(not self.coverage and self.field_hit and self.point != 0):
            self.field_farm()
              
    
    def payout(self, roll):
        if(roll == 7):
            self.restart(False)
            return 
        
        if(roll in [4,10]):
            self.win = self.win + (self.table[str(roll)] / 5 ) * 9
            self.bank_roll = self.bank_roll + (self.table[str(roll)] / 5) * 9 
            
        elif(roll in [5,9]):
            self.win = self.win + (self.table[str(roll)] / 5) * 7
            self.bank_roll = self.bank_roll + (self.table[str(roll)] / 5) * 7
            self.table['field'] = 0  

        elif(roll in [6,8]):
            self.win = self.win + (self.table[str(roll)] / 6) * 7
            self.bank_roll = self.bank_roll + (self.table[str(roll)] / 6) * 7

        if(roll in [2,12]):
            self.field_hit = self.table['field'] != 0  
            self.bank_roll = self.bank_roll + self.table['field'] * 3 
            self.win = self.win + self.table['field'] * 3        
            self.table['field'] = 0 

        if(roll in [4,9,10,11]):
            self.field_hit = self.table['field'] != 0  
            self.bank_roll = self.bank_roll + self.table['field'] * 2 
            self.win = self.win + self.table['field'] * 2
            self.table['field'] = 0
        
        if(roll == self.point):
            self.bank_roll = self.bank_roll + self.table['pass'] * 2 
            self.restart(True)

    def field_farm(self):
        for idx in self.table:
            if(idx not in  ['field','pass'] and self.table[idx] == 0):
                if(idx in ['4', '5', '9', '10']):
                    self.place_bet([idx], 5)  
                else:
                    self.place_bet([idx], 6)
                break 
        
        for idx in self.table:
            if(self.table[idx] == 0):
                return

        self.coverage = True         

    def place_strat(self):
        self.place_bet(['field'], 5) 
        if(self.point in [4,5,9,10]): 
            self.place_bet(['6','8'], 6)
        
        if(self.point == 6): 
            choice_bet = ['4','5','9','10']
            self.place_bet([random.choice(choice_bet)], 5)
            self.place_bet(['8'], 6)

        if(self.point == 8):
            choice_bet = ['4','5','9','10']
            self.place_bet([random.choice(choice_bet)], 5)
            self.place_bet(['6'], 6)
    
    def restart(self, win):
        self.win = 0
        self.bet = 0
        self.point = 0 
        self.coverage = False 
        self.rounds = self.rounds - 1

        if(win):
            for idx in self.table:
                self.bank_roll = self.bank_roll + self.table[idx] 
            
            choice = random.randint(0, 50)
            if(choice > 40):
                self.place_bet(['pass'], 5)
        
        for idx in self.table:
            self.table[idx] = 0 
    
        self.play_hand()
    
    def play_hand(self):
        if(self.rounds == 0):
            return

        if(self.point != 0):
            self.after_point()
        else:
            self.before_point()    
        
        if(self.bank_roll <= 0):
            print("FAILURE")
            return
             
