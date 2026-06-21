# -*- coding: utf-8 -*-
import csv
import random
import numpy as np
import time

NB_VILLES = 100
NB_FOURMIS = 10
NB_ITERATIONS = 50

ALPHA = 1.0      
BETA = 1.0       
EVAPORATION = 0.5 
Q = 100          

random.seed(100)

def ACO(NB_VILLES,NB_FOURMIS,NB_ITERATIONS):
    
    random.seed(100)
    
    debut = time.perf_counter()
    positions_villes = {i: () for i in range(NB_VILLES)}
    
    for i in range(NB_VILLES):
        while positions_villes[i]==():
    
            a = (random.randint(0,100),random.randint(0,100))
            t=False    
            for j in range(i):
                if positions_villes[j] == a:
                    t=True
            if not t:     
                positions_villes[i] = a  
    
    
    
    distances = np.zeros((NB_VILLES, NB_VILLES))
    for i in range(NB_VILLES):
        for j in range(NB_VILLES):
            if i != j:
                x1, y1 = positions_villes[i]
                x2, y2 = positions_villes[j]
                distances[i][j] = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            else:
                distances[i][j] = float('inf') 
    
    
    pheromones = np.ones((NB_VILLES, NB_VILLES))
    
    meilleur_chemin_global = None
    meilleure_distance_globale = float('inf')
    
    
    for iteration in range(NB_ITERATIONS):
        chemins_fourmis = []
        distances_fourmis = []
        
        
        for f in range(NB_FOURMIS):
            ville_depart = random.randint(0, NB_VILLES - 1)
            chemin = [ville_depart]
            villes_visitees = {ville_depart}
            
            while len(chemin) < NB_VILLES:
                ville_actuelle = chemin[-1]
                probabilites = []
                villes_accessibles = []
                
               
                for prochaine_ville in range(NB_VILLES):
                    if prochaine_ville not in villes_visitees:
                        
                        attrait_pheromone = pheromones[ville_actuelle][prochaine_ville] ** ALPHA
                        visibilite = (1.0 / distances[ville_actuelle][prochaine_ville]) ** BETA
                        score = attrait_pheromone * visibilite
                        
                        probabilites.append(score)
                        villes_accessibles.append(prochaine_ville)
                
                
                somme_scores = sum(probabilites)
                probabilites = [p / somme_scores for p in probabilites]
                choix_ville = random.choices(villes_accessibles, weights=probabilites, k=1)[0]
                
                chemin.append(choix_ville)
                villes_visitees.add(choix_ville)
                
            
            chemin.append(chemin[0])
            chemins_fourmis.append(chemin)
            
            
            dist_totale = 0
            for i in range(NB_VILLES):
                dist_totale += distances[chemin[i]][chemin[i+1]]
            distances_fourmis.append(dist_totale)
            
           
            if dist_totale < meilleure_distance_globale:
                meilleure_distance_globale = dist_totale
                meilleur_chemin_global = chemin
    
        
        pheromones *= (1 - EVAPORATION)
        
        
        for f in range(NB_FOURMIS):
            chemin = chemins_fourmis[f]
            dist = distances_fourmis[f]
            depot = Q / dist 
            
            for i in range(NB_VILLES):
                v_actuelle = chemin[i]
                v_suivante = chemin[i+1]
                pheromones[v_actuelle][v_suivante] += depot
                pheromones[v_suivante][v_actuelle] += depot 
                
    fin = time.perf_counter()

    return meilleur_chemin_global, meilleure_distance_globale , fin-debut

    
with open("meilleur-chemin-nbr-fourmis.csv","w",newline="", encoding="utf-8") as fichier:
        
    writer = csv.writer(fichier)
    writer.writerow(["nombre de fourmis","plus court chemin","temps"])
    for i in range(1,51):
        writer.writerow([i,ACO(100,i,50)[1],ACO(100, i, 50)[2]])


with open("meilleur-chemin-nbr-iteration.csv","w",newline="", encoding="utf-8") as fichier:
        
    writer = csv.writer(fichier)
    writer.writerow(["nombre d'iterations","plus court chemin","temps"])
    for i in range(1,51):
        writer.writerow([i,ACO(100,10,i)[1],ACO(100, 10, i)[2]])

"""print("=== RÉSULTAT FINAL ===")
print(f"Meilleur chemin trouvé : {meilleur_chemin_global}")
print(f"Distance minimale : {meilleure_distance_globale:.2f}")"""