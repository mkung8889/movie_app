import pandas as pd
import numpy as np
import json
import requests

# from config import api_key
import config
from keras.models import load_model


# #Reading users file:


# #Reading ratings file:
# r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
# ratings = pd.read_csv('../matrix_factorization/data/ml-100k/includes_team_ratings.csv').drop("Unnamed: 0",axis=1)
# ratings['user_emb_id'] = ratings['user_id'] - 1
# ratings['movie_emb_id'] = ratings['movie_id'] - 1
# # Set max_userid to the maximum user_id in the ratings
# max_userid = ratings['user_id'].drop_duplicates().max()
# # Set max_movieid to the maximum movie_id in the ratings
# max_movieid = ratings['movie_id'].drop_duplicates().max()

# #Reading items file:
# i_cols = ['movie_id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
# 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
# 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
# items = pd.read_csv('../matrix_factorization/data/ml-100k/u.item', sep='|', names=i_cols,
# encoding='latin-1')

# k_factors = 100
trained_model = load_model('../deep_learning2.0/movie_recommender_100k_trained.h5')
def predict_rating(userId, movieId):
    return trained_model.predict([np.array([userId - 1]), np.array([movieId - 1])])[0][0]

def top5rec(userId):
    user_ratings = ratings[ratings['userId'] == userId][['userId', 'movieId', 'rating']]
    user_ratings['prediction'] = user_ratings.apply(lambda x: predict_rating(userId, x['movieId']), axis=1)
    user_ratings.sort_values(by='rating', 
                         ascending=False).merge(movies,
                                                on='movieId',
                                                how='inner',
                                                suffixes=['_u', '_m'])

    recommendations = ratings[ratings['movieId'].isin(user_ratings['movieId']) == False][['movieId']].drop_duplicates()
    recommendations['prediction'] = recommendations.apply(lambda x: predict_rating(userId, x['movieId']), axis=1)
    recommendations = recommendations.sort_values(by='prediction',
                                             ascending=False).merge(movies,
                                                                   on='movieId',
                                                                   how='inner',
                                                                   suffixes=['_u','_m'])
    top5 = recommendations[0:5]
    movie_list = []
    for i, row in top5.iterrows():
        movie_data = {
            'movie_id': row[0],
            'movie_title': row[2]
        }
        movie_list.append(movie_data)
    url = "http://www.omdbapi.com/?t="
    for movie in movie_list:
        title = movie['movie_title'][:-7]
        if ', The' in title:
            split_title = title.split(', ')
            title = split_title[1] + ' ' + split_title[0]
        year = movie['movie_title'][-6:]
        year = year.replace('(', '').replace(')', '')
        response = requests.get(url + title + config.api_key + "&y=" + year)
        data = response.json()
        if "Error" not in data.keys() and data["Poster"] != "N/A":
            movie_data.append(data)
    return movie_data[0:5]

    