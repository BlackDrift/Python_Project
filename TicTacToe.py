import random
class TicTacToe (object):

    def __init__(self,secondPlayer=False):
        if secondPlayer :
            self._iaMode = False
        else :
            self._iaMode = True
        self._winningCombos = [[(0,0)(0,1)(0,2)][(0,0)(1,0)(2,0)][(0,0)(1,1)(2,2)][(1,0)(1,1)(1,2)][(2,0)(2,1)(2,2)][(0,1)(1,1)(2,1)][(0,2)(1,2)(2,2)][(0,2)(1,1)(2,0)]]
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

    def playerTurn(self):
        rowCoord=int(input("Please select a row number between 1 and 3 : ") -1)
        assert self._rowCoord >= 0 and rowCoord <=2, "You're supposed to have chosen a number between 1 and 3..."
        colCoord=int(input("Please select a row number between 1 and 3 : ") -1)
        assert self._colCoord >= 0 and colCoord <=2, "You're supposed to have chosen a number between 1 and 3..."
        return (rowCoord, colCoord)

    def botTurn(self) :
        botRowCoord=random.randint(0,2)
        botColCoord=random.randint(0,2)
        return (botRowCoord,botColCoord)

    def ticTacToeGame(self):
        takenCoords=[]
        if self._iaMode :
            self._playerCoords=self.playerTurn()
            if self._playerCoords in self._takenCoords:
                print("You are supposed to pick free coords, not taken ones... do it again")
                self._playerCoords=self.playerTurn()
            else :
                self._takenCoords.append(self._playerCoords)
            self._gamePlate.insert(self._playerCoords,"X")    
            self._botCoords=self.botTurn()
            if self._botCoords in takenCoords :
                self._botCoords=self.botTurn()
            else :
                self._takenCoords.append(self._botCoords)
            self._gamePlate.insert(self._botCoords,"O")
            if len(takenCoords) >=6 :
                for i in range(len(self._takenCoords)):
                    savingItem = self._takenCoords[i]
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
            assert len(takenCoords) <= 9, "An internal error occured..."
            if len(takenCoords) == 9 and pointsAligned != 3 :
                self.draw()                        
            






game=TicTacToe(True)
game.ticTacToeStart()