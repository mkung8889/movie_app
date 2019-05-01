import pandas as pd

ratings = pd.read_csv('ml-20m/ratings.csv', encoding='latin-1')
items = pd.read_csv('ml-20m/movies.csv', encoding='latin-1')
df = pd.merge(ratings, items, on="movieId")
genres = pd.get_dummies(df.genres.str.split('|',expand=True).stack()).sum(level=0)
df = pd.concat([df,genres], axis=1)
data = df.drop(['timestamp', 'title', 'genres'],axis=1, inplace=True)
datacsv = df.to_csv("ml-20m/201820M.csv")

print("finished encoding")