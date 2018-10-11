#coding: utf-8
from flask import Flask

class Calculatrice:
	#constructeur
	def __init__(self,nombre1,nombre2):
		self.nombre1=nombre1
		self.nombre2=nombre2

	def multiplication(self):
		total = self.nombre1 * self.nombre2
		return total


def tableMutliplication(n):
	n1 = 0
	multi1 = Calculatrice(n,n1)
	while n1 <= 10:
		total = multi1.multiplication()
		#print(multi1.nombre1)
		#print(multi1.nombre2)
		n1 = n1 + 1
		multi1.nombre2 = n1
		x = total


print(tableMutliplication(1))

#app = Flask(__name__)

''''@app.route('/table1')
def index3():
	return "<h1>Table de multiplication</h1><br/><table><caption>Table de 1</caption>" + multiplicationtable() + "</table>"

#ouvrir le navigateur et dans la barre URL taper : localhost:5000

if __name__ == "__main__":
	app.run(debug=True)
'''