import pandas as pd
import numpy as np
import json
import requests

import config as config
import popularmovies as popular

# ###### movies to rate
def moviestorate():
    url = "http://www.omdbapi.com/?i="
    movie_data = []
    for index, row in popular.df.iterrows():
        imdb = row["imdbId"]
        response = requests.get(url + str(imdb) + config.api_key)
        data = response.json()
        if "Error" not in data.keys() and data["Poster"] != "N/A":
            movie_data.append(data)
    return(movie_data)