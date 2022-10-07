#on importe la librairie tkinter pour avoir la fonction graphique
from cProfile import label
from cgi import test
from cmath import exp
from glob import glob
from http.client import SWITCHING_PROTOCOLS
from lib2to3.pgen2.token import LESS
from operator import sub
from sqlite3 import Row
from tkinter import *
import tkinter
from tkinter.tix import COLUMN
from turtle import Screen, bgcolor
import tkinter.ttk as ttk



#import la lib selenium
import tkinter
import selenium
#import la fonction find_element(By.ID/CLASS_NAME/X_PATH,"")
from selenium.webdriver.common.by import By
#import la fonction pour lancer le google automatisé
from selenium import webdriver
#import time afin d'ajouter des temps de repo
import time
#on importe la librairie qui permet d'avoir l'heure actuelle
from datetime import datetime
#import random pour mettre des temps de pause aléatoire
import random
#import les extensions
from selenium.webdriver.chrome.options import Options as ChromeOptions
#import tkinter
from tkinter import Tk
#import pillow, permet d'ajouter une image dans tkinter
from PIL import ImageTk, Image  


#on crée la fenetre
window = Tk()

window.title("SpotiBruh")
window.iconbitmap('img/spotify.ico')
window.minsize(480,360)
window.config(background='green')


def main ():
        
        #Faire une fonction qui met pause de facon aléatoire 


        def pause_play():
                playsong = driver.find_element(By.XPATH, "//button[@class='vnCew8qzJq3cVGlYFXRI']")
                playsong.click()  
        
        
        def ajout_compteur(i):
                if durée_actuelle == durée_totale :
                        i += 1 
                        print(f"Ecoute numéro : {i}")
                return i





        #on ajoute le vpn sur le bot
        chrome_options = ChromeOptions()
        chrome_options.add_extension('VPN.crx')

        # on définit notre driver sur chrome car on utilise ça
        driver = webdriver.Chrome(options=chrome_options)

        #on définit l'url afin de pouvoir la changer si on veut
        url_google = 'https://www.google.com/'
        url_spotify = 'https://accounts.spotify.com/fr/login?continue=https%3A%2F%2Fopen.spotify.com%2F'

        #lance chrome avec l'url
        driver.get(url_spotify)
        print('Lancement de chrome')

        time.sleep(10)



        #Connexion*************************

                # Insère le mail dans la case login    

        username_mail = mail

        username = driver.find_element(By.ID,"login-username")
        username.send_keys(username_mail)

                # Insère le mdp dans la case mdp  
                
        username_password = password

        username = driver.find_element(By.ID,"login-password")
        username.send_keys(username_password)

                # Clique sur le bouton connexion

        connexion = driver.find_element(By.XPATH,"//button[@data-testid='login-button']")
        connexion.click()

        print(f"Utilisateur : {mail}")
        print(f"Password : {password}")
        print(f"Pays : {country}")

        #***********************************


        # Met un timeur de 10 secondes avant que la prochaine fonction soit excécuté, ce qui permet d'attendre que la page charge
        
        print('Pause de 40 secondes pour attendre le chargement de la page')
        time.sleep(40)
        

        # Clique sur accepter les cookies

        if country == 'US' :
                acceptcookie = driver.find_element(By.XPATH, '//button[@class="onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon"]')
                acceptcookie.click()
        else :
                acceptcookie = driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
                acceptcookie.click()


        #***********************************
        #Lecture
        # Clique sur titre liké 

        likesong = driver.find_element(By.CLASS_NAME, 'r9YzlaAPnM2LGK97GSfa')
        likesong.click()
        print("Chargement de la page titre liké")

        time.sleep(15)

        lecture_boucle = driver.find_element(By.CLASS_NAME,'//button[@class="Vz6yjzttS0YlLcwrkoUR"]')
        lecture_boucle.click()

        #************************************
        #Calculer nb d'ecoute 

        durée_actuelle = driver.find_element(By.XPATH, "//div[@class='Type__TypeElement-goli3j-0 bjvopG playback-bar__progress-time-elapsed']")
        durée_actuelle_content = durée_actuelle.get_attribute('innerHTML')
        print (durée_actuelle_content.strip())

        durée_totale = driver.find_element(By.XPATH, "//div[@class='Type__TypeElement-goli3j-0 bjvopG npFSJSO1wsu3mEEGb5bh']")
        durée_totale_content = durée_totale.get_attribute('innerHTML')
        print (durée_totale_content.strip())

        ecoute_total = 0

        #************************************

        
        
        stop_musique = False 


        while stop_musique == False :
                
                # on définit l'heure actuelle 
                heure_actuelle = datetime.now().time().hour
                print(f"Il est {heure_actuelle}h.")
                
                print("Pause dans boucle while de 10 secondes")

                time.sleep(10)

                #En fonction du choix du pays, une plage horaire d'écoute est définie.

                if country == "US" : 


                        if heure_actuelle >= 1 and heure_actuelle <= 15 :

                                pause_play()
                                # on définit le temps d'écoute en seconde de façon aléatoire entre 2h (7200 secondes) et 3h (10800 secondes)
                                time_random = random.randint(7200, 10800)
                                print(f'Lecture de {time_random} secondes')
                                time.sleep(time_random)
                                
                                
                                pause_play()
                                # on définit le temps de pause en seconde de façon aléatoire entre 20min (1200 secondes) et 30min (1800 secondes)
                                time_random = random.randint(1200, 1800)
                                print(f'Pause de {time_random} secondes')
                                time.sleep(time_random)


                        else :
                                print('Trop tard')
                
                elif country == "Allemagne " or country == "Pays-Bas":
                        
                        if heure_actuelle >= 7 and heure_actuelle <= 21 :

                                pause_play()
                                # on définit le temps d'écoute en seconde de façon aléatoire entre 2h (7200 secondes) et 3h (10800 secondes)
                                time_random = random.randint(7200, 10800)
                                print(f'Lecture de {time_random} secondes')
                                time.sleep(time_random)
                                
                                
                                pause_play()
                                # on définit le temps de pause en seconde de façon aléatoire entre 20min (1200 secondes) et 30min (1800 secondes)
                                time_random = random.randint(1200, 1800)
                                print(f'Pause de {time_random} secondes')
                                time.sleep(time_random)


                        else :
                                print('Trop tard')

                elif country == "Roumanie" :
                        
                        if heure_actuelle >= 8 and heure_actuelle <= 22 :

                                pause_play()
                                # on définit le temps d'écoute en seconde de façon aléatoire entre 2h (7200 secondes) et 3h (10800 secondes)
                                time_random = random.randint(7200, 10800)
                                print(f'Lecture de {time_random} secondes')
                                time.sleep(time_random)
                                
                                
                                pause_play()
                                # on définit le temps de pause en seconde de façon aléatoire entre 20min (1200 secondes) et 30min (1800 secondes)
                                time_random = random.randint(1200, 1800)
                                print(f'Pause de {time_random} secondes')
                                time.sleep(time_random)


                        else :
                                print('Trop tard')
                



#**************************
#Cahier de Charges
# - Se connecte / ok
# - Lance une musique / ok
# - Coupe et remet la musique de façon aléatoire / ok 
# - Ajoute un VPN différent à chaque bot : https://www.youtube.com/watch?v=Fx1hbZMVS7k / ok 
# - Voir si on peut récupérer l'heure actuelle afin de couper la musique la nuit et qu'un autre le lance le jour. /ok
# - Définir les horaires en fonctions des différents pays des VPN /ok
#       - US : -6h de France /ok
#       - Roumanie : +1h de France /ok
#       - Allemagne : Même que France /ok
#       - Pays-Bas : Même que France /ok 
# - Mettre 2 Bot aux US qui écoutent pendant que les 2 autres sont en pause et inversement
# - Penser à une possibilité d'entrer différent mail/mdp /ok
# - Dans le logiciel mettre une liste déroulante et si on choisit un pays on aura l'ecoute de ce pays /ok
# - Reussir à récuperer le input de tkinter /ok
#**************************


def Newuser():

    global mail, password, country

    mail = saisie_mail.get()
    password = saisie_mdp.get()
    country = saisie_pays.get()

    main()


# logo en haut à gauche


label_title = tkinter.Label (text = "SPOTIBRUH", bg='green',font=('Proxima Nova',15))
label_title.pack()

#Zone de saisie du mail :

label_mail = tkinter.Label (text = "Saisissez votre mail :", bg='green',font=('Proxima Nova',15))
label_mail.pack()


saisie_mail = tkinter.Entry(font=('Proxima Nova',15))
saisie_mail.pack()

saisie_mail.focus_set()



#Zone de saisie du mdp :
label_mdp = tkinter.Label (text = "Saisissez votre mot de passe :", bg='green',font=('Proxima Nova',15))
label_mdp.pack()


saisie_mdp = tkinter.Entry(font=('Proxima Nova',15))
saisie_mdp.pack()


#Liste des pays
label_pays = tkinter.Label (text = "Saisissez le VPN de votre Pays :", bg='green',font=('Proxima Nova',15))
label_pays.pack()
saisie_pays = ttk.Combobox(window, values=["Allemagne", "US", "Pays-Bas", "Roumanie"],font=('Proxima Nova',15))
saisie_pays.pack()


# Créer un objet photoimage pour utiliser l'image
photo = PhotoImage(file = r"img/spo_button.png", height=40, width= 40) 
# Ajouter l'image dans le bouton 
Button(window,text= 'Se connecter', image=photo, compound=LEFT, command=Newuser).pack(side=TOP)



#Loop qui excécute la fenetre

window.mainloop()

#*************************
# - Adresse-mail du compte /ok
# - MDP du compte /ok
# - Liste des différents pays /ok
# - Bouton submit /ok 
# - Récupérer ces infos / ok
# - Bouton submit lance chrome /ok
#*************************




#*********************************
#Fonction compteur à tester 
# Activer la lecture en boucle !!!!!!!! suis trop con zebi   /ok
# mettre le compteur d'ecoute dans la boucle dans la boucle constante