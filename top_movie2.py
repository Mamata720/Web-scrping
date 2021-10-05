from top_movie1 import sracp_movie
import pprint
import json
scraped_movies=sracp_movie()
def group_by_year(movie):
    years=[]
    for i in movie:
        if i["Year"] not in years:
            years.append(i["Year"])
            movie_dic={i:[] for i in years}
            for i in movie:
                year=i["Year"]
                for (uppdate_year)in movie_dic:
                    if (uppdate_year)==year:
                        movie_dic[uppdate_year].append(i)
    with open("year_name.json","w")as file:
        json.dump(movie_dic,file,indent=5)
    return movie_dic
group_by_year(scraped_movies)








