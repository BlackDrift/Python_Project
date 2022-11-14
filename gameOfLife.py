"""class GameOfLife (object) :

    def __init__(self,x:int)->None : 
        self.tab=[]
        for i in range (x) :
            self.tab.append([])
            for _ in range(x) :
                self.tab[i].append(0)


    def gameInit(self,tab):


    def affiche(self):
        return self.tab        












test = GameOfLife(3)
print(test.affiche())"""


def CreateGrid(x:int)->list : 
    #on définit un tableau vide grid
    grid=[]
    #pour i allant de 0 à x
    for i in range (x) :
        #j'ajoute à la fin du tableau un tableau vide
        grid.append([])
        #pour une variable dont on se fout royal allant de 0 à x
        for _ in range(x) :
            #on ajoute en fin du sous-tableau d'index i un 0
            grid[i].append(0)
    #et on renvoie la matrice pleine de 0
    return grid


def uFormConfig(grid:list)->list :
    #on vérifie que la taille du tableau est suffisante pour pouvoir y insérer une forme en U.
    newGrid=grid
    if len(grid)%2 == 0 :
        x = len(grid)//4 - 1
        y = len(grid)//4 - 1
        for i in range(3):
            newGrid[x][y]=1
            x+=1
        for i in range(2):
            y+=1
            newGrid[x][y]=1    
        for i in range(2):
            x-=1
            newGrid[x][y]=1 
    else :
        x = len(grid)//2 - 1
        y = len(grid)//2 - 1
        for i in range(2):
            newGrid[x][y]=1
            x+=1
        for i in range(2):
            y+=1
            newGrid[x][y]=1    
        for i in range(2):
            x-=1
            newGrid[x][y]=1 
    return newGrid

test = CreateGrid(2)
print(test)
uFormConfig(test)
test2=CreateGrid(4)
print(test2)
test2 = uFormConfig(test2)
print(test2)