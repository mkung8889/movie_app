from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func

from flask_jsglue import JSGlue

from random import *

import pandas as pd
import moviestorate as mtr
import deep_learning_prediction as dlp

# u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code', '#_ratings', 'RMSE']
# users = pd.read_csv('matrix_factorization/user_data.csv').drop("Unnamed: 0",axis=1)
# print(list(users["user_id"].values))

app = Flask(__name__)
jsglue = JSGlue(app)

app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/2018Movies.sqlite'
db = SQLAlchemy(app)

Base = automap_base()


Base.prepare(db.engine, reflect=True)
Ratings_Data = Base.classes.movie_ratings

@app.route("/", methods=["GET", "POST"])
def home():
    # # u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code', '#_ratings', 'RMSE']
    # # users = pd.read_csv('matrix_factorization/user_data.csv').drop("Unnamed: 0",axis=1)
    # # print(list(users["user_id"].values))
    if request.method == "GET":
        movies = mtr.moviestorate()
    #     user_id = randint(1,948)
    #     user_data = mp.user_data(user_id)
    #     user_rec = mp.top5rec(user_id)
        return render_template("index.html", movies=movies)

    # if request.method == "POST":
    #     user_id = request.form["userId"]
    #     if user_id in list(users["user_id"].values.astype(str)):
    #         user_data = mp.user_data(user_id)
    #         user_rec = mp.top5rec(user_id)
    #         return render_template("index.html", user_data=user_data, user_rec=user_rec)
    #     else:
    #         return render_template("error.html")

# @app.route("/movies")
# def movies():
#     i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
#     'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
#     'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']


#     items = pd.read_csv("matrix_factorization/data/ml-100k/u.item", sep='|', names=i_cols,
#     encoding='latin-1')

#     items_dict = []
#     for i,row in enumerate(items.values):
#         movie = {
#             "movie_id": row[0],
#             "movie_title": row[1],
#             "release_date": row[2],
#             "IMDb_URL": row[4]
#         }
#         items_dict.append(movie)

#     return jsonify(items_dict)

@app.route("/movies/popular")
def popular_movies():
    movies = mtr.moviestorate()

    return jsonify(movies)

@app.route("/user/<user_id>")
def recommender(user_id):

    # Should use deep_learning_prediction.py to 
    # predict movies based on ratings given after 
    # submit button. 

    return jsonify(user_dict)


if __name__ == "__main__":
    app.run()
