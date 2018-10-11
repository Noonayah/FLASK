def calculette(n1,n2):
	if operateur == '+' :
		resultat = n1 + n2

	if operateur == '-' :
		if n1>n2:
			resultat = n1 - n2
		else:
			resultat = n2 - n1

	if operateur == '*':
		resultat = n1 * n2

	if operateur == '/' :
		if n2>0 and n1>n2:
			resultat = n1 / n2
		elif n1>0 and n2>n1:
			resultat = n2 / n1
		else:
			print("Il est impossible de diviser par zéro")

	return resultat

print(calculette())

