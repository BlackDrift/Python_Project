from random import randint
def add(x,y):
    #on calcule la somme de x + y
    return x+y

def sub(x,y):
    #on calcule la différence entre x et y
    return x-y

def multiply(x,y):
    #on calcule le produit de x par y
    return x*y

def divide(x,y):
    #si y est différent de 0, alors on peut faire la division
    if y != 0 :
        #on effectue donc la division de x par y
        return x/y
    #sinon, bah diviser par 0 c'est le mal donc non en fait
    else :
        #du coup on renvoie rien parce que voilà
        raise ZeroDivisionError ("Diviser par 0 c'est le mal !")

def modulo(x,y):
    #on calcule le reste de la division euclidienne de x par y
    return x%y

def calculSalaireParSeconde(salaireHoraire, heureParJourOuvrable, jourOuvrable) :
    salaireAnnuel = salaireHoraire * heureParJourOuvrable * jourOuvrable #calcul du salaire annuel
    nbSecondeParAn = 365 * 24 * 60 * 60 #calcul du nombre de secondes par an (pour une année non bissextile)
    return salaireAnnuel / nbSecondeParAn #calcul du revenu par seconde obtenu en divisant le salaire annuel par le nombre de secondes dans une année

def salaire_net(salaireBrut, fonctionPublique=False):
    #est-ce que la personne est dans la fonction publique ?
    if fonctionPublique : 
        #si oui, son salaire net est égal à 85% du salaire brut, car 15% sont partis aux charges sociales et aux impôts
        return salaireBrut * 0.85 
    #sinon ? si le if ne s'active pas et qu'il n'y a pas déjà le précédent return, c'est que la personne n'est pas du secteur public, donc on renvoie bien la ligne qui suit dans tous les autres cas
    #le salaire net est égal à 77% du salaire brut, car les salariés qui ne sont pas de la fonction publique doivent 23% de ce dernier aux charges sociales et aux impôts
    return salaireBrut * 0.77

"""
DEBUT
 DEFINIR add(x, y) :
    RENVOYER x + y

 DEFINIR sub(x, y) :
    RENVOYER x - y

 DEFINIR multiply(x, y) :
    RENVOYER x * y

 DEFINIR divide(x, y) :
    RENVOYER x / y

 DEFINIR modulo(x, y) :
    RENVOYER x % y


FIN
"""

def input():
    #renvoie un caractère de type string au hasard
    listeLettres = "abcdefghijklmnopqrstuvwxyz"
    indiceLettre = randint(0, len(listeLettres)-1)
    return listeLettres[indiceLettre]
#Exercice :
    #faire un mini-jeu qui affiche un message lorsque input renvoie le bon caractère
    #le caractère doit être paramètrable

def akiLettre(lettre,nombreEssais=0):
    #on définit la lettre à deviner
    lettreADeviner = input()
    #on vérifie si les lettres sont différentes dans un premier temps
    
    while lettre != lettreADeviner :
        #on relance la fonction (appel récursif) 
        return akiLettre(lettre, nombreEssais + 1)
    #sinon, c'est que les lettres sont identiques, donc on renvoie le message de victoire
    return "Bien joué BG ! Tu as réussi ton coup en {nombreEssais} essais !"

def afficherMessage(chaine):
    return chaine

listUser = {"Alexandre" : "motdepasse", "Michel" : "password", "Toto" : "12345", "JhonDoe" : "azerty"}

def login(userName, password, listUser):
    if userName not in listUser.keys() :
        afficherMessage("Wrong username.")
    else :
        if password == listUser[userName]:
            afficherMessage("You're connected !")
        else :
            afficherMessage("Wrong password.")


tableau = [0, 10, 15, 5, 14, 7, 6 ,3, 4, 8, 4, 9, 5, 1, 7, 5, 2, 1, 8, 4, 4, 6, 8]

#Exercice :
    #faire une fonction qui concatène deux chaînes de caractères, les séparants par une virgule
    #faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaîne de caractères avec l'ensemble des occurences d'un chiffre

"""
DEBUT
DEFINIR concatene(chaineA, chaineB)

FIN DEFINIR
FIN
"""
#définir une fonction qui prend en paramètres : chaineA et chaineB deux chaînes de caractères
#et qui retourne la concaténation de chaineA, une virgule et enfin chaineB
def concatenation(chaine1, chaine2):
    #Je m'assure que chaineA soit bien de type str
    stringifiedChaineA = str(chaine1)
    #Je m'assure que chaineB soit bien de type str
    stringifiedChaineB = str(chaine2)
    return stringifiedChaineA + ", " + stringifiedChaineB

#définir une fonction qui prend une liste tableau et une variable x quelconque
def occurence(tableau, x):
    #Initialiser i à 0
    i=0
    #définir chaineResultat en tant que string vide
    chaineResultat=""
    #Tant que i est inférieur à la longueur de tableau
    """
    while i < len(tableau) :
    """
    for el in tableau :
        #alors si l'élément d'index i de tableau est égal à x
        """
        if tableau[i] == x:
        """
        if el == x :
            #alors on assigne à chaineResultat le retour de concatenation(chaineResultat, str(i))
            chaineResultat = concatenation(chaineResultat, str(i))
        #On incrémente i de 1
        i = i + 1  
    return chaineResultat

def occurence(tableau, x):
    #Initialiser i à 0
    i=0
    #définir chaineResultat en tant que string vide
    chaineResultat = ""
    #On détermine firstTurn à true
    firstTurn = True
    #Tant que i est inférieur à la longueur de tableau
    while i < len(tableau) :
        #alors si l'élément d'index i de tableau est égal à x
        if tableau[i] == x:
            #Si je suis au premier tour (Si firstTurn est true)
            if firstTurn :
                #Alors j'assigne str(i) a chaineResultat
                chaineResultat = str(i)
                #On passe firstTurn à false
                firstTurn = False
            #sinon on assigne à chaineResultat le retour de concatenation(chaineResultat, str(i))
            else :
                chaineResultat = concatenation(chaineResultat, str(i))
        #On incrémente i de 1
        i = i + 1  
    return chaineResultat    