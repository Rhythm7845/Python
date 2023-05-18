class Player:  
    def __init__(self, name, run_rate, matches):  
        self.name = str(name)
        self.runRate = int(run_rate)
        self.matches = int(matches)
    def showStats(self):
        print(self.name, self.runRate, self.matches)
        
kush = Player("kush", 1000, 2)
kush.showStats()

shubh = Player("Shubh", 1, 999)
shubh.showStats()

Team_CSK = {kush, shubh}
