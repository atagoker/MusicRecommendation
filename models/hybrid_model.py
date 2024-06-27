from .collaborative_filtering import CollaborativeFiltering
from .content_based_filtering import ContentBasedFiltering

class HybridModel:
    def __init__(self, n_neighbors=5, metric='cosine'):
        self.cf_model = CollaborativeFiltering(n_neighbors, metric)
        self.cb_model = ContentBasedFiltering()
    
    def fit(self, user_item_matrix, item_features):
        self.cf_model.fit(user_item_matrix)
        self.cb_model.fit(item_features)
    
    def recommend(self, user_id, user_item_matrix, item_features, n_recommendations=5):
        cf_recommendations = self.cf_model.recommend(user_id, user_item_matrix, n_recommendations)
        cb_recommendations = self.cb_model.recommend(cf_recommendations[0], n_recommendations)
        return cb_recommendations
