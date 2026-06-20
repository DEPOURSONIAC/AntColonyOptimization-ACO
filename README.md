# AntColonyOptimization (ACO)

## Projet et présentation de celui-ci.
Le projet **Ant Colony Optimization (ACO)** est une simulation  du comportement des fourmis.

Le but est de résoudre des problèmes d’optimisation (comme trouver le chemin le plus court entre plusieurs villes ou le meilleur chemin pour envoyer des paquets IP avec RIP/ OSPF (Réseaux)) en imitant la nature :
les fourmis déposent des **phéromones virtuelles** pour guider les autres.

---

## Idée générale


Voici le fonctionnement :
- Chaque fourmi explore un réseau de points (villes)
- Elle choisit ses chemins en fonction :
  - des phéromones (expérience passée d'une autre fourmis)
  - de la distance
- Les bons chemins sont renforcés
- Les mauvais chemins disparaissent avec le temps

Le système converge vers une bonne solution.

---

## Fonctionnement
a. Création du graphe (villes + distances)
b. Initialisation des fourmis
c. Chaque fourmi construit un chemin
d. Calcul de la qualité du chemin
e. Mise à jour des phéromones
f. Répétition sur plusieurs itérations
g. Récupération du meilleur chemin

---

## Paramètre mathématique
- **α (alpha)** -> importance des phéromones (mémoire du système)
- **β (beta)** -> importance de la distance
- **évaporation** -> disparition des phéromones avec le temps
- **nombre de fourmis** -> intensité de l’exploration
- **nombre d’itérations** -> durée de convergence/ temps absolu

---

## Organisation du projet ACO
### main.py (programme P)
- Lance toute la simulation
- Contient la boucle principale
- Affiche les résultats (meilleur chemin)

Le fichier le + important

---

### moduleAco.py (logique ACO)
- Calcul des probabilités de choix
- Mise à jour des phéromones
- Construction des chemins

C’est le cerveau de l’algorithme.

---

### tools.py (outils)
- Calcul des distances entre villes
- Gestion des matrices
- Fonctions utilitaires

Sert à simplifier le code principal.

---

### README.md
- Présentation du projet
- Explication rapide du fonctionnement
- Instructions pour lancer le programme

Le but est d'expliquer le projet et comment il est structurer

---

## Utilisation de certaines technologies
- **Python** -> langage principal
- **NumPy** -> calculs rapides sur matrices
- **Matplotlib** -> visualisation des chemins
- **CSV** -> stockage des données de villes
- (optionnel) interface graphique avec Tkinter( avoir si j'ai le temps)

---

## Obj
- Simuler un système intelligent inspiré de la nature
- Comprendre un algorithme d’optimisation moderne
- Résoudre un problème complexe (type TSP)
- Observer comment une solution émerge sans calcul direct

---

## Cas concret
- Optimisation de trajets (GPS, livraison)
- Réseaux télécom (routage)
  > Je me permets de mettre routage car je suis en R&T XD
- Logistique
- Intelligence artificielle (optimisation entre LLM)

---

## GROSSO MODO
Des fourmis explorent un problème/ chemin.

Ils laissent des traces.
Les bonnes solutions sont renforcées.
Le système finit par trouver un bon chemin sans être programmé explicitement pour ça.


Projet propre, structuré, modulaire.
> Scalable/ scalabilité / evolutivité (important dans le monde pro)
Objectif : compréhension totale de l’algorithme + code clair + résultats visibles.

Travail sérieux, pas approximatif.
