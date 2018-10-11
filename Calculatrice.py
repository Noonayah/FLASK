
class Calculatrice:
	#attribut de classe
	compteur_objet = 0

	#constructeur
	def __init__(self,nombre1,nombre2):
		self.nombre1=nombre1
		self.nombre2=nombre2
		Calculatrice.compteur_objet +=1

	#méthodes
	def addition(self):
		total = self.nombre1+self.nombre2
		print(total)

	def soustraction(self):
		if self.nombre1 > self.nombre2:
			total = self.nombre1-self.nombre2
			print(total)
		else :
			total = self.nombre2 - self.nombre1
			print(total)

	def multiplication(self):
		total = self.nombre1*self.nombre2
		print(total)

	def divisionSimple(self):
		if self.nombre1 > self.nombre2 and self.nombre1 >= 0 and self.nombre2 > 0:
			total = self.nombre1/self.nombre2
			print(total)
		elif self.nombre1 == 0 and self.nombre2 > self.nombre1 :
			print("La division par 0 est impossible")
		elif self.nombre2 == 0 and self.nombre1 > self.nombre2:
			print("la division par 0 est impossible")
		else: 
			total = self.nombre2/self.nombre1
			print(total)


'''nombre1 = float(input("Entrez un premier nombre :\n"))
nombre2 = float(input("Entrez un second nombre :\n"))
operation = input("choisissez l'operation :\n")

c = Calculatrice(nombre1,nombre2)'''

'''def calcul():
	if operation == "addition" or operation == "+":
		c.addition()
	elif operation == "soustraction" or operation == "-":
		c.soustraction()
	elif operation == "multiplication" or operation == "*":
		c.multiplication()
	elif operation == "division" or operation == "/": 
		c.divisionSimple()
	else: 
		print("Il y a une erreur de saisie")
calcul()'''
