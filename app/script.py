#! /usr/bin/python3

from tools import Reader, Mongod,recherche_clean
from pprint import pprint
path= "/media/jhy/JHY/Projet/Simplon/Projet Final/"


PCG = Reader(header = 2).xls(clean = True)
#pprint(PCG)

database = 'compta_DB'
collection = "documents"
mongod = Mongod(database,collection)
