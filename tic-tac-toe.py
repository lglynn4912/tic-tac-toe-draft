def make_board(spot1 = "", spot2 = "", spot3 = "", spot4 = "", spot5 = "",
spot6 = "", spot7 = "", spot8 = "", spot9 = ""):

    print(spot1 + " | " + spot2 + " | " + spot3)
    print("------")
    print(spot4 + " | " + spot5 + " | " + spot6)
    print("------")
    print(spot7 + " | " + spot8 + " | " + spot9)

    

class Player:
    
    def __init__(self, mark):
        self.mark = mark
        
    def goturn(self, spot):
        self.spot = spot

player1 = Player("X")
player1.goturn(2)

make_board(spot2=player1.mark)