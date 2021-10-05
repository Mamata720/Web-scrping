from bs4 import BeautifulSoup
from task_1 import scrape_movie
from task_2 import group_by_year
import pprint
import json

scrapped=scrape_movie()
decade_arenge=group_by_year(scrapped)
def group_by_decade(movies):
    list=[]
    dict={}
    for i in movies:           
       module=i%10             
       decade_substract=i-module
       if decade_substract not in list:
           list.append(decade_substract)
    list.sort()
    for i in list:
        dict[i]=[]
    for i in dict:
        decade_10=i+9 
        for x in movies:
            if x<=decade_10 and x>=i: 
                for v in movies[x]: 
                    dict[i].append(v)
    
                
        with open("group_by_decade.json","w") as num:
            json.dump(dict,num,indent=6)

    return dict
group_by_decade(decade_arenge)


    
