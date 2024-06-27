import pickle
import numpy as np
import os

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, '..', 'models', 'recommendation_model.pkl')

def load_model(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

def evaluate_model(model, user_item_matrix, n_recommendations=5):
    user_id = np.random.randint(0, user_item_matrix.shape[0])
    recommendations = model.recommend(user_id, user_item_matrix, np.random.rand(user_item_matrix.shape[0], 5), n_recommendations)
    return recommendations

def main():
    try:
        model = load_model(model_path)
        user_item_matrix = csr_matrix(np.random.rand(10, 10))
        recommendations = evaluate_model(model, user_item_matrix)
        print(f"Recommendations: {recommendations}")
    except Exception as e:
        print(f"Error during model evaluation: {e}")

if __name__ == "__main__":
    main()
