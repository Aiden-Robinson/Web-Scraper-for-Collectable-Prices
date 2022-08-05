# Web-Scraper-for-Collectable-Prices
The goal of project was to save me the time of indiviudally checking the prices of various colletable prices. I am able to run the code and it displays the prices of items I am keeping an eye on simply by inputting their website URLs into my program. In this demonstration, I am tracking the prices of valuable Charizard Pokemon cards I own.

`Skills:` Beautiful Soup 4, Pandas, Python

![Webscraping](https://user-images.githubusercontent.com/106715980/182493441-1cf482c9-b0ae-4b4c-9117-3abb3a1124bc.png)

## Working with HTML code
I used Beautiful Soup 4, a python library for HTML parsing which sent an HTTP request to obtain the HTML code from all the websites. I learned some basic HTML tree structuring and used built-in functions to navigate thorugh classes and tags in order to isolate the information I needed.

![HTML example](https://user-images.githubusercontent.com/106715980/182493862-4238c070-fca2-46f4-b17f-0dab00147444.png)

## Data Processing

I used several python functions like `.split()` and `.strip()` in order to fully isolate the information I needed. I iterated thorugh each URL and appended the name of the card and price to their respective lists. Both lists were then sorted in descending order of price. 

`card_prices, card_names= zip(*sorted(zip(card_prices,card_names)` sorts both lists by price

These lists were appended to a dictionary which was then converted to a data frame in `Pandas`. I decided to use Pandas becasue it has a clean output with the way it orgainizes tables.
