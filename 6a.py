"""
Ecrire un algorithme qui déclare et remplisse un tableau de 7 valeurs numériques en les mettant toutes à zéro.
"""

def remplissageTableau ():
	tab=[]
	for i in range(7):
		tab.append(0)
	print(tab)
#remplissageTableau ()

"""	
Ecrire un algorithme qui déclare et remplisse un tableau contenant les six voyelles de l’alphabet latin.		
"""		
#JE SAIS PAS
	
"""
Ecrire un algorithme qui déclare un tableau de 9 notes, dont on fait ensuite saisir les valeurs par l’utilisateur.
"""

def tableNote():
	note = []
	for i in range(9):
		nb = int(input("Entrez les notes : "))
		note.append(nb)
	#print(note)
	print(note[2])
tableNote()
