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
        return None

def modulo(x,y):
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