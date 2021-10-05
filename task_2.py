from task_1 import scrape_movie
import pprint
import json

scrapped_data=scrape_movie()
def group_by_year(movies):

    years=[]
    for i in movies:
        if i["Year"] not in years:
            years.append(i["Year"])
    # for loop eliye hamne dict me lagya he kyuki hame jo year ke movils h wo list me chahiye in dict me to ek ke years ke movle ko leta rahega
    movies_dict={i:[] for i in years}
    for i in movies:
        year=i["Year"]
        for update_year in movies_dict:
            # print(update_year,year)
            if (update_year)==(year):
                movies_dict[update_year].append(i)

    with open("Yeras_way_data_2.json","w") as file1:
        json.dump(movies_dict,file1,indent=5)
    return movies_dict

group_by_year(scrapped_data)