#on importe la librairie tkinter pour avoir la fonction graphique
from cProfile import label
from cmath import exp
from http.client import SWITCHING_PROTOCOLS
from operator import sub
from tkinter import *
import tkinter
from turtle import Screen, bgcolor
import tkinter.ttk as ttk
from functions import main
from functions import Utilisateur

#on crée la fenetre
window = Tk()

window.title("SpotiBruh")
window.iconbitmap('img/spotify.ico')
window.minsize(480,360)
window.config(background='green')


user = Utilisateur()


#Zone de saisie du mail :

label_mail = tkinter.Label (text = "Saisissez votre mail :", bg='green',font=('Proxima Nova',15))
label_mail.pack()


user.saisie_mail = tkinter.Entry(font=('Proxima Nova',15))
user.saisie_mail.pack()

user.saisie_mail.focus_set()



#Zone de saisie du mdp :
label_mdp = tkinter.Label (text = "Saisissez votre mot de passe :", bg='green',font=('Proxima Nova',15))
label_mdp.pack()


user.saisie_mdp = tkinter.Entry(font=('Proxima Nova',15))
user.saisie_mdp.pack()


#Liste des pays
label_pays = tkinter.Label (text = "Saisissez le VPN de votre Pays :", bg='green',font=('Proxima Nova',15))
label_pays.pack()
user.saisie_pays = ttk.Combobox(window, values=["Allemagne", "US", "Pays-Bas", "Roumanie"],font=('Proxima Nova',15))
user.saisie_pays.pack()

submit=Button(window, text="Envoyer",font=('Proxima Nova',20))
submit.pack()
submit.config(command=main)

#Loop qui excécute la fenetre

window.mainloop()

#*************************
# - Adresse-mail du compte /ok
# - MDP du compte /ok
# - Liste des différents pays /ok
# - Bouton submit /ok 
# - Récupérer ces infos
# - Bouton submit lance chrome
#*************************


