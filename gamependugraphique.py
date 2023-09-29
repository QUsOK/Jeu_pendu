# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 17:04:54 2023

@author: QUsOK
"""
mots =  [
    "python", "programme", "developpement", "informatique", "algorithme", "variable", "fonction", "boucle", "condition", "liste",
    "tableau", "chaine", "nombre", "calcul", "aléatoire", "logique", "classe", "objet", "module", "import", "fichier", "texte",
    "affichage", "console", "navigateur", "web", "site", "internet", "url", "lien", "image", "video", "audio", "fichier",
    "dossier", "répertoire", "système", "fichier", "mémoire", "disque", "réseau", "serveur", "client", "protocole", "adresse",
    "port", "connexion", "socket", "packet", "data", "information", "base", "donnée", "requête", "réponse", "formulaire",
    "champ", "bouton", "menu", "page", "lien", "navigateur", "url", "site", "internet", "balise", "html", "css",
    "javascript", "script", "code", "algorithme", "variable", "boucle", "condition", "fonction", "classe", "objet", "module",
    "import", "affichage", "console", "système", "mémoire", "fichier", "réseau", "serveur", "client", "protocole", "adresse",
    "port", "connexion", "socket", "packet", "data", "information", "base", "donnée", "requête", "réponse"
]
import tkinter as tk

import random
import unicodedata

def afficher_accents(lettre):
    accents = [c for c in unicodedata.normalize('NFD', lettre)]
    for accent in accents:
        return accent

def pendu(message, affichages, anciennes_tentatives, tentative):
    global ancienne_tentative 
    global point
    global affichage 
    anciennes_tentatives.append(tentative.upper())
    anciennes_tentatives.sort()
    ancienne_tentative = anciennes_tentatives
    new_affichage = ""
    nombre_tentative = 0

    if len(tentative) == 1:
        for i in range(len(message)):
            if len(affichages) != len(message):
                if message[i] == tentative or tentative == afficher_accents(message[i]):
                    new_affichage += message[i]
                    nombre_tentative += 1
                else:
                    new_affichage += "-"
            elif len(affichages) == len(message):
                if message[i] == tentative or tentative == afficher_accents(message[i]):
                    new_affichage += message[i]
                    nombre_tentative += 1
                else:
                    new_affichage += affichages[i]
        affichage = new_affichage
        if nombre_tentative == 0:
            point -= 1
            return (f"Il n'y a pas de {tentative.upper()}", new_affichage)
        else:
            return (f"{nombre_tentative } '{tentative.upper()}' {'trouvés' if nombre_tentative>1 else 'trouvé'}", new_affichage)
    else:
        if tentative == message:
            affichage = message
            return ("Bravo tu as gagné !", new_affichage)
        else:
            point -= 1
            return (f"Mauvaise tentative avec {tentative.upper()}", affichage)
ancienne_tentative = []
point = 10
affichage = ""
def pendu_graphique(message):
    def clavierENTREE(event):     
        cliquer()
    def cliquer():
        global message
        lettre = entree.get()
        if lettre.isalpha() and lettre.upper() not in ancienne_tentative:
            result = pendu(message.lower(), affichage, ancienne_tentative, lettre)
            label_affichage.config(text=result[1])
            label_resultat_affichage.config(text=result[0])
            r, g, b = int(point * 255/10), int(point * 255/10), int(point * 255/10)
            fenetre.configure(bg=f'#{r:02x}{g:02x}{b:02x}')
            label_point.config(text=f"{'Vies' if point>1 else 'Vies'} : {point}")
            entree.delete(0, 'end')

        if affichage == message:
            label_affichage.config(text=f"Gagné, le message était bien '{message}', il te restait {point} {'essais' if point>1 else 'essai'}")
            bouton.config(command=rejouer, text="Rejouer ?") 
            label_resultat.config(text="Tu as trouvé après avoir tester ceci :")

        elif point == 0:
            label_affichage.config(text=f"Perdu, le message était '{message}', tu feras mieux la prochaine fois")
            label_resultat.config(text="")
            label_ancien.config(text="")
            bouton.config(command=rejouer, text="Rejouer ?") 
        else:
            label_resultat.config(text="Veuillez entrer une lettre de l'alphabet ou une lettre différente de celle ci :")
            label_ancien.config(text=f"{ancienne_tentative}")    

    def rejouer():
        global ancienne_tentative 
        global point
        global affichage
        global message
        message = random.choice(mots)
        ancienne_tentative = []
        point = 10
        affichage = ""
        label_affichage.config(text="")
        label_ancien.config(text="")
        label_resultat_affichage.config(text="")

        label_point.config(text=f"{'Vies' if point>1 else 'Vies'} : {point}")
        label_resultat.config(text="Veuillez entrer une lettre de l'alphabet")
        bouton.config(command=cliquer, text="Essayer")
        
    fenetre = tk.Tk()
    fenetre.geometry("800x300")
    fenetre.title("Jeu du Pendu")

    label_titre = tk.Label(fenetre, text="Jeu du Pendu", font=("Helvetica", 16))
    label_titre.pack(pady=(10, 0))

    label_affichage = tk.Label(fenetre, text="", font=("Helvetica", 20))
    label_affichage.pack(pady=(0, 20))

    entree = tk.Entry(fenetre, font=("Helvetica", 16), width=5)
    entree.bind("<Return>", clavierENTREE)
    entree.pack(pady=(0, 20))

    bouton = tk.Button(fenetre, text="Essayer", font=("Helvetica", 12), command=cliquer)
    bouton.pack()

    label_resultat = tk.Label(fenetre, text="Veuillez entrer une lettre de l'alphabet", font=("Helvetica", 12))
    label_resultat.pack(pady=(10, 0)) 
    
    label_ancien = tk.Label(fenetre, text="", font=("Helvetica", 12))
    label_ancien.pack(pady=(10, 0)) 
    
    label_resultat_affichage = tk.Label(fenetre, text="", font=("Helvetica", 12))
    label_resultat_affichage.pack(pady=(10, 0))

    label_point = tk.Label(fenetre, text=f"Vies : {point}", font=("Helvetica", 12))
    label_point.pack()

    fenetre.mainloop()

message = random.choice(mots)
pendu_graphique(message)
