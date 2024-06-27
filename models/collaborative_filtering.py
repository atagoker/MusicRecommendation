import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

class CollaborativeFiltering:
    def __init__(self, n_neighbors=5, metric='cosine'):
        self.n_neighbors = n_neighbors
        self.metric = metric
        self.model = NearestNeighbors(n_neighbors=self.n_neighbors, metric=self.metric, algorithm='brute')
    
    def fit(self, user_item_matrix):
        self.model.fit(user_item_matrix)
    
    def recommend(self, user_id, user_item_matrix, n_recommendations=5):
        distances, indices = self.model.kneighbors(user_item_matrix[user_id], n_neighbors=n_recommendations)
        return indices.flatten()

