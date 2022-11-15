import random
class TicTacToe (object):

    def __init__(self,secondPlayer=False):
        if secondPlayer :
            self._iaMode = False
        else :
            self._iaMode = True
        self._winningCombos = [[(0,0),(0,1),(0,2)],[(0,0),(1,0),(2,0)],[(0,0),(1,1),(2,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],[(0,2),(1,1),(2,0)]]
        self._gamePlate=[]

    def affiche(self,content):
        for i in range(len(content)):
            contentLine = ""
            for j in range(len(content)):
                contentLine += content[i][j]
                contentLine += (" |")
            print(contentLine)
            print(" - "*(len(content)))    

    
    def ticTacToeStart(self):
        for i in range(3):
            self._gamePlate.append([])
            for _ in range (3) :
                self._gamePlate[i].append("▣")
        self.affiche(self._gamePlate) 
        
    
    def win(self,pointOwner):
        if pointOwner == "X" :
            return "Player 1 Wins !"
        else :
            if self._iaMode :
                return "AI wins !"
            else :
                return "Player 2 wins !"

    def draw(self):
        return "That's a draw !"    

    def playerTurn(self):
        rowCoord=int(input("Please select a row number between 1 and 3 : "))-1
        assert rowCoord >= 0 and rowCoord <=2, "You're supposed to have chosen a number between 1 and 3..."
        colCoord=int(input("Please select a column number between 1 and 3 : "))-1
        assert colCoord >= 0 and colCoord <=2, "You're supposed to have chosen a number between 1 and 3..."
        return (rowCoord, colCoord)

    def botTurn(self) :
        botRowCoord=random.randint(0,2)
        botColCoord=random.randint(0,2)
        return (botRowCoord,botColCoord)

    def ticTacToeGame(self):
        takenCoords=[]
        continuing=True
        if self._iaMode :
            while continuing :
                  
                self._playerCoords=self.playerTurn()
                if self._playerCoords in takenCoords:
                    print("You are supposed to pick free coords, not taken ones... do it again")
                    self._playerCoords=self.playerTurn()
                else :
                    takenCoords.append(self._playerCoords)
                
                self._gamePlate[self._playerCoords[0]].insert(self._playerCoords[1],"X")    
                
                self._botCoords=self.botTurn()
                
                if self._botCoords in takenCoords :
                    self._botCoords=self.botTurn()
                else :
                    takenCoords.append(self._botCoords)

                self._gamePlate[self._botCoords[0]].insert(self._botCoords[1],"O")
                print(takenCoords)
                self.affiche(self._gamePlate)
                if len(takenCoords) >=5 :
                    for i in range(len(takenCoords)):
                        savingItem = takenCoords[i]
                        pointOwner = self._gamePlate[savingItem[0]][savingItem[1]]
                        listTaker = []
                        pointsAligned = 1
                        for j in range (len(self._winningCombos)) :
                            if savingItem in self._winningCombos[j]:
                                listTaker = self._winningCombos[j]
                            for k in range (1,len(takenCoords)-1):
                                if takenCoords[k] in listTaker :
                                    pointsAligned += 1
                                    if pointsAligned == 3 :
                                        self.win(pointOwner)
                                        continuing=False
                assert len(takenCoords) <= 9, "An internal error occured..."
                if len(takenCoords) == 9 and pointsAligned != 3 :
                    self.draw()
                    continuing=False                        
            






game=TicTacToe()
game.ticTacToeStart()
game.ticTacToeGame()