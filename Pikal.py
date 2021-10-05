from bs4 import BeautifulSoup
import requests
import pprint
import json


def pikal_scrap_data():
    url= url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    api=requests.get(url)
    soup=BeautifulSoup(api.text,"html.parser")
    div_1=soup.find("div",class_="_1gX7")

    div_2=div_1.span.get_text()
    split=div_2.split(" ")
    intiger_conv=int(split[1])
    page=intiger_conv//32+1
    list=[]
    k=1
    possition=0
    while k<=page:
        
        url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(k)
        api=requests.get(url)
        soup=BeautifulSoup(api.text,"html.parser")
        main_div=soup.find("div",class_="_3RA-")
        div=main_div.find_all("div",class_="UGUy")
        amount=main_div.find_all("div",class_="_1kMS")
        link=main_div.find_all("div",class_="_3WhJ")
        
        i=0
        
        while i<len(div):
            possition+=1
            pickal_name=(div[i].get_text())
            price=(amount[i].get_text())
            link_1=(link[i].a["href"])
        
            dict={"Position":possition,"Pikal name":pickal_name,"Price":price,"link":link_1}
            list.append(dict)
            i=i+1
        k=k+1
 
    with open("Pikal_scrap_data9.json","w") as file:
        json.dump(list,file,indent=5)
    return list
pikal_scrap_data()







