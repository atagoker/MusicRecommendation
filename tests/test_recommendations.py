import unittest
from recommendations.generate_recommendations import generate_recommendations

class TestGenerateRecommendations(unittest.TestCase):
    def test_generate_recommendations(self):
        # Dummy model and data for testing
        class DummyModel:
            def kneighbors(self, X, n_neighbors):
                return None, [[1, 2, 3, 4, 5]]

        model = DummyModel()
        recommendations = generate_recommendations(model, user_id=0)
        self.assertEqual(len(recommendations), 5)

if __name__ == '__main__':
    unittest.main()
