from flask import Flask, jsonify, render_template, request
import os
import pickle

try:
    from .recommendation_engine import recommend_from_songs
except ImportError:
    from recommendation_engine import recommend_from_songs

app = Flask(__name__)

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, '..', 'models', 'recommendation_model.pkl')


def load_model():
    """Loads the trained model."""
    with open(model_path, 'rb') as file:
        return pickle.load(file)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/api/recommendations', methods=['POST'])
def api_recommendations():
    payload = request.get_json(silent=True) or {}
    songs = payload.get('songs', [])
    if not isinstance(songs, list):
        songs = []

    cleaned_songs = [str(song).strip() for song in songs if str(song).strip()]
    if len(cleaned_songs) < 3:
        return jsonify({
            "error": "Please enter the last 3 songs you listened to or remember.",
        }), 400

    return jsonify({
        **recommend_from_songs(cleaned_songs[:3], count=1),
        "source": "local-spotify-style-catalog",
    })


@app.route('/recommend/<int:user_id>', methods=['GET'])
def recommend(user_id):
    """Legacy endpoint kept for older clients."""
    songs = [
        request.args.get('song1', 'Borderline Tame Impala'),
        request.args.get('song2', 'Nights Frank Ocean'),
        request.args.get('song3', 'Glue Bicep'),
    ]
    return jsonify(recommend_from_songs(songs, count=1)["recommendations"])


if __name__ == "__main__":
    app.run(debug=True)
