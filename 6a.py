"""
Ecrire un algorithme qui déclare et remplisse un tableau de 7 valeurs numériques en les mettant toutes à zéro.
"""

def remplissageTableau ():
	tab=[]
	for i in range(7):
		i = 0
		tab.append(i)
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
#tableNote()

"""
Ecrivez un algorithme constituant un tableau, à partir de deux tableaux de même longueur préalablement saisis. Le nouveau tableau sera la somme des éléments des deux tableaux de départ.
"""

def additionTab (tab1, tab2):
	tab3 = []
	for i in range(len(tab1)):
		for j in range(1):
			nb = tab1[i] + tab2[i]
			tab3.append(nb)
	print(tab3)
l = [1, 2, 3, 4 ]
l2 = [5, 6, 7, 8]
#l2 = [5, 6]
#additionTab (l, l2) #ok

"""
Toujours à partir de deux tableaux précédemment saisis, écrivez un algorithme qui calcule le schtroumpf des deux tableaux. Pour calculer le schtroumpf, il faut multiplier chaque élément du tableau 1 par chaque élément du tableau 2, et additionner le tout. Par exemple si l'on a :
3 * 4 + 3 * 8 + 3 * 7 + 3 * 12 + 6 * 4 + 6 * 8 + 6 * 7 + 6 * 12 = 279
"""

def additionTab (tab1, tab2)
	somme = 0
	for i in range(len(tab1)):
		for j in range(len(tab2)):
			nb = tab1[i] * tab2[j]
			somme = nb + somme
	print(somme)

#l2 = [4, 8, 7, 12]
#l1 = [3, 6]
#additionTab (l2, l1)

