import pickle
import numpy as np
import os

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, '..', 'models', 'recommendation_model.pkl')

def load_model(filename):
    """Loads the trained model."""
    with open(filename, 'rb') as file:
        return pickle.load(file)

def generate_recommendations(model, user_id, n_recommendations=5):
    """Generates recommendations for a given user."""
    distances, indices = model.kneighbors(np.random.rand(1, model._fit_X.shape[1]), n_neighbors=n_recommendations)
    return indices.flatten()

def main():
    """Main function to load the model and generate recommendations."""
    try:
        model = load_model(model_path)
        recommendations = generate_recommendations(model, user_id=0)
        print(f"Recommendations: {recommendations}")
    except Exception as e:
        print(f"Error during recommendation generation: {e}")

if __name__ == "__main__":
    main()

