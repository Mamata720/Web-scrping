import requests 
from bs4 import BeautifulSoup
import json

# if you want to scrape a website.class
# 1.use the api
# 2. HTML web scraping some tool like bs4.

def scrape_movie():
    url="https://www.imdb.com/india/top-rated-indian-movies/"
    api=requests.get(url)
    soup=BeautifulSoup(api.text,"html.parser")
    # Go to HTML code 
    main_div=soup.find("div",class_="lister")
    tbody=main_div.find("tbody",class_="lister-list")
    tr=tbody.find_all("tr")
    

    list=[]
    serial=0
    for i in tr:
        serial+=1
        movie_name=i.find("td",class_="titleColumn").a.get_text()
        movie=movie_name

        movie_year=i.find("td",class_="titleColumn").span.get_text()[1:5]
        years=int(movie_year)

        movie_rating=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        rating=float(movie_rating)

        movie_link=i.find("td",class_="titleColumn").a["href"]
        link="https://www.imdb.com/"+movie_year

        dict={"serial":serial,"Movie Name":movie,"Year":years,"Rating":rating,"url":link}
        list.append(dict) 
        with open("Movie_data_.json","w")as file:
            json.dump(list,file,indent=7)
    return list

scrape_movie()