"""
 Ecrivez un algorithme permettant à l’utilisateur de saisir un nombre quelconque de valeurs, qui devront être stockées dans un tableau. L’utilisateur doit donc commencer par entrer le nombre de valeurs qu’il compte saisir. Il effectuera ensuite cette saisie. Enfin, une fois la saisie terminée, le programme affichera le nombre de valeurs négatives et le nombre de valeurs positives.
"""

def ajout ():
	tableau = []
	n = int(input("Indiquez la longueur de votre tableau : "))
	nbrPositif = 0
	nbrNegatif = 0
	while len(tableau) < n :
		nb = int(input("Entrez des valeurs : ")) 
		tableau.append(nb)
	#print(tableau)
	for i in tableau : 
		if i > 0 :
			nbrPositif = nbrPositif + 1
		else:
			nbrNegatif = nbrNegatif + 1
	print("valeurs negatives : ", nbrNegatif, "Valeurs positives : ", nbrPositif)
#ajout ()
"""
Ecrivez un algorithme calculant la somme des valeurs d’un tableau (on suppose que le tableau a été préalablement saisi).
"""

def sommeListe (liste):
	somme = 0
	for i in liste :
		somme = somme +i
	print(somme)
#l = [5,5]#10
#sommeListe (l)

"""
Ecrivez un algorithme qui permette la saisie d’un nombre quelconque de valeurs, sur le principe de l’ex 6.8. Toutes les valeurs doivent être ensuite augmentées de 1, et le nouveau tableau sera affiché à l’écran.
"""
def makeNewTab ():
	tableau = []
	tableau1 = []
	n = int(input("Indiquez la longueur de votre tableau : "))
	while len(tableau) < n :
		nb = int(input("Entrez des valeurs : ")) 
		tableau.append(nb)
	for i in tableau :
		tableau1.append(i + 1)
	print(tableau1)
#makeNewTab ()
"""
Ecrivez un algorithme permettant, toujours sur le même principe, à l’utilisateur de saisir un nombre déterminé de valeurs. Le programme, une fois la saisie terminée, renvoie la plus grande valeur en précisant quelle position elle occupe dans le tableau. On prendra soin d’effectuer la saisie dans un premier temps, et la recherche de la plus grande valeur du tableau dans un second temps.
"""
def positionListe(nb, liste):
	position = 0
	for i in liste :
		position = position +1
		if i == nb in liste :
			pos = position			
		else :
			pass
	print ("Voici la position du plus grand :", pos)
#p = [5, 1, 9, 0]
#positionListe(9, p)

def tabMax ():
	tableau = []
	n = int(input("Indiquez la longueur de votre tableau : "))
	while len(tableau) < n :
		nb = int(input("Entrez des valeurs : ")) 
		tableau.append(nb)
	xMax = tableau[0]
	for i in tableau :
		if i > xMax :
			xMax = i 
		else:
			pass
	positionListe(xMax, tableau)	
	print( "le plus grand est : ", xMax)
tabMax ()



			

























