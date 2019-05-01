# A simple implementation of matrix factorization for collaborative filtering expressed as a Keras Sequential model

# Keras uses TensorFlow tensor library as the backend system to do the heavy compiling

import numpy as np
from keras.layers import Input, Embedding, dot, Dense, Reshape
from keras.models import Model, Sequential

class CFModel(Model):

    # The constructor for the class
    def __init__(self, n_users, m_items, k_factors, **kwargs):
        # P is the embedding layer that creates an User by latent factors matrix.
        # If the intput is a user_id, P returns the latent factor vector for that user.
        user_input = Input(shape=(1,), name='user_input')
        x = Embedding(input_dim=n_users, output_dim=k_factors, input_length=1)(user_input)
        user_output = Reshape((k_factors,))(x)

        # Q is the embedding layer that creates a Movie by latent factors matrix.
        # If the input is a movie_id, Q returns the latent factor vector for that movie.
        movie_input = Input(shape=(1,), name='movie_input')
        y = Embedding(input_dim=m_items, output_dim=k_factors, input_length=1)(movie_input)
        movie_output = Reshape((k_factors,))(y)
        
        # The Merge layer takes the dot product of user and movie latent factor vectors to return the corresponding rating.
        z = dot([Dense(10)(user_output), Dense(10)(movie_output)], axes=1)

        self.Model(inputs=[user_input, movie_input], outputs=z)

    # The rate function to predict user's rating of unrated items
    def rate(self, user_id, item_id):
        return self.predict([np.array([user_id]), np.array([item_id])])[0][0]
