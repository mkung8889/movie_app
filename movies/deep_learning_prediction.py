import pandas as pd
import numpy as np
import json
import requests

# from config import api_key
import config
from CFModel import CFModel


#Reading users file:
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('../matrix_factorization/data/ml-100k/includes_team_users.csv').drop("Unnamed: 0",axis=1)

#Reading ratings file:
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('../matrix_factorization/data/ml-100k/includes_team_ratings.csv').drop("Unnamed: 0",axis=1)
ratings['user_emb_id'] = ratings['user_id'] - 1
ratings['movie_emb_id'] = ratings['movie_id'] - 1
# Set max_userid to the maximum user_id in the ratings
max_userid = ratings['user_id'].drop_duplicates().max()
# Set max_movieid to the maximum movie_id in the ratings
max_movieid = ratings['movie_id'].drop_duplicates().max()

#Reading items file:
i_cols = ['movie_id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('../matrix_factorization/data/ml-100k/u.item', sep='|', names=i_cols,
encoding='latin-1')

k_factors = 100
trained_model = CFModel(max_userid, max_movieid, k_factors)
trained_model.load_weights('../deep_learning/weights.h5')

def predict_rating(user_id, movie_id):
    return trained_model.rate(user_id - 1, movie_id - 1)

def top5rec(user_id):
    user_id = int(user_id)
    user_ratings = ratings[ratings['user_id'] == user_id][['user_id', 'movie_id', 'rating']]
    user_ratings['prediction'] = user_ratings.apply(lambda x: predict_rating(user_id, x['movie_id']), axis=1)
    user_ratings.sort_values(by='rating', 
                            ascending=False).merge(movies,
                                                    on='movie_id',
                                                    how='inner',
                                                    suffixes=['_u', '_m'])

    recommendations = ratings[ratings['movie_id'].isin(user_ratings['movie_id']) == False][['movie_id']].drop_duplicates()
    recommendations['prediction'] = recommendations.apply(lambda x: predict_rating(user_id, x['movie_id']), axis=1)
    recommendations = recommendations.sort_values(by='prediction',
                          ascending=False).merge(movies,
                                                 on='movie_id',
                                                 how='inner',
                                                 suffixes=['_u', '_m'])     

    top5 = recommendations[0:5]
    movie_list = []
    for i, row in top5.iterrows():
        movie_data = {
            'movie_id': row[0],
            'movie_title': row[1],
            'release_date': row[2],
            'IMDb_URL': row[5]
        }  
        movie_list.append(movie_data)
    url = "http://www.omdbapi.com/?t="
    movie_data = [] 
    for movie in movie_list:
        title = movie['movie_title'][:-7]
        if ", " in title:
            split_title = title.split(", ")
            title = split_title[1] + " " + split_title[0]
        year = movie["release_date"].split("-")[2]
        # response = requests.get(url + title + api_key +"&y="+year)
        response = requests.get(url + title + config.api_key +"&y="+year)
        # print(response.url)
        data = response.json()
        movie_data.append(data)
    return(movie_data)

    



