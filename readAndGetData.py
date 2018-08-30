#Script de lecture d'un fichier
#le 02/07/2018 Par Oscar KALONJI
#Optique : Analyse de données
import os
#Positionnement dans le repertoire de travail
os.chdir("E:\\BIBLIOTHEQUE\\EXERCICE\\python")
liste = []
def getData(file):
    with open(file,"r") as openData:
        donne = openData.read()
        i = 0
        donne_ = donne.split('\n')
        for g in donne_:
            liste.append(g)
        return liste
def transformListeDic(a):
    dic = {}
    for e in a:
        print(e)



h = getData("liste.txt")
g = transformListeDic(h)
print(g)
            
            
