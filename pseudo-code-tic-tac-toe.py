# DEBUT 

# On définit une classe TicTacToe, un objet qui va représenter complètement une partie de Morpion :

    # On définit une méthode __init__, surcharge de la méthode constructrice du même nom, qui prend en paramètres self, et secondPlayer un booléen qui vaut par défaut False :
        # On vérifie si secondPlayer est égal à True :
            # Alors
            # On met la variable self._iaMode à False, il y a donc deux joueurs, ce sera donc un JcJ
        #Sinon
            # Alors
            # On met la variable self._iaMode à True, il n'y a qu'un joueur, ce sera donc un JcB

    # On définit une fontion ticTacToeStart qui prend self comme paramètre et renverra une liste:
        # On définit un tableau self._gamePlate vide
        # On parcourt ensuite pour i allant de 0 à 2 :
            # On ajoute un tableau vide à la fin du tableau self._gamePlate
            # On parcourt ensuite pour une variable quelconque allant de 0 à 2 :
                # On ajoute une chaine de caractères vide à la fin du tableau d'index i
        # On renvoie le tableau self._gamePlate

    # On définit une fonction ticTacToeGame qui prend comme paramètre self et simulera pas à pas une partie de Morpion :
        # 





#FIN