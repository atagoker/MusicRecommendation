import unittest
import numpy as np
from models.collaborative_filtering import CollaborativeFiltering
from models.content_based_filtering import ContentBasedFiltering
from models.hybrid_model import HybridModel

class TestCollaborativeFiltering(unittest.TestCase):
    def test_fit(self):
        model = CollaborativeFiltering()
        user_item_matrix = np.random.rand(10, 5)
        model.fit(user_item_matrix)
        self.assertTrue(model.model)

    def test_recommend(self):
        model = CollaborativeFiltering()
        user_item_matrix = np.random.rand(10, 5)
        model.fit(user_item_matrix)
        recommendations = model.recommend(0, user_item_matrix, 5)
        self.assertEqual(len(recommendations), 5)

class TestContentBasedFiltering(unittest.TestCase):
    def test_fit(self):
        model = ContentBasedFiltering()
        item_features = np.random.rand(10, 5)
        model.fit(item_features)
        self.assertTrue(model.item_similarity is not None)

    def test_recommend(self):
        model = ContentBasedFiltering()
        item_features = np.random.rand(10, 5)
        model.fit(item_features)
        recommendations = model.recommend(0, 5)
        self.assertEqual(len(recommendations), 5)

class TestHybridModel(unittest.TestCase):
    def test_fit(self):
        model = HybridModel()
        user_item_matrix = np.random.rand(10, 5)
        item_features = np.random.rand(10, 5)
        model.fit(user_item_matrix, item_features)
        self.assertTrue(model.cf_model.model)
        self.assertTrue(model.cb_model.item_similarity is not None)

    def test_recommend(self):
        model = HybridModel()
        user_item_matrix = np.random.rand(10, 5)
        item_features = np.random.rand(10, 5)
        model.fit(user_item_matrix, item_features)
        recommendations = model.recommend(0, user_item_matrix, item_features, 5)
        self.assertEqual(len(recommendations), 5)

if __name__ == '__main__':
    unittest.main()
