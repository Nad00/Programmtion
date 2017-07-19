"""
Ecrire un algorithme qui déclare et remplisse un tableau de 7 valeurs numériques en les mettant toutes à zéro.
"""

def remplissageTableau ():
	tab=[]
	for i in range(7):
		i = 0
		tab.append(i)
	print(tab)
remplissageTableau ()

"""	
Ecrire un algorithme qui déclare et remplisse un tableau contenant les six voyelles de l’alphabet latin.		
"""		
#JE SAIS PAS
	
"""
Ecrire un algorithme qui déclare un tableau de 9 notes, dont on fait ensuite saisir les valeurs par l’utilisateur.
"""

def tableNote():
	note = []
	s = 0
	for i in range(9):
		i = int(input("Entrez les notes : "))
		note.append(i)
		somme = s + i
	#print(note)
	#print(note[2])
	moyenne = somme/len(note)
	print(moyenne)
	print(len(note))		
tableNote()


