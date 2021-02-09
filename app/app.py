#! usr/bin/python3

#region # Import 
from flask import Flask, render_template, request
from flask_pymongo import PyMongo

#endregion#

#region # Database information

hostname = 'localhost'
port = 27017
username = 'root'
password = 'root'
database = 'compta_DB'
collection = "documents"
#endregion#

#region # APP

app = Flask(__name__,template_folder="templates")
app.config["MONGO_URI"] = "mongodb://{ip}:{port}/{db}".format(ip = hostname, port = port , db = database)
app.config['MONGO_DBNAME'] = collection
app.config['SECRET_KEY'] = 'secret_key'

mongo = PyMongo(app)

#region# Fonction APP
@app.route('/')
def Welcome():
    from bot import Arsene
    launch = Arsene()
    return render_template("home.html", Arsene = launch)

@app.route('/', methods=['GET','POST'])
def Arsene():
    from bot import Arsene
    question = request.form['msg'] 
    return render_template("home.html",Arsene = Arsene(question))

@app.route('/formulaire')
def formulaire_NOSQL():
    return render_template("formulaire.html")

@app.route('/formulaire',methods=['POST'])
def formulaire_post_NOSQL():
    from tools import nettoyage

    date = request.form['date']
    op = request.form['op']
    tiers = nettoyage(request.form['tiers'],upper = True)
    objet = nettoyage(request.form['objet'],lower = False)
    montant = float(request.form['ttc'])
    currency = request.form['currency']
    justificatif = request.files['justificatif']

    #TODO should be auto-detect after machine learning
    if date == "":
        date = "2020/01/01"
    #TODO prevoir exeption si l'utilisateur supprime le 0 du montant

    reg_image = mongo.save_file(justificatif.filename,justificatif )
    reg_id = mongo.db[collection].insert_one( 
            {
                #'_id': TODO a definir,
                'Date': date,
                'Operation': op,
                'Tiers': tiers,
                'Objet': objet,
                'Montant': montant,
                'Devise': currency,
                'Justificatif': justificatif.filename,
            })

    return render_template("formulaire.html")

@app.route('/database')
def database_list():
    from tools import Mongod

    requete = Mongod(database,collection).request()
    
    return render_template("database.html",database=requete)


@app.route('/database',methods=['POST'])
def database_search():
    from tools import Mongod
    from tools import nettoyage

    op = request.form['op']
    tiers = nettoyage(request.form['tiers'],upper = True)
    objet = nettoyage(request.form['objet'],lower = False)

    if op != "" and tiers == "" and objet == "" :
        requete = Mongod(database,collection).request(operation = op)
    
    if op != "" and tiers != "" and objet == "" :
        requete = Mongod(database,collection).request(operation = op, tiers = tiers)
    
    if op != "" and tiers == "" and objet != "" :
        requete = Mongod(database,collection).request(operation = op, objet = objet)

    if op != "" and tiers != "" and objet != "" :
        requete = Mongod(database,collection).request(operation = op, tiers = tiers , objet = objet)
    
    return render_template("database.html",database=requete)

@app.route('/situation')
def situation():
    from tools import Mongod
    mongod = Mongod(database,collection)
    nombre = mongod.howmuch()

    depense = sum(mongod.request(operation = "AC",direct = True))
    ca = sum(mongod.request(operation = "VT",direct = True))

    return render_template("situation.html",CA = ca , depense = depense,resultat = ca - depense, nombre = nombre)
    
# Region en construction #### TODO Afficher une piece spécifique


@app.route('/img/<img_src>')
def img(img_src):
    return mongo.send_file(img_src)

# TODO fonction recherche spécifique
@app.route('/database-Research',methods=['POST'])
def database_Research():
    from tools import nettoyage

    op = request.form['op']
    tiers = nettoyage(request.form['tiers'],upper = True)
    objet = nettoyage(request.form['objet'],lower = False)
    return render_template("database-research.html", request = requete)
    #TODO should allow this in future : 
    #date = request.form['date']
    #montant = float(request.form['ttc'])

@app.route('/database-Research',methods=['GET'])
def database_Result():
    from tools import Mongod
    from tools import nettoyage

    operation = "request.form['op']"
    tiers = "nettoyage(request.form['tiers'],upper = True)"
    objet = "nettoyage(request.form['objet'],lower = False)"

    requete = Mongod(database,collection).request(operation= operation, objet = objet,tiers = tiers)
 
    return render_template("database-research.html", request = requete)
#endregion#

#region# Launch APP

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000, debug = True)
