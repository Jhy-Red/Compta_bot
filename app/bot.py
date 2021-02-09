#!usr/bin/python3
import re

greeting = "Bonjour, que puis-je pour vous aujourd'hui ? "
aide = "Par defaut toutes vos demandes aboutiront a une sugestion de compte comptable"

bonjour = "Bonjour"
aurvoir = "bye"

erreur = "Je fais de mon mieux, mais je n'ai pas trouver !"
answers = "Yup"

question_nom = r"nom|comment t'apelle tu ?"
reponse_nom = "Arsene Lapin !"
def Arsene_Python(flag = True):
    from tools import nettoyage
    print(greeting)

    
    while (flag == True):
        question = input("> ")
        texte = nettoyage(question)
        if (re.search(aurvoir, texte)):
            flag = False
            print(aurvoir)
        else :
            print("Yup")

def Arsene(message = None):
    from tools import nettoyage
    from tools import Reader

    PCG = Reader(header = 2).xls(clean = True)

    if message is None :
        return greeting

    texte = nettoyage(message)

    if (re.search(aurvoir, texte)):
        return aurvoir

    elif (re.search("help",texte)):
        return aide

    elif (re.match(question_nom,texte)):
        return reponse_nom

    else :
        reponse = Reader().select(PCG = PCG, request = texte) 
        if reponse ==  []:
            
            return erreur
        else :
            return message + " correspond au compte :" + str(reponse)