""" Lire la suite des prix (en euros entiers et terminée par zéro) des achats d’un client. Calculer la somme qu’il doit, lire la somme qu’il paye, et simuler la remise de la monnaie en affichant les textes "10 Euros", "5 Euros" et "1 Euro" autant de fois qu’il y a de coupures de chaque sorte à rendre.
"""

def addition(liste):
	s = 0
	for i in liste :
		s = s+ i
	s = float(s)
	print(s)
	#print(type(s)) #float
#l = [2, 2] #4
#addition(l)

def listeArticle():
	articles = []
	nb = float(input("entrez le prix d'un article : "))
	while nb > 0 or nb < 0 :
		articles.append(nb)
		nb = float(input("entrez le prix d'un article : "))
	articles.append(nb)
	addition(articles)
	#print(type(articles)) #liste
#listeArticle()

def remiseMonnaie(nb):
	while nb >= float(0.01):
		if nb >= 50:
			print ("billet 50 $")
			nb = nb -50
		elif nb >= 20:
			print("billet 20$")
			nb = nb - 20
		elif nb >= 10:
			print("10$")
			nb = nb - 10
		elif nb >= 2:
			print("pièce de 2$")
			nb = nb - 2
		elif nb >= 1:
			print("pièce de 1$")
			nb = nb -1
		elif nb >= 0.5:
			print("pièce de 0.5")
			nb = nb -0.5
		elif nb >= 0.2:
			print("pièce de 0.2")
			nb = nb -0.2
		elif nb >= 0.1:
			print(" pièce de 0.1")
			nb = nb -0.1
		elif nb >= 0.05:
			print("pièce de 0.05")
			nb = nb -0.05
		elif nb >= 0.02:
			print("pièce de 0.02")
			nb = nb -0.02
		elif nb >= 0.01:
			print("pièce de 0.01")
			nb = nb -0.01
			print(nb)
	print("Merci de votre visite")

#n = 45.54 #pbm
#n=20 #ok
#n = 21
#n = 0.01
#n= 20.11 #pbm
#remiseMonnaie(n)

def exoC():
	articles = listeArticle()
	remiseMonnaie(articles)

exoC()	

"""
 Variables E, somdue, M, Reste, Nb10E, Nb5E En Entier
Debut
E ← 1
somdue ← 0
TantQue E <> 0
  Ecrire "Entrez le montant : "
  Lire E
  somdue ← somdue + E
FinTantQue
Ecrire "Vous devez :", somdue, " euros"
Ecrire "Montant versé :"
Lire M
Reste ← M - somdue
Nb10E ← 0
TantQue Reste >= 10
  Nb10E ← Nb10E + 1
  Reste ← Reste – 10
FinTantQue
Nb5E ← 0
Si Reste >= 5
  Nb5E ← 1
  Reste ← Reste – 5
FinSi
Ecrire "Rendu de la monnaie :"
Ecrire "Billets de 10 E : ", Nb10E
Ecrire "Billets de  5 E : ", Nb5E
Ecrire "Pièces de 1 E : ", reste
Fin
"""
