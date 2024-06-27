from flask import Flask, jsonify
import os
import pickle
import numpy as np

app = Flask(__name__)

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, '..', 'models', 'recommendation_model.pkl')

def load_model():
    """Loads the trained model."""
    with open(model_path, 'rb') as file:
        return pickle.load(file)

@app.route('/recommend/<int:user_id>', methods=['GET'])
def recommend(user_id):
    """Generates recommendations for a given user."""
    try:
        model = load_model()
        recommendations = model.kneighbors(np.random.rand(1, model._fit_X.shape[1]), n_neighbors=5)[1].flatten().tolist()
        return jsonify(recommendations)
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)

