from scipy.sparse import dok_matrix
from sklearn.metrics.pairwise import pairwise_distances

import numpy as np

# Set random seed (for reproducibility)
np.random.seed(1000)

# Create a dummy user-item dataset
nb_users = 1000
nb_products = 2500
max_rating = 5
max_rated_products = 500

X_preferences = dok_matrix((nb_users, nb_products), dtype=np.uint8)

for i in range(nb_users):
    # Extract n random products
    n_products = np.random.randint(0, max_rated_products+1)
    products = np.random.randint(0, nb_products, size=n_products)
    
    # Populate preference sparse matrix
    for p in products:
        X_preferences[i, p] = np.random.randint(0, max_rating+1)
        
# Compute pairwise distances
distance_matrix = pairwise_distances(X_preferences, metric='euclidean')

# Sort distances
sorted_distances = np.argsort(distance_matrix, axis=1)