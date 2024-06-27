# User Manual

## Overview

This user manual provides instructions on how to use the Music Recommendation System.

## Getting Recommendations

1. Open the web application in your browser.

2. Enter your user ID in the input field.

3. Click on the "Get Recommendations" button.

4. The system will display a list of recommended items based on your user ID.

## API Endpoints

### `GET /recommend/<user_id>`

- Returns a list of recommended items for the specified user ID.

#### Example Request

```sh
curl http://localhost:5000/recommend/1
