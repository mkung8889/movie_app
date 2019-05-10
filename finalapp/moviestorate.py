import pandas as pd
import numpy as np
import json
import requests

import config as config
import popularmovies as popular

# ###### movies to rate
def moviestorate():
    url = "http://www.omdbapi.com/?t="
    movie_data = []
    for movie in popular.df:
        title = popular.df["movieId"][:-7]
        if ", " in title:
            split_title = title.split(", ")
            title = split_title[1] + " " + split_title[0]
        year = popular.df["year"]
        response = requests.get(url + title + config.api_key +"&y="+year)
        data = response.json()
        if "Error" not in data.keys() and data["Poster"] != "N/A":
            movie_data.append(data)
    return(movie_data)