from selenium import webdriver
from datetime import timedelta
import pandas as pd
import datetime
from bs4 import BeautifulSoup
import requests
import re
from mongo_pipe import data_pipe
import schedule
import time
from apscheduler.schedulers.blocking import BlockingScheduler

# def open_flight(start, destination, debut, duration):
def open_flight():
    #set-up des deffierent parametre d'ouverture du navigateur
    driver_path = "/home/eadnoth/flight_price/chromedriver"
    # brave_path = "/usr/bin/brave-browser"

    option = webdriver.ChromeOptions()
    # option.binary_location = brave_path
    # option.add_argument('--headless')
    # option.add_argument("--no-sandbox")
    # option.add_argument("window-size=1400,2100") 
    # option.add_argument('--disable-gpu')
    # option.add_argument('--disable-dev-shm-usage')  

    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
    
    #determination de la date de fin du voyage
    # fin = debut + timedelta(days = duration)
    # fin = fin.strftime("%Y-%m-%d")

    #generation de l'url du vol attendu
    # url = "https://www.kayak.com/flights/"+ start + "-" + destination + "/" + debut_str+ "/" + fin + "?sort=bestflight_a&fs"
    url = "https://www.kayak.com/flights/CDG-JFK/2022-01-16/2022-01-21?sort=bestflight_a&fs"

    browser.get(url)
    reponse = requests.get(url)

    #variable nous permettant d'avoir acce au code de la page 
    soup = BeautifulSoup(browser.page_source, 'lxml')

    # price_list = soup.find_all('div', attrs={'class' : 'Common-Booking-MultiBookProvider Theme-featured-large featured-provider cheapest multi-row'})
    #grace a la variable 'soup' nous cherchons les prix grace au balise et au ''class'
    # price_list = soup.find_all('span', attrs={'class' : 'price-text'})
    # price_list = soup.find_all('span', class_ = 'price-text')

    ################################################################
    #recupreration des prix de vol
    price_list = soup.find_all('div', class_ = 'col-price result-column js-no-dtog')

    #nettoyage de la variable 'price_list' pour recuperer le prix du billet et le caster en 'int' dans la list price
    price =[]
    for i in range(len(price_list)):
        value = price_list[i].getText().split()[2]
        value = int(re.sub("[\n $,]", '', value))#int()
        price.append(value)
    # price = price[:16] 

    ################################################################
    #recupreration des noms de compagnies
    compagny_list = soup.find_all('div', class_ = 'bottom', attrs = {'dir' : 'ltr'})
    compagnie = []
    
    for i in range(len(compagny_list)):
        value = compagny_list[i].getText().replace("\n", "")
        compagnie.append(value)

    compagnie_alle = compagnie[::2]
    compagnie_retour = compagnie[1::2]

    ################################################################
    #recupreration du nombre d'arret
    stop_list = soup.find_all('span', class_ = 'stops-text')
    stop = []
    
    for i in range(len(stop_list)):
        value = stop_list[i].getText()
        value = re.sub("[\n ]", '', value)
        stop.append(value)

    stop_alle = stop[::2]
    stop_retour = stop[1::2]

    ################################################################
    #recupreration de l'heure de depart du val
    heure_list = soup.find_all('span', class_ = 'time-pair')
    heure = []

    for i in range(len(heure_list)):
        value = heure_list[i].getText().replace("\n","")
        heure.append(value)

    heure = heure[::2]
    heure_alle = heure[::2]
    heure_retour = heure[1::2]

    ################################################################
    #recupreration du temps de vol
    temps_list = soup.find_all('div', class_ = 'top')
    temps = []

    for i in range(len(temps_list)):
        value = temps_list[i].getText().replace('\n','')
        temps.append(value)

    temps = temps[3::4]
    temps_alle = temps[::2]
    temps_retour = temps[1::2] 
    
    list_test = [compagnie_alle, compagnie_retour, stop_alle, stop_retour, heure_alle, heure_retour, temps_alle, temps_retour, price]

    for i in list_test:
        print(len(i))

    ################################################################
    #gerneration d'une dataframe contenant toute les informations
    df = pd.DataFrame({"Compagnie alle" : compagnie_alle,
                       "Compagnie retour" : compagnie_retour,
                       "Nb stop alle" : stop_alle,
                       "Nb stop retour" : stop_retour,
                       "Heure depart alle" : heure_alle,
                       "Heure depart retour" : heure_retour,
                       "Temps trajet alle" : temps_alle,
                       "Temps trajet retour" : temps_retour,
                       "price" : price
                      })

    df['date recup data'] = datetime.datetime.now()
    # df['id_flight'] = start+"_"+destination+"_"+debut_str+"_"+fin

    #fermeture du navigateur 
    #browser.close()
    # data_pipe(df)
    #la fonction retourne un dataframe de tout les vols contenu dans la page qui nous interesse 
    return df 

if __name__ == '__main__':

    #parametre selectionné pour le vol souhaité
    start = 'CDG'
    arrive = 'JFK'
    debut = datetime.datetime.now() + timedelta(days=3)
    debut_str = debut.strftime("%Y-%m-%d")

    print('Scraping for origin: {} and destination: {}, for date: {}'.format(start, arrive, debut_str))
    #appel de la fonction ouvrant la page a scraper
    # df = open_flight(start, arrive, debut, 5)
    # open_flight(start, arrive, debut, 5)
    df = open_flight()
    print(df)
    print(df.dtypes)
    
    # scheduler = BlockingScheduler()
    # scheduler.add_job(open_flight, 'interval', minutes=1)
    # scheduler.start()

