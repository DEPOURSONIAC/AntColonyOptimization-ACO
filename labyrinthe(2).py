# -*- coding: utf-8 -*-
import pygame
import sys
import random
# 1. Configuration et Couleurs
pygame.init()
TAILLE_CASE =30
COULEUR_MUR = (44, 62, 80)      # Bleu nuit
COULEUR_VIDE = (236, 240, 241)  # Gris clair
COULEUR_JOUEUR = (231, 76, 60)   # Rouge
COULEUR_ARRIVEE = (46, 204, 113) # Vert
clock = pygame.time.Clock()
a=0



# 2. Le Labyrinthe (1 = Mur, 0 = Chemin, 2 = Arrivée)
# Tu peux modifier ce dessin à ta guise !
labyrinthe = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
[1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1],
[1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1],
[1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1],
[1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1],
[1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1],
[1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1],
[1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1],
[1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1],
[1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1],
[1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
[1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1],
[1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1],
[1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1],
[1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
[1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1],
[1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1],
[1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1],
[1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1],
[1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1],
[1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
[1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1],
[1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1],
[1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1],
[1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
[1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1],
[1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
[1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,2,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]


# Calcul de la taille de la fenêtre selon la matrice
LARGEUR = len(labyrinthe[0]) * TAILLE_CASE
HAUTEUR = len(labyrinthe) * TAILLE_CASE
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Mon Labyrinthe Pygame")

# Position initiale du joueur (ligne, colonne)
joueur_x, joueur_y = 1, 1
ancienne_pos_x,ancienne_pos_y =joueur_x, joueur_y
Directions =[[(0,1),(0,-1)],[(1,0),(-1,0)]]


# 3. Boucle principale
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
           
            
           
        if event.type == pygame.KEYDOWN:
            nouvelle_x, nouvelle_y = joueur_x, joueur_y
            if event.key == pygame.K_SPACE:
                d_possible=[]
                for directions_y in Directions[0] :
                    if labyrinthe[nouvelle_y + directions_y[1]][nouvelle_x] != 1 and nouvelle_y + directions_y[1] != ancienne_pos_y :
                        d_possible.append(directions_y)
                for directions_x in Directions[1] :
                    if labyrinthe[nouvelle_y][nouvelle_x + directions_x[0]] != 1 and nouvelle_x + directions_x[0] != ancienne_pos_x :
                        d_possible.append(directions_x)    
                if len(d_possible)>0:
                    dx, dy = random.choice(d_possible)
                    nouvelle_x += dx
                    nouvelle_y += dy
                    ancienne_pos_x,ancienne_pos_y = joueur_x,joueur_y
                else:
                    ancienne_pos_x,ancienne_pos_y = joueur_x,joueur_y 
            # Vérification des collisions (on ne marche pas sur les 1)
            if labyrinthe[nouvelle_y][nouvelle_x] != 1 :
                joueur_x, joueur_y = nouvelle_x, nouvelle_y

    # 4. Dessin du labyrinthe
    ecran.fill(COULEUR_VIDE)
    
    for ligne in range(len(labyrinthe) ):
        for col in range(len(labyrinthe[ligne])):
            rect = (col * TAILLE_CASE, ligne * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE)
            if labyrinthe[ligne][col] == 1:
                pygame.draw.rect(ecran, COULEUR_MUR, rect)
            elif labyrinthe[ligne][col] == 2:
                pygame.draw.rect(ecran, COULEUR_ARRIVEE, rect)

    # Dessin du joueur
    pygame.draw.circle(ecran, COULEUR_JOUEUR, 
                       (joueur_x * TAILLE_CASE + TAILLE_CASE//2, 
                        joueur_y * TAILLE_CASE + TAILLE_CASE//2), 
                       TAILLE_CASE//3)

    pygame.display.flip()
    clock.tick(60)
    # Victoire
    if labyrinthe[joueur_y][joueur_x] == 2:
        print("Gagné !")
        continuer = False

pygame.quit()
sys.exit()