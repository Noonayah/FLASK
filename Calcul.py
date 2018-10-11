from flask import Flask
#Lancement de l'application FLask:
app = Flask(__name__)

#Création des fonctions de calcul types de la calculatrice :
def addition(nb1,nb2):
    total = nb1 + nb2
    return str(total)

def multiplication(nb1,nb2):
    total = nb1*nb2
    return str(total)

def soustraction(nb1,nb2):
    total = nb1-nb2
    return str(total)

def divisionSimple(nb1,nb2):
    if nb1 == 0 and nb2 > nb1:
        fail = "La division par 0 est impossible"
        return fail
    elif nb2 == 0 and nb1 > nb2:
        fail = "la division par 0 est impossible"
        return fail
    else:
        total = nb1 / nb2
        return str(total)

#Paramétrage des routes:
#On définit ici la vue : en fonction de la chaine entrée en paramètre, le programme utilise la fonction de calcul qui lui correspond
#et on détermine le texte.
@app.route('/<chaine>-<int:nb1>-<int:nb2>/')
def index(chaine,nb1,nb2):
    title="""<h1 style="text-align:center;">Calculatrice</h1>"""
    if chaine == "somme":
        return title+"<p>La somme de "+str(nb1)+" et "+str(nb2)+" vaut "+addition(nb1,nb2)+"</p>"
    if chaine == "multiplication":
        return title+"<p>La multiplication de "+str(nb1)+" et "+str(nb2)+" vaut "+multiplication(nb1,nb2)+"</p>"
    if chaine == "soustraction":
        return title+"<p>La soustraction de "+str(nb1)+" et "+str(nb2)+" vaut "+soustraction(nb1,nb2)+"</p>"
    if chaine == "division":
        return title+"<p>Le résultat de la division de "+str(nb1)+" et "+str(nb2)+" est : "+divisionSimple(nb1,nb2)+"</p>"



if __name__ == "__main__":
	app.run(debug=True)