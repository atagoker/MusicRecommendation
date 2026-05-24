# Sweetify Music Recommendation System

Sweetify is a lightweight music recommendation project with a Flask web interface. It asks for the last three songs a user listened to, or simply three songs they remember, then recommends one new track from a local Spotify-style catalog.

The app works immediately after cloning. No Spotify account, API token, database, or model file is required for the main demo flow.

## Highlights

- Three-song personalization flow
- 100+ track local Spotify-style catalog
- Recommendation scoring with genre, mood, energy, valence, and danceability
- Match explanation for the selected song
- Spotify search link for the recommendation
- Flask web app with responsive styling
- Existing collaborative, content-based, and hybrid model modules
- Test-friendly fallback data for Spotify collection utilities

## Demo Flow

1. Open the web app.
2. Enter three songs you recently listened to or remember.
3. Sweetify matches them against the local catalog.
4. The app returns one focused recommendation with a match score and Spotify link.

Example inputs:

```text
Arctic Monkeys - 505
Radiohead - Weird Fishes
Beach House - Space Song
```

## Quick Start

Install dependencies:

```bash
python -m pip install -r docs/requirements.txt
```

Run the app:

```bash
python -m app.server
```

Open the app:

```text
http://127.0.0.1:5000/
```

## API Usage

Endpoint:

```http
POST /api/recommendations
Content-Type: application/json
```

Request body:

```json
{
  "songs": [
    "Tame Impala - Borderline",
    "Frank Ocean - Nights",
    "Bicep - Glue"
  ]
}
```

Example response shape:

```json
{
  "recommendations": [
    {
      "title": "Midnight City",
      "artist": "M83",
      "match_score": 72,
      "why": "It keeps the electronic side and the night feeling from your inputs.",
      "spotify_url": "https://open.spotify.com/search/Midnight+City+M83"
    }
  ],
  "matched_inputs": [
    { "title": "Borderline", "artist": "Tame Impala" }
  ],
  "catalog_size": 102,
  "source": "local-spotify-style-catalog"
}
```

## Project Tree

```text
music-recommendation/
|-- app/
|   |-- recommendation_engine.py   # Local catalog and similarity scoring
|   |-- server.py                  # Flask app and API routes
|   |-- routes.py                  # Compatibility entry point
|   |-- static/
|   |   |-- css/
|   |   |   `-- style.css
|   |   |-- js/
|   |   |   `-- main.js
|   |   `-- images/
|   `-- templates/
|       |-- index.html
|       `-- recommendations.html
|-- data/
|   |-- data_collection.py
|   |-- data_preprocessing.py
|   `-- datasets/
|       |-- raw/
|       |   `-- .gitkeep
|       `-- processed/
|           `-- .gitkeep
|-- models/
|   |-- collaborative_filtering.py
|   |-- content_based_filtering.py
|   |-- hybrid_model.py
|   `-- train_model.py
|-- recommendations/
|   |-- evaluate_model.py
|   `-- generate_recommendations.py
|-- tests/
|   |-- test_data_collection.py
|   |-- test_data_preprocessing.py
|   |-- test_models.py
|   `-- test_recommendations.py
|-- utils/
|   |-- data_utils.py
|   |-- model_utils.py
|   `-- recommendation_utils.py
|-- docs/
|   |-- README.md
|   |-- installation_guide.md
|   |-- requirements.txt
|   `-- user_manual.md
|-- config.py
|-- logging_config.py
|-- setup.py
`-- deploy.sh
```

## How Recommendations Work

The main demo uses `app/recommendation_engine.py`.

1. Each user input is fuzzy-matched against the local catalog.
2. The matched songs are averaged across audio-style features.
3. Candidate songs are scored by feature distance, genre overlap, mood overlap, and popularity.
4. Songs already used as inputs are filtered out.
5. The highest-scoring candidate is returned with a short explanation.

## Testing

Run the full test suite:

```bash
python -m pytest -q
```

Expected result:

```text
10 passed
```

## Notes

- The primary web demo does not require `SPOTIFY_API_TOKEN`.
- If a Spotify token is available, the data collection utility can still use it.
- The Spotify button opens a search URL for the recommendation instead of requiring OAuth.
