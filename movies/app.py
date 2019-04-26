from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import movies.movie_prediction as mp

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_id = request.form["userId"]
        user_data = mp.user_data(user_id)
        user_rec = mp.top5rec(user_id)
        return render_template("index.html", user_data=user_data, user_rec=user_rec)   
    else:  
        return render_template("index.html",user_data =1)
    return render_template("index.html", user_data =1)

@app.route("/movies")
def movies():
    i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
    'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
    'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']


    items = pd.read_csv("matrix_factorization/data/ml-100k/u.item", sep='|', names=i_cols,
    encoding='latin-1')

    items_dict = []
    for i,row in enumerate(items.values):
        movie = {
            "movie_id": row[0],
            "movie_title": row[1],
            "release_date": row[2],
            "IMDb_URL": row[4]
        }
        items_dict.append(movie)

    return jsonify(items_dict)

@app.route("/movies/recommended/<user_id>")
def movie_rec(user_id):
    rec_movies = mp.top5rec(user_id)

    return jsonify(rec_movies)

@app.route("/user/<user_id>")
def user_data(user_id):
    user_dict = mp.user_data(user_id)

    return jsonify(user_dict)



if __name__ == "__main__":
    app.run()
