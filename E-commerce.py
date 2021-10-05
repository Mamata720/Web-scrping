from bs4 import BeautifulSoup
import requests
import json
import pprint

def Ecommerce_site_data():
    url="https://webscraper.io/test-sites"
    api=requests.get(url)
    soup=BeautifulSoup(api.text,"html.parser")
    main_div=soup.find("div",class_="container test-sites")
    div=main_div.find_all("div",class_="col-md-7 pull-right")
    
    list=[]
    position=0
    for i in div:
        position+=1
        title=i.find("h2",class_="site-heading").a.get_text().strip()
        num=title

        url=i.find("h2",class_="site-heading").a["href"]
        link="https://webscraper.io/"+url
        
        dict={"Position":position, "Site Name":num, "url":link}
        list.append(dict)

        with open("E-Comarce_data.json","w") as k:
            json.dump(list,k,indent=5)
        
    return list
Ecommerce_site_data()