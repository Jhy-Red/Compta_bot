#! /usr/bin/python3

from tools import Reader, Mongod, recherche_clean
from pprint import pprint
path= "/media/jhy/JHY/Projet/Simplon/Projet Final/"
PCG = Reader(header = 2).xls(lower = True)

database = 'compta_DB'
collection = "documents"
mongod = Mongod(database,collection)

#print(PCG)
#print(Reader.select(PCG,6))
#all_in = Mongod(database,collection).request()
#achat = Mongod(database,collection).request("AC")
#update = Mongod(database,collection).update(column = "Operation", critere = "AC",multiple = True )

#get_field = Mongod(database,collection).reader_cols(cols = "Objet", empty = False)
###pdf = "edf-1.pdf"
###files = Reader(directory=path + "app/ressources"/).pdf(pdf)
###print(files)

#PCG[PCG['Texte'].str.contains("eau")]
#pprint(Reader().select(PCG = PCG,request = "électricité", controle = True))


#pprint(mongod.request())
pprint(mongod.request(operation = "AC", objet = "Consomation electricité"))

texte = mongod.request(operation = "AC", objet = "electricité")
pprint(recherche_clean(texte))

#Mongod(database,collection).update(column = "Operation", critere = "AC",multiple = True )


#PCG = Reader(header = 2).xls(lower = True).select(request = "éléctricité") a controller

# texte = mongod.request(operation = "AC", objet = "electricité") working 
texte = mongod.request(operation = "AC", objet = 'electricité', tiers = 'EDF')
#texte = mongod.request(operation = "AC",objet = "electricite")

pprint(texte)

# if recherche_clean(texte) match pcg
# Mongod(database,collection).update(column = "Objet", critere = texte,multiple = True )


#mongod.update_test(libelle = texte, multiple = True, compte = 699)



#pprint(mongod.request())

#Mongod(database,collection).update(column = "Operation", critere = "AC",multiple = True )


#PCG = Reader(header = 2).xls(lower = True).select(request = "éléctricité") a controller

# texte = mongod.request(operation = "AC", objet = "electricité") working 
texte = mongod.request(operation = "AC", objet = 'electricité', tiers = 'EDF')
#texte = mongod.request(operation = "AC",objet = "electricite")

pprint(texte)

# if recherche_clean(texte) match pcg
# Mongod(database,collection).update(column = "Objet", critere = texte,multiple = True )


#mongod.update_test(libelle = texte, multiple = True, compte = 699)

#a = mongod.request_resultat_test()
#a = mongod.howmuch()


a = mongod.request(operation = "AC",direct = True)
print(a)
print(sum(a))