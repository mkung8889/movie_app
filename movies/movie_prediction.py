import pandas as pd
import numpy as np
import json
import requests

# from config import api_key
import config


#Reading users file:
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('../matrix_factorization/data/ml-100k/includes_team_users.csv').drop("Unnamed: 0",axis=1)

#Reading ratings file:
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('../matrix_factorization/data/ml-100k/includes_team_ratings.csv').drop("Unnamed: 0",axis=1)

#Reading items file:
i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('../matrix_factorization/data/ml-100k/u.item', sep='|', names=i_cols,
encoding='latin-1')

#prediction matrix
prediction_matrix = np.loadtxt("../matrix_factorization/team_prediction_matrix.txt")

# ###### rating prediction and RMSE
# predicted_df = pd.read_csv("../matrix_factorization/predicted_ratings.csv")
# predicted_df = predicted_df.drop("Unnamed: 0", axis=1)
# predicted_df["rating_diff"] = predicted_df["predicted_rating"] - predicted_df["rating"]
# rating_predictions = users[["user_id","age","sex"]]
# rating_predictions = rating_predictions.merge(ratings.groupby("user_id")["rating"].count(),on="user_id").rename(columns={"rating":"#_ratings"})
# rating_predictions["RMSE"] = ""
# for i in range(len(users)):
#     user_id = rating_predictions["user_id"][i]
#     user_df = predicted_df.loc[predicted_df["user_id"]==user_id].reset_index(drop=True)
#     sse = 0 
#     for j in user_df["rating_diff"]:
#         sse += np.power(j,2)
#     mse = sse/len(user_df)
#     rating_predictions["RMSE"][i] = np.sqrt(mse)

###### movie recommendations
def top5rec(user_id):
    user_id = int(user_id)
    rated_movies = list(ratings.loc[ratings["user_id"] ==user_id,"movie_id"].values)
    orderedRecs = list(np.argsort(-prediction_matrix[user_id - 1,]))
    for movie in rated_movies:
        if movie-1 in orderedRecs:
            orderedRecs.remove(movie)
    top5 = orderedRecs[0:5]
    rec_df = pd.DataFrame()
    for movie in top5:
        rec_df = rec_df.append(items.loc[items["movie id"]==int(movie)+1])
    movie_list = []
    for i,row in enumerate(rec_df.values):
        movie_data = {
            "movie_id": row[0],
            "movie_title": row[1],
            "release_date": row[2],
            "IMDb_URL": row[4]
        }
        movie_list.append(movie_data)
    url = "http://www.omdbapi.com/?t="
    movie_data = []
    for movie in movie_list:
        title = movie["movie_title"][:-7]
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

######user data
def user_data(user_id):
    user_data = users.set_index("user_id")
    ratings_count = ratings.groupby("user_id").count()["movie_id"]
    user_data["#_movies_rated"] = ratings_count
    user = {
        "user_id": user_id,
        "age": str(user_data.iloc[int(user_id)-1].values[0]),
        "sex": str(user_data.iloc[int(user_id)-1].values[1]),
        "occupation": str(user_data.iloc[int(user_id)-1].values[2]),
        "zipcode": str(user_data.iloc[int(user_id)-1].values[3]),
        "num_movies_rated": str(user_data.iloc[int(user_id)-1].values[4])
    }
    return(user)