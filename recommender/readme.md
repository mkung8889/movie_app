inspired from: https://www.analyticsvidhya.com/blog/2016/06/quick-guide-build-recommendation-engine-python/

The Jupyter Notebook  covers:
    a) Simple Popularity Model
    b) Collaborative Filtering Model (using Cosine Similarity)
    c) Evaluates the above Recommendation Engines (in terms of Recall and Precision)

data set from: https://grouplens.org/datasets/movielens/100k/   
    all the data for this script is located in the data subfolder


to use graphlab you will need to register for an academic account
https://turi.com/download/academic.html

You will then get an email, with instructions on how to set it up.

I followed the Install GraphLab Create with Command Line, as the laucher failed on me multiple times.

1) # Create a new conda environment with Python 2.7.x
conda create -n gl-env python=2.7

2) # Activate the conda environment
activate gl-env

3) # Install your licensed copy of GraphLab Create
pip install --upgrade --no-cache-dir https://get.graphlab.com/GraphLab-Create/2.1/yourname@youremail.com/yourkey/GraphLab-Create-License.tar.gz

