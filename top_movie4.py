import requests
from bs4 import BeautifulSoup
import json
def smovie_detalies():

    url="https://www.rottentomatoes.com/m/black_panther_2018"
    api=requests.get(url)
    soup=BeautifulSoup(api.text,"html.parser")
    main_Div=soup.find("ul",class_="content-meta info")
    li=main_Div.find_all("li",class_="meta-row clearfix")
    dict_1={}
    list_1=[]

    for i in li:
        reating=i.find("div",class_="meta-value").get_text().strip().replace("\n",' ')
        gener=i.find('div',class_='meta-label subtle').get_text()
        dict_1.update({gener:reating})
    list_1.append(dict_1)
    with open("movies_dealites.json","w")as file:
        json.dump(list_1,file,indent=5)
    return dict_1
smovie_detalies()





    
        
    

