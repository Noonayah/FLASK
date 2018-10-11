#coding: utf-8

from flask import Flask #importer le module du framework Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """<h1 style="color:#006666;font-family:Arial;">Bonjour les DevOps !</h1><p>Ca va la famille ? </p><img src="https://thumbs.gfycat.com/FrequentPaltryGalapagossealion-small.gif" />""" #ouvrir le navigateur et dans la barre URL taper : localhost:5000

@app.route('/patate')
def index1():
    return """<h1 style="color:#006666;font-family:Arial;">Bonjour les DevOps !</h1><p>De nos jours la vie est dure quand on est une petite patate. Qu'on soit mûre ou pas mûre il faut savoir tenir sur ses pattes. Alors mon ptit gars, si t'es une petite patate comme moi, écoute bien ces paroles, si tu ne veux pas passer à la casserole.</p>""" #ouvrir le navigateur et dans la barre URL taper : localhost:5000


if __name__ == "__main__":
    app.run(debug=True)

