import random  #importation de la bibiliothèque random 
class TicTacToe (object):  #création de la class TicTacToe de type object 

    def __init__(self,secondPlayer=False): #surcharge de la méthode constructeur __init__
        if secondPlayer :  #s'il y a un second joueur
            self._iaMode = False   #Pas de présence d'une IA
        else : #sinon, il n'y a qu'un seul joueur
            self._iaMode = True #on indique la présence d'une IA
        self._winningCombos = [[(0,0),(0,1),(0,2)],[(0,0),(1,0),(2,0)],[(0,0),(1,1),(2,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],[(0,2),(1,1),(2,0)]]   #Les combos gagnants
        self._gamePlate=[]

    def affiche(self,content):  #affichage du tableau de jeu
        for i in range(len(content)):
            contentLine = ""
            for j in range(len(content)):
                contentLine += content[i][j]
                contentLine += (" | ")
            print(contentLine)  

    
    def ticTacToeStart(self):   #Création du tableau 
        for i in range(3):
            self._gamePlate.append([])
            for _ in range (3) :
                self._gamePlate[i].append("*") #caractère montrant la case non choisi auparavant
        self.affiche(self._gamePlate) 
        
    
    def win(self,pointOwner): #annonces des vainqueurs
        if pointOwner == "X" :
            return "Player 1 Wins !"  #retourner le joueur 1 a gagné
        else :
            if self._iaMode :
                return "AI wins !"  #retourner le joueur 2 a gagné
            else :
                return "Player 2 wins !"

    def draw(self):
        return "That's a draw !"    

    def playerTurn(self):   #Les actions à faire du joueur 
        rowCoord=int(input("Please select a row number between 1 and 3 : "))-1
        assert rowCoord >= 0 and rowCoord <=2, "You're supposed to have chosen a number between 1 and 3..."
        colCoord=int(input("Please select a column number between 1 and 3 : "))-1
        assert colCoord >= 0 and colCoord <=2, "You're supposed to have chosen a number between 1 and 3..."
        return (rowCoord, colCoord)

    def botTurn(self) :   #Les actions à faire du bot
        botRowCoord=random.randint(0,2)   #le robot choisi une coordonnée horizontale aléatoire
        botColCoord=random.randint(0,2)   #le robot choisi une coordonnée verticale aléatoire
        return (botRowCoord, botColCoord)

    def ticTacToeGame(self):    #Le jeu commence 
        takenCoords=[]   #on initialise takenCoords qui enregistrons  les coordonées dans une liste vide 
        continuing=True   
        if self._iaMode :
            while continuing : #tant que personne ne gagne
                  
                self._playerCoords=self.playerTurn()
                if self._playerCoords in takenCoords:
                    print("You cannot pick this used space... try again")
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
                #print(takenCoords)
                self.affiche(self._gamePlate)
                if len(takenCoords) >=5 : # si la longueur de takenCoords est plus grand ou égal à 5 
                    for i in range(len(takenCoords)): #on parcourt le tableau takenCoords
                        savingItem = takenCoords[i] #on définit savingItem qui est la coordonnée que l'on regarde 
                        pointOwner = self._gamePlate[savingItem[0]][savingItem[1]] #on regarde à qui appartient cette coordonnée
                        listTaker = [] #on définit listTaker un tableau vide qui doit stocker le winning combo de la coordonée savingItem
                        pointsAligned = 1 #on définit pointsAligned qui vaut 1 (car il y a au moins un point aligné)
                        for j in range (len(self._winningCombos)) :
                            #print(savingItem)
                            if savingItem in self._winningCombos[j]: #si savingItem est une des trois coordonnées du winning combo
                                listTaker = self._winningCombos[j] #alors on assigne ce winningcombo à listeTaker
                            #print(listTaker)    
                            for k in range (j+1,len(takenCoords)-1): 
                                if takenCoords[k] in listTaker and self._gamePlate[takenCoords[k][0]][takenCoords[k][1]]==pointOwner: #si la coordonnée prise est dans listTaker et que la coordonnée appartient au pointOwner :
                                    pointsAligned += 1 #alors on a d'office un deuxième point aligné
                                    #print(pointsAligned)
                                    if pointsAligned == 3 : #si 3 points sont alignés (verticalement/horizontalement/diagonalement)
                                        continuing=False #la boucle s'arrête
                                        
            assert len(takenCoords) <= 9, "An internal error occured..."
            if len(takenCoords) == 9 and pointsAligned != 3 :
                self.draw()
                continuing=False                        
            return self.win(pointOwner)






game=TicTacToe()
game.ticTacToeStart()
game.ticTacToeGame()