#import la lib selenium
from curses.ascii import US
from lib2to3.pgen2 import driver
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

class Utilisateur() :

    def __init__(self):
        self.username = ''
        self.password = ''
        self.country = ''

user = Utilisateur()

def main ():
        #Faire une fonction qui met pause de facon aléatoire 

        def pause_play():
                playsong = driver.find_element(By.XPATH, "//button[@class='vnCew8qzJq3cVGlYFXRI']")
                playsong.click()  





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

        time.sleep(10)



        #Connexion*************************

                # Insère le mail dans la case login    

        #username_mail = "arnaudsacepee210@gmail.com"
        #username_mail = "dimitri.kakapolas@gmail.com"
        username_mail = user.username

        username = driver.find_element(By.ID,"login-username")
        username.send_keys(username_mail)

                # Insère le mdp dans la case mdp  

        #username_password = "Dimieva04+"
        #username_password = "Olympiakos07+"
        username_password = user.password

        username = driver.find_element(By.ID,"login-password")
        username.send_keys(username_password)

                # Clique sur le bouton connexion

        connexion = driver.find_element(By.XPATH,"//button[@data-testid='login-button']")
        connexion.click()

        #***********************************


        # Met un timeur de 10 secondes avant que la prochaine fonction soit excécuté, ce qui permet d'attendre que la page charge

        time.sleep(20)

        # Clique sur accepter les cookies

        acceptcookie = driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
        acceptcookie.click()

        #***********************************
        #Lecture
        # Clique sur titre liké 

        likesong = driver.find_element(By.CLASS_NAME, 'r9YzlaAPnM2LGK97GSfa')
        likesong.click()

        time.sleep(5)
        
        #clique sur le gros bouton play 

        playsong = driver.find_element(By.XPATH, "//button[@class='Button-qlcn5g-0 kgFBvD']")
        playsong.click()

        stop_musique = False 

        # on définit l'heure actuelle 
        heure_actuelle = datetime.now().time().hour


        #on définit le pays 
        saisie_pays = user.country

        # if saisie_pays == "US" :
        #         print('US')
        # elif saisie_pays == "Allemagne" :
        #         print('Allemagne')
        # elif saisie_pays == " Roumanie" :
        #         print('Roumanie')
        # elif saisie_pays == "Pays-Bas" :
        #         print("Pays-Bas")

        while stop_musique == False :

                if heure_actuelle >= 7 and heure_actuelle <= 21  :

                        # on définit le temps de pause en seconde de façon aléatoire entre 20min et 30min
                        time_random = random.randint(10, 20)
                        time.sleep(time_random)
                        pause_play()

                        #on définit le temps d'écoute en seconde de façon aléatoire entre 2h et 3h
                        time_random = random.randint(1, 3)
                        time.sleep(time_random)
                        pause_play()

                else :
                        print('Trop tard')
        




#**************************
#Derniere erreur :
#  File "c:\Users\Dimitri\Desktop\Dimitri\python\bot_spotify\functions.py", line 61, in main
#    username_mail = user.username
#AttributeError: 'Utilisateur' object has no attribute 'username'
#Cahier de Charges
# - Se connecte / ok
# - Lance une musique / ok
# - Coupe et remet la musique de façon aléatoire / ok 
# - Ajoute un VPN différent à chaque bot : https://www.youtube.com/watch?v=Fx1hbZMVS7k / ok 
# - Voir si on peut récupérer l'heure actuelle afin de couper la musique la nuit et qu'un autre le lance le jour. /ok
# - Définir les horaires en fonctions des différents pays des VPN 
#       - US : -6h de France
#       - Roumanie : +1h de France
#       - Allemagne : Même que France
#       - Pays-Bas : Même que France
# - Mettre 2 Bot aux US qui écoutent pendant que les 2 autres sont en pause et inversement
# - Penser à une possibilité d'entrer différent mail/mdp
# - Dans le logiciel mettre une liste déroulante et si on choisit un pays on aura l'ecoute de ce pays
#**************************