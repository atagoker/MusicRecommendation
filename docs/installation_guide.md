# Installation Guide

## Prerequisites

- Python 3.6+
- Virtual environment (optional but recommended)

## Installation Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/music_recommendation_system.git
    cd music_recommendation_system
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    - Create a `.env` file in the root directory of the project.
    - Add your environment variables (e.g., `SPOTIFY_API_TOKEN`, `DATABASE_URL`).

5. Run the application:

    ```sh
    python app/server.py
    ```

