# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 16:33:56 2026

@author: mitsu
"""

import csv
import numpy as np 
import matplotlib.pyplot as plt

with open("meilleur-chemin-nbr-fourmis.csv", "r", encoding="utf-8") as fichier:
    reader = csv.reader(fichier)

    next(reader)  # saute l'en-tête
    NBR_fourmis=[]
    meilleur_chemin = []
    temps_execution=[]
    for ligne in reader:
        NBR_fourmis.append(round(float(ligne[0])))
        meilleur_chemin.append(round(float(ligne[1])))
        temps_execution.append(round(float(ligne[2])))

    NBR_fourmis=np.array(NBR_fourmis)
    meilleur_chemin=np.array(meilleur_chemin)
    temps_execution=np.array(temps_execution)*10**1.75
    

plt.figure()

plt.plot(NBR_fourmis, meilleur_chemin,marker='+',color="r")

plt.plot(NBR_fourmis,temps_execution,marker='+',color="b")


plt.show()