# coding: utf-8


"""
Module ACO (Ant Colony Optimization)

Ce module contient l'algo de colonie de fourmis.
Il gère le meilleur chemin entre les villes:
    - il gère les probas via les phéromones
    - la dist entre les villes
    - l'évaporation  et le dépot des phéromones

"""
import random
import numpy as np
import tools
import time

# Décla des constantes (en MAJUSCULES)

ALPHA       : float = 1.0
BETA        : float = 1.0
EVAPORATION : float = 0.5
Q           : float = 100 # Ratio du nombre de phéromone sur une route/ chemin


# fonctions
def ACO(nombreVilles: int = 100, nombreFourmis: int = 100, nombreIterations: int = 50):
    """
    ACO (Ant Colony Optimization)

    Paramètres :
        - nombreVilles      (int)    : nombre total de villes du problème
        - nombreFourmis     (int)    : nombre de fourmis utilisées à chaque itération
        - nombreIterations  (int)    : nombre de cycles d’exécution de l’algorithme

    Explication :
        - implémente l’algo du ACO
        - chaque fourmi construit un chemin complet entre les villes
        - les choix sont crées par les phéromones et les distances
        - les bonnes solutions renforcent les chemins via le dépôt de phéromones
        - les mauvaises solutions disparaissent via l'évaporation

    Retour :
        - tuple :
            - le meilleur chemin trouvé
            - la distance minimale associée
            - le temps mis pour le trouver (deltaT)
    """

    # Décla des variables
    debut = time.perf_counter()

    meilleurChemin   = None
    meilleurDistance = np.inf

    villes   = tools.creationDesVilles(nombreVilles)
    distances = tools.matriceDistanceEuclidienne(villes, nombreVilles)

    # Matrice des phéromones : toutes les valeurs sont mises à 1. Elle sert à aider les fourmis dans le choix des chemins
    MatricePheromones : np.ndarray = np.ones((nombreVilles, nombreVilles))

    # Algo du ACO
    for iteration in range(nombreIterations):

        # Liste des chemins trouvés par les fourmis
        cheminTrouverParFourmis : list = list()
        # Liste des distances associées
        listeDistance           : list = list()

        for fourmis in  range(nombreFourmis):
            villeDepart = random.randint(0, nombreVilles-1)

            cheminFourmi: list = [villeDepart]
            villesVisitees: set = {villeDepart}

            while (len(cheminFourmi) < nombreVilles):

                villeActuelle = cheminFourmi[-1]

                proba = []
                villesAccessibles = []

                for prochaineVille in range(nombreVilles):

                    if (prochaineVille not in villesVisitees):
                        pheromone = MatricePheromones[villeActuelle][prochaineVille] ** ALPHA
                        visibilite = (1.0 / distances[villeActuelle][prochaineVille]) ** BETA

                        score = pheromone * visibilite

                        proba.append(score)
                        villesAccessibles.append(prochaineVille)
                    pass

            pass

        

        print(' TEST ITERATION')
   
    # Mesurer le temps que ça prends
    fin = time.perf_counter()
    deltaT = fin - debut

    return (meilleurChemin, meilleurDistance, deltaT )


if ( __name__ == "__main__"):
    print('HelloWorld')