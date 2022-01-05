from selenium import webdriver
from datetime import timedelta
import datetime
from bs4 import BeautifulSoup
import requests
import re

# driver_path = "./chromedriver"
# brave_path = "/usr/bin/brave-browser"

# option = webdriver.ChromeOptions()
# option.binary_location = brave_path

# browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

def open_flight(start, destination, debut, duration):
    #set-up des deffierent parametre d'ouverture du navigateur
    driver_path = "./chromedriver"
    brave_path = "/usr/bin/brave-browser"

    option = webdriver.ChromeOptions()
    option.binary_location = brave_path

    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
    


    #determination de la date de fin du voyage
    fin = debut + timedelta(days = duration)
    fin = fin.strftime("%Y-%m-%d")

    #generation de l'url du vol attendu
    url = "https://www.kayak.com/flights/"+ start + "-" + destination + "/" + debut_str+ "/" + fin + "?sort=bestflight_a&fs"

    browser.get(url)
    reponse = requests.get(url)

    #voir la methode avec le text !!!!!

    soup = BeautifulSoup(browser.page_source, 'lxml')

    # price_list = soup.find_all('div', attrs={'class' : 'Common-Booking-MultiBookProvider Theme-featured-large featured-provider cheapest multi-row'})
    price_list = soup.find_all('span', attrs={'class' : 'price-text'})

    price =[]
    for i in range(len(price_list)):
        value = price_list[i].getText()
        value = int(re.sub("[\n $,]", '', value))
        price.append(value)
    
    
    return print(price)

if __name__ == '__main__':

    #parametre selectionné pour le vol souhaité
    start = 'CDG'
    arrive = 'JFK'
    debut = datetime.datetime.now() + timedelta(days=3)
    debut_str = debut.strftime("%Y-%m-%d")

    print('Scraping for origin: {} and destination: {}, for date: {}'.format(start, arrive, debut_str))
    #appel de la fonction ouvrant la page a scraper
    open_flight(start, arrive, debut, 5)
