import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class ContentBasedFiltering:
    def __init__(self):
        self.item_similarity = None
    
    def fit(self, item_features):
        self.item_similarity = cosine_similarity(item_features)
    
    def recommend(self, item_id, n_recommendations=5):
        similar_items = np.argsort(self.item_similarity[item_id])[::-1]
        return similar_items[:n_recommendations]
