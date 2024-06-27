import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import os

current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir, '..', 'data', 'datasets', 'processed')

def load_data(filename):
    """Loads processed data."""
    file_path = os.path.join(data_dir, filename)
    return pd.read_json(file_path)

def train_model(data):
    """Trains a simple collaborative filtering model."""
    user_item_matrix = csr_matrix((np.random.randint(1, 100, size=len(data)),
                                   (np.random.randint(0, 10, size=len(data)),
                                    np.arange(len(data)))))
    
    model = NearestNeighbors(metric='cosine', algorithm='brute')
    model.fit(user_item_matrix)
    
    return model

def save_model(model, filename):
    """Saves the trained model."""
    model_path = os.path.join(current_dir, filename)
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)

def main():
    """Main function to load data, train model, and save it."""
    try:
        data = load_data('processed_new_releases.json')
        model = train_model(data)
        save_model(model, 'recommendation_model.pkl')
        print("Model training successful")
    except Exception as e:
        print(f"Error during model training: {e}")

if __name__ == "__main__":
    main()

