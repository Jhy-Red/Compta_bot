#! /usr/bin/python3

def nettoyage(texte, lower = True, upper = False):
    import re ; import string
    if lower is True:
        texte = texte.lower() # Miniscule
    
    if upper is True :    
        texte = texte.upper() # Majuscule
   
    texte = re.sub(f"[{string.punctuation}]", " ", texte) #Delete punctuation
    texte = re.sub("é|è|ê", "e", texte) #
    texte = re.sub("à|@|â", "a", texte) #
    texte = re.sub("ö|o|ô", "o", texte) # replace special character
    return texte

def recherche_clean(texte, col = 'Objet'): 
    clean = []
    for x in texte :
            clean.append(nettoyage(x['{col}'.format(col=col)]))
    return clean

class Reader : #read pcg

    def __init__(self,directory = None, header = None, column = "Texte"):
        path_pcg = "app/ressources/PCG lighted.xls"
        self.directory = directory
        self.header = header
        self.column = column
        if self.directory is None :
            self.path = path_pcg
        else :
            self.path = directory + path_pcg            


    def xls(self, clean = False ):
        from pandas import read_excel
        xls = read_excel(self.path,index_col = 0, header = self.header)
        
        if clean != False :
             xls[self.column] =  xls[self.column].apply(lambda x: nettoyage(x))

        return xls 

    def select(self, PCG, request, controle = False):
        
        if type(request) == int or request.isdigit() == True :
            filter = "^"
            axis = 0
            answer =  PCG.filter(regex=("{filter}{request}".format(request = request, filter = filter)), axis = axis)

        else :
            filter = ".*"
            request = nettoyage(request)
            answer = PCG[PCG[self.column].str.contains('({request}{filter})'.format(request = request, filter = filter), regex= True)]
            
            if controle is False :
                index = list(answer.index)
                answer = []
                for i in index :
                    answer = i

            #answer = PCG[PCG[self.column].str.extract(r'([{request}]{filter})'.format(request = request, filter = filter))] # IN PROGRESS
        return answer


class Mongod : #make request to find

    def __init__(self,database,collection=None, hostname = "localhost", port = 27017, enable_Docker = False ):

        if enable_Docker == True :
            hostname = "0.0.0.0"

        from pymongo import MongoClient
        self.client = MongoClient("mongodb://{hostname}:{port}".format(hostname=hostname,port=port))
        self.database = database
        self.collection = collection
        self.db = self.client[self.database]
        
        
    def request(self,operation= None, objet = None,tiers = None, init = True, direct = False) : # Fonction Recherche base de donnée pour trouver une correspondance
        cursor =self.db[self.collection]
        if init is True :
             cursor.create_index([('Objet','text')])      

        if operation == None and objet == None:
            requete  = cursor.find({},{"_id":0})

        if operation != None : 
            requete = cursor.find({"Operation": operation},{"_id":0})

            if objet != None :
                requete = cursor.find({"Operation" : operation, '$text': { "$search": objet }},{"_id":0})

                if tiers != None : 
                    requete = cursor.find({"Operation" : operation, '$text': { "$search": objet }, "Tiers" : tiers},{"_id":0})
            else :
                if tiers != None : 
                    requete = cursor.find({"Operation" : operation, "Tiers" : tiers},{"_id":0})

        resultat = []

        for x in requete :
            if direct is False :
                resultat.append(x)
            else :
                resultat.append(x['Montant'])
    
        return resultat
        

    def request_resultat(self): #Methode rapide, mais non filtrante
        cursor =self.db[self.collection]
        pipeline = [{"$group": {"_id": "$Operation", "sum": {"$sum": "$Montant"}}}]

        cursor = cursor.aggregate(pipeline)
        
        resultat = []

        for x in cursor :
            resultat.append(x['sum'])

        return resultat

    def howmuch(self):
        cursor = self.db[self.collection]
        return cursor.find().count() 


    def update(self,tiers = None, journal = None ,libelle = None , multiple = False): #base sur le journal = ok
        cursor = self.db[self.collection]

        if tiers != None :
            journal = None
            libelle = None
            request = {"Tiers": "{tiers}".format(tiers = tiers)}


        if journal != None :
            request = { "Operation": "{journal}".format(journal = journal)}
        
        if libelle != None : 
            libelle = nettoyage(libelle)
            request = {"Objets": "{libelle}".format(libelle = libelle)}

        compte = { "$set": { "Compte": "615" } } #fonction NLP à inscruter

        if multiple == False :
            cursor.update_one(request, compte)
            print("line added")
        else :
            cursor.update_many(request, compte)
            print("multiple line added")

    def update_test(self,tiers = None, journal = None ,libelle = None , compte = None, multiple = False): 
        cursor = self.db[self.collection]

        if tiers != None :
            journal = None
            libelle = None
            requete = self.request(operation = "AC", objet = tiers)
            #requete = {"Tiers": "{tiers}".format(tiers = tiers)} # should rework


        if journal != None :
            requete = { "Operation": "{journal}".format(journal = journal)} # should rework
        
        if libelle != None :
            requete = {"Objets": "{libelle}".format(libelle = libelle)} 
            #requete = request(objet = libelle) 

        compte = { "$set": { "Compte": "{compte}".format(compte=compte) } }
        
        if multiple == False :
            cursor.update_one(requete, compte)
            print("line added")
        else :
            cursor.update_many(requete, compte)
            print("multiple line added")


    def reader_cols(self,cols = "Objet", empty = True):
        cursor = self.db[self.collection]
        request = {"{cols}".format(cols=cols) : 1}

        if empty != True :
            research = {"Compte" : {"$exists" : False}}
        resultat = cursor.find({},request)

        liste = []

        for x in resultat :
            liste.append(x['{cols}'.format(cols=cols)])

        return liste

        
class comptabilise : # will translate into account number
    def __init__(self):
        pass