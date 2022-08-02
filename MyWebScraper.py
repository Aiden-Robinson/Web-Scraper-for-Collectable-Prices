from bs4 import BeautifulSoup #libraries that I need
import requests
import pandas as pd




url1= "https://www.trollandtoad.com/pokemon/sword-shield-brilliant-stars-singles/charizard-vstar-174-172-hyper-rare/1744388" #URLS of cards I want to chec
url2= "https://www.trollandtoad.com/pokemon/xy-flashfire-singles/charizard-ex-100-106-full-art-ultra-rare/1053665"
url3= "https://www.trollandtoad.com/pokemon/xy-flashfire-singles/m-charizard-ex-108-106-ultra-rare/1053672"
url4= "https://www.trollandtoad.com/pokemon/xy-evolutions-reverse-holo-singles/charizard-11-108-rare-reverse-holo/1105308"

prices={"Card": 0 , "Price" : 0} #dictionary with all card names and prices
urls= [url1, url2, url3, url4] #list of URLS
card_names=[] #list of card names
card_prices=[] #list of card prices

for url in urls: #iterates through each of the URLS
    page= requests.get(url).text #Sending an HTTP request to obtain the HTML code from the website
    doc= BeautifulSoup(page, "html.parser") #choosing a parsing tool to open the file with

    div= doc.find(class_= "d-flex flex-column").span #search the "d-flex flex-column" class and "span" tag
    price= float(str(div).split("$")[1].split("<")[0]) #isolating just the numerical value for the price
    price= "$"+ str(price)

    div2= doc.find(class_= "font-weight-bold font-large font-md-largest mt-1") #within the "font-weight.." class
    name= str(div2).split(">")[1].split("<")[0] #isolating for just the name of the card

    card_names.append(name) #adding the name of the card to the card list
    card_prices.append(price) #adding the price of the card to the price list

prices["Card"]= card_names #adding the list of cards to the dictionary
prices["Price"]= card_prices #adding the list of prices to the dictionary

songs_frame= pd.DataFrame(prices) #converting the dictionary to a dataframe

print(songs_frame.head()) #printing the dataframe

