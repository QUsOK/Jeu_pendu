# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 09:05:10 2023

@author: QUsOK
"""

import random
import unicodedata

phrases_faciles = [
    "La vie est belle",
    "Le soleil brille",
    "Python est génial",
    "Les chats sont mignons",
    "La pizza est délicieuse",
    "Les fleurs sont belles",
    "Le sport est amusant",
    "Les oiseaux chantent",
    "Les arbres sont grands",
    "La musique est relaxante",
    "Les vacances sont super",
    "Les amis sont importants",
    "Le chocolat est délicieux",
    "Les chiens sont fidèles",
    "La nature est magnifique",
    "Les sourires sont contagieux",
    "Les étoiles brillent la nuit",
    "Les livres sont enrichissants",
    "Les rires font du bien",
    "La pluie apaise l'âme",
    "Les gâteaux sont délicieux",
    "Les rêves se réalisent",
    "La mer est apaisante",
    "Les émotions sont belles",
    "La simplicité est élégante",
    "Le rire est la meilleure médecine",
    "Les éclats de rire sont précieux",
    "La vie est une aventure",
    "Les câlins font du bien",
    "Le café est revigorant",
    "La gratitude rend heureux"
]


phrases_difficiles = [
    "Phénomène astronomique",
    "Complexité algorithmique",
    "Ingénierie logicielle",
    "Théorie des graphes",
    "Intelligence artificielle",
    "Algorithmes de tri",
    "Mécanique quantique",
    "Équations différentielles",
    "Méthodes numériques",
    "Analyse de données",
    "Optimisation linéaire",
    "Modélisation mathématique",
    "Réseaux de neurones",
    "Cryptographie moderne",
    "Méthodes d'approximation",
    "Théorème de Fermat",
    "Physique des particules",
    "Théorie de l'information",
    "Statistiques avancées",
    "Calculabilité et complexité",
    "Géométrie différentielle",
    "Probabilités et statistiques",
    "Analyse numérique",
    "Théorie de la complexité",
    "Méthodes d'optimisation",
    "Systèmes dynamiques",
    "Théorème central limite",
    "Optimisation non linéaire",
    "Analyse fonctionnelle",
    "Algorithmes génétiques"
]

phrases_tres_difficiles = [
    "Quasar lointain",
    "Physique quantique",
    "Phénomènes thermodynamiques",
    "Mécanique relativiste",
    "Équations intégrales",
    "Systèmes d'équations différentielles",
    "Méthodes itératives",
    "Analyse de Fourier",
    "Calcul tensoriel",
    "Théorie de la complexité computationnelle",
    "Géométrie symplectique",
    "Cryptanalyse avancée",
    "Théorie de l'information quantique",
    "Statistiques bayésiennes",
    "Théorème de Gödel",
    "Physique des particules élémentaires",
    "Théorie des cordes",
    "Théorie de la relativité générale",
    "Systèmes dynamiques chaotiques",
    "Transformée de Laplace",
    "Probabilités conditionnelles",
    "Théorie de la mesure",
    "Calcul des variations",
    "Méthodes de Monte Carlo",
    "Réseaux de Pétri",
    "Théorème de Banach-Tarski",
    "Optimisation convexe",
    "Analyse fonctionnelle non linéaire",
    "Algorithmes d'approximation",
    "Théorie de la décidabilité"
]

phrases = phrases_faciles + phrases_difficiles + phrases_tres_difficiles

# Vérifie si le mot contient la lettre donnée avec un acccent (e : réponse)
def afficher_accents(lettre):
    accents = [c for c in unicodedata.normalize('NFD', lettre)]
    for accent in accents:
        return accent


def pendu(message, point, affichage, mode, ancienne_tentative):
    tentative = input(f"Essai lettre : {ancienne_tentative} \n")
    for ancienne in ancienne_tentative:
        # S'il y a des espaces dans sa réponse, sa ne lui demande pas de refaire sa demande
        if not " " in tentative:
            while not tentative.isalpha() or tentative.isalpha() and tentative.upper() in ancienne_tentative:
                tentative = input(f"Il faut une lettre de l'alphabet': (autre que celle ci ({ancienne_tentative}))\n")
    new_affichage = ""
    nombre_tentative = 0
    if len(tentative) == 1:
        for i in range(len(message)):
            #première boucle pour faire apparaitre le message codé
            if len(affichage) != len(message):
                
                # Vérifie si la lettre correspond à une lettre du mot ou à une version avec accent
                if message[i] == tentative or tentative == afficher_accents(message[i]):
                    new_affichage += message[i]
                    nombre_tentative += 1
                else:
                    # Affiche les points et les espaces des phrases
                    if not message[i].isalpha():
                        new_affichage += message[i]
                    else:
                        # "_" au lieu de "-" à cause des de certains phrases avec tiret
                        new_affichage += "_"
            elif len(affichage) == len(message):
                
                # Vérifie si la lettre correspond à une lettre du mot ou à une version avec accent
                if message[i] == tentative or tentative == afficher_accents(message[i]):
                    new_affichage += message[i]
                    nombre_tentative += 1
                else:
                    new_affichage += affichage[i]
        # S'il n'y a pas de correspondance avec une lettre du mot 
        if nombre_tentative == 0 and len(affichage) == len(message):
            print(f"Il n'y a pas de {tentative.upper()}")
            point -= 1
        else:
            print(f"{nombre_tentative } '{tentative.upper()}' {'trouvés' if nombre_tentative>1 else 'trouvé'}")
        # Ajoute la lettre tenté et trie le tableau
        ancienne_tentative.append(tentative.upper())
        ancienne_tentative.sort()
    else:
        if tentative != message and len(tentative) == len(message) or tentative != message and " " in tentative:
            # S'il n'y a pas de correspondance avec une lettre du mot 
            # ou s'il y a un espace mais que ce n'est pas égale à la réponse
            point -= 1
            new_affichage = affichage
            ancienne_tentative.append(tentative.upper())
            ancienne_tentative.sort()
            for i in range(len(message)):
                # Vérifie les lettre et les accents et les affichent
                if message[i] == tentative or tentative == afficher_accents(message[i]):
                    new_affichage += message[i]
                else:
                    # Garde les anciennes données (soit _, soit les lettres trouvés précédamment)
                    new_affichage += affichage[i]
        elif  tentative != message:
            # Il a écrit des lettres mais sans mettre d'espace donc c'est une erreur
            print("Essayez un lettre ou une réponse mais pas des lettres au hasard (cette erreur n'a pas été prise en compte")
            new_affichage = affichage
        else:
            # Affiche la réponse car elle a été trouvé
            new_affichage = message

    affichage = new_affichage  
    # Affiche le message caché et le nombre d'essais restant
    print(affichage, "/", point, f"{'essais' if point>1 else 'essai'}\n")
    # Mode 1 seule tentative
    if mode == 2:
        if affichage == message:
            print(f"Gagné, le message était bien '{message}', il te restait {point} {'essais' if point>1 else 'essai'}")
        elif point == 0:
            print(f"Perdu, le message était '{message}', tu feras mieux la prochaine fois")
        else:
            pendu(message, point, affichage, mode, ancienne_tentative)
    else:
        # Mode jusqu'à la fin des tentative
        if affichage == message:
            print(f"Gagné, le message était bien '{message}', tu as gagné 1 essai en plus pour le prochain mot ({point+1} {'essais' if point>1 else 'essai'} restant)")
            message = random.choice(phrases).lower()
            pendu(message, point+1, "", mode, [])
        elif point == 0:
            print(f"Perdu, le message était '{message}', ce fut une belle game")
        else:
            pendu(message, point, affichage, mode, ancienne_tentative)
    
point = 0
mode = ""
while point == 0:
    mode = input("Quel mode voulez-vous ? (1 ou 2)\n 1 - Mort subite\n 2 - Classique\n")
    if mode == "1":
        point = 20
        message = random.choice(phrases)
    elif mode == "2":
        niveau = input("\nQuel niveau voulez-vous ?(1 ou 2 ou 3)\n 1 - Facile\n 2 - Moyen\n 3 - Difficile\n")
        if niveau == "1":
            message = random.choice(phrases_faciles)
            point = 10
        elif niveau == "2":
            message = random.choice(phrases_difficiles)
            point = 7
        elif niveau == "3":
            message = random.choice(phrases_tres_difficiles)
            point = 5
        else:
            print("Vous devez choisir soit 1, soit 2, soit 3\n")
    else:
        print("Vous devez choisir 1 ou 2\n")
    
pendu(message.lower(), point, "", int(mode), [])

""