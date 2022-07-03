from enum import Enum

class Strategy_Name(Enum):
    FARM = 1
    COME = 2
    CROSS = 3
    PARLEY = 4

class Parley():
    def __init__(self):
        self.five_hit = False
        self.nine_hit = False
class Come():
    def __init__(self):
        self.count = 4

class Strategy():
    def __init__(self):
        self.strat = Strategy_Name.FARM

    def get_strategy(self):
        return self.strat    
    def set_strategy(self, val):
        self.strat = val

    strat = property(lambda self: self.strat, set_strategy)

    def do_strategy(self, craps_game):
        if(self.strat == Strategy_Name.FARM):
            if(not craps_game.coverage and craps_game.field_hit and craps_game.point != 0):
                for idx in craps_game.table:
                    if(idx not in  ['field','pass', str(craps_game.point)] and craps_game.table[idx] == 0):
                        if(idx in ['4', '5', '9', '10']):
                            craps_game.place_bet([idx], 5)  
                        else:
                            craps_game.place_bet([idx], 6)
                        break 
            
                for idx in craps_game.table:
                    if(idx not in ['field', 'pass'] and craps_game.table[idx] == 0):
                        return

        if(self.strat == Strategy_Name.COME):
            craps_game.place_bet(["6", "8"], 6)  
            craps_game.place_bet(["come"], 5)
            return
        if(self.strat == Strategy_Name.CROSS):
            craps_game.place_bet(["4", "5","9", "10"], 5)  
            craps_game.place_bet(["6", "8"], 6)  
            return
        if(self.strat == Strategy_Name.PARLEY):
            parl = craps_game.get_parley()
            if(parl.five_hit):
                craps_game.place_bet(["6"], 6) 
            if(parl.nine_hit):
                craps_game.place_bet(["8"], 6) 
            if(not parl.five_hit and not parl.nine_hit \
                    and craps_game.table["5"] == 0 \
                    and craps_game.table["9" == 0]):    
                craps_game.place_bet(["5","9"], 5)  
            return