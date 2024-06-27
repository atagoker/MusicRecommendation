from flask import Flask, jsonify
import os
import pickle
import numpy as np

app = Flask(__name__)

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, '..', 'models', 'recommendation_model.pkl')

def load_model():
    with open(model_path, 'rb') as file:
        return pickle.load(file)

@app.route('/recommend/<int:user_id>', methods=['GET'])
def recommend(user_id):
    try:
        model = load_model()
        recommendations = model.recommend(user_id, np.random.rand(10, 10), np.random.rand(10, 5), 5)
        return jsonify(recommendations.tolist())
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)
