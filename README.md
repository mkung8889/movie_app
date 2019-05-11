# Cinematrix 
by Michael Kung, Pablo Maceda, Dexter D'Cruz, Kerry Kovacik & Kristen Cannon

### Cinematrix App:
https://movie-suggestion-app.herokuapp.com/

### Sources:
grouplens MovieLens data sets
https://grouplens.org/datasets/movielens/

### App Versions:

Version 2: Used the 2018 100k data set due to it being the most up to date and being a smaller size for use with students. 
https://grouplens.org/datasets/movielens/latest/

* The app was revised to show 20 of the most popular movies in this dataset for the user to rate. Based on the user input, their top 5 movie recommendations are shown.

Version 1: Used the 1998 100k data set (for most models) due to additional user data, pre feature engineered one hot encoding of the movie genres as well as the smaller sizing for use with students. 
https://grouplens.org/datasets/movielens/100k/

* The app displayed the top 5 movie receommendations based on userid. Each team member rating at least 20 movies and appended the data with their ratings to be included in training and predictions of the top 5 recommendations. 

* Used the 20M 2018 data set for the deep learning model.
https://grouplens.org/datasets/movielens/20m/

### Models explored:
* Decision Tree
* Random Forest
* Recommender
    * GraphLab Popularity
    * GraphLab Item Similarity
    * Turicreate Factorization
    * Turicreate Popularity
* Matrix Factorization
* Deep Learning

### Tools:
* GraphLab: https://pypi.org/project/GraphLab-Create/
* scikit-learn: https://scikit-learn.org/stable/
* Turicreate: https://github.com/apple/turicreate
* Pandas: https://pandas.pydata.org/
* Numpy: https://www.numpy.org/
* Matplotlib: https://matplotlib.org/
* Tableau: https://www.tableau.com/
* Seaborn: https://seaborn.pydata.org/
* Flask: http://flask.pocoo.org/
* TensorFlow: https://www.tensorflow.org/
* Keras: https://keras.io/
* HTML, CSS
