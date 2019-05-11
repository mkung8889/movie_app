# import dependencies
import pandas as pd

# read ratings csv
ratings = pd.read_csv("../data/ml-100k/ratings.csv")

# only select ratings of "5"
ratings = ratings[ratings.rating == 5.0]

# count 5 star ratings for each movie
ratings = ratings.groupby(["movieId"]).count()

# sort by most 5 star ratings received and limit to 20 movies
ratings = ratings.sort_values(by=['rating'], ascending=False).head(30)

# read the movies csv and extract the year from the title
movies = pd.read_csv("../data/ml-100k/movies.csv")
movies['year'] = movies['title'].str.extract('.*\((.*)\).*')
print(movies.head())

# read the imdb data
links = pd.read_csv("../data/ml-100k/links.csv")

# merge the ratings and movies df
df = pd.merge(ratings, movies, on="movieId", how="left")
df

# merge the df with the links
df = pd.merge(df, links, on="movieId", how="left")
df

# drop unnecessary columns
df.drop(['userId', 'timestamp', 'genres', 'tmdbId'],axis=1, inplace=True)

# adding prefix 
df['imdbId'] = 'tt0' + df['imdbId'].astype(str)
df


