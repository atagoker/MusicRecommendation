from urllib.parse import quote_plus
import difflib
import math
import re


CATALOG = [
    {"title": "Borderline", "artist": "Tame Impala", "genres": ["psychedelic pop", "indie"], "moods": ["dreamy", "night"], "energy": 0.62, "valence": 0.55, "danceability": 0.67, "popularity": 86},
    {"title": "The Less I Know The Better", "artist": "Tame Impala", "genres": ["psychedelic pop", "indie"], "moods": ["groovy", "bittersweet"], "energy": 0.74, "valence": 0.78, "danceability": 0.64, "popularity": 90},
    {"title": "Do I Wanna Know?", "artist": "Arctic Monkeys", "genres": ["indie rock", "alt rock"], "moods": ["dark", "late night"], "energy": 0.53, "valence": 0.40, "danceability": 0.55, "popularity": 91},
    {"title": "505", "artist": "Arctic Monkeys", "genres": ["indie rock", "alt rock"], "moods": ["melancholy", "crescendo"], "energy": 0.64, "valence": 0.28, "danceability": 0.52, "popularity": 88},
    {"title": "Sweet Disposition", "artist": "The Temper Trap", "genres": ["indie rock", "indie pop"], "moods": ["uplifting", "cinematic"], "energy": 0.82, "valence": 0.50, "danceability": 0.46, "popularity": 78},
    {"title": "Electric Feel", "artist": "MGMT", "genres": ["indie pop", "electropop"], "moods": ["groovy", "retro"], "energy": 0.78, "valence": 0.76, "danceability": 0.75, "popularity": 84},
    {"title": "Midnight City", "artist": "M83", "genres": ["synthpop", "electronic"], "moods": ["night", "cinematic"], "energy": 0.84, "valence": 0.43, "danceability": 0.53, "popularity": 83},
    {"title": "Intro", "artist": "The xx", "genres": ["indie electronic", "minimal"], "moods": ["night", "calm"], "energy": 0.45, "valence": 0.20, "danceability": 0.42, "popularity": 80},
    {"title": "Angels", "artist": "The xx", "genres": ["indie electronic", "minimal"], "moods": ["intimate", "calm"], "energy": 0.31, "valence": 0.23, "danceability": 0.36, "popularity": 75},
    {"title": "Retrograde", "artist": "James Blake", "genres": ["alt r&b", "electronic"], "moods": ["soulful", "dark"], "energy": 0.48, "valence": 0.25, "danceability": 0.43, "popularity": 74},
    {"title": "Limit To Your Love", "artist": "James Blake", "genres": ["alt r&b", "electronic"], "moods": ["minimal", "deep"], "energy": 0.34, "valence": 0.18, "danceability": 0.38, "popularity": 70},
    {"title": "Nights", "artist": "Frank Ocean", "genres": ["alt r&b", "neo soul"], "moods": ["late night", "reflective"], "energy": 0.56, "valence": 0.42, "danceability": 0.59, "popularity": 88},
    {"title": "Pink + White", "artist": "Frank Ocean", "genres": ["alt r&b", "neo soul"], "moods": ["warm", "nostalgic"], "energy": 0.55, "valence": 0.54, "danceability": 0.54, "popularity": 87},
    {"title": "Redbone", "artist": "Childish Gambino", "genres": ["funk", "neo soul"], "moods": ["groovy", "warm"], "energy": 0.36, "valence": 0.64, "danceability": 0.74, "popularity": 89},
    {"title": "Come Through and Chill", "artist": "Miguel", "genres": ["r&b", "neo soul"], "moods": ["smooth", "romantic"], "energy": 0.50, "valence": 0.48, "danceability": 0.63, "popularity": 73},
    {"title": "Cranes in the Sky", "artist": "Solange", "genres": ["neo soul", "r&b"], "moods": ["soft", "reflective"], "energy": 0.37, "valence": 0.33, "danceability": 0.62, "popularity": 75},
    {"title": "Good Days", "artist": "SZA", "genres": ["r&b", "neo soul"], "moods": ["dreamy", "healing"], "energy": 0.50, "valence": 0.41, "danceability": 0.44, "popularity": 86},
    {"title": "Supermodel", "artist": "SZA", "genres": ["r&b", "neo soul"], "moods": ["raw", "melancholy"], "energy": 0.44, "valence": 0.32, "danceability": 0.53, "popularity": 76},
    {"title": "Japanese Denim", "artist": "Daniel Caesar", "genres": ["r&b", "soul"], "moods": ["romantic", "slow"], "energy": 0.36, "valence": 0.35, "danceability": 0.48, "popularity": 80},
    {"title": "Best Part", "artist": "Daniel Caesar, H.E.R.", "genres": ["r&b", "soul"], "moods": ["romantic", "warm"], "energy": 0.29, "valence": 0.44, "danceability": 0.52, "popularity": 86},
    {"title": "No Problem", "artist": "Chance the Rapper", "genres": ["hip hop", "gospel rap"], "moods": ["bright", "confident"], "energy": 0.79, "valence": 0.72, "danceability": 0.66, "popularity": 76},
    {"title": "Money Trees", "artist": "Kendrick Lamar", "genres": ["hip hop", "west coast rap"], "moods": ["smooth", "reflective"], "energy": 0.53, "valence": 0.39, "danceability": 0.70, "popularity": 88},
    {"title": "LOVE.", "artist": "Kendrick Lamar, Zacari", "genres": ["hip hop", "r&b"], "moods": ["romantic", "soft"], "energy": 0.59, "valence": 0.49, "danceability": 0.80, "popularity": 87},
    {"title": "Self Care", "artist": "Mac Miller", "genres": ["hip hop", "cloud rap"], "moods": ["reflective", "late night"], "energy": 0.55, "valence": 0.32, "danceability": 0.73, "popularity": 84},
    {"title": "Dang!", "artist": "Mac Miller, Anderson .Paak", "genres": ["hip hop", "funk"], "moods": ["groovy", "sunny"], "energy": 0.70, "valence": 0.74, "danceability": 0.84, "popularity": 77},
    {"title": "Am I Wrong", "artist": "Anderson .Paak, ScHoolboy Q", "genres": ["funk", "hip hop"], "moods": ["groovy", "confident"], "energy": 0.78, "valence": 0.76, "danceability": 0.80, "popularity": 72},
    {"title": "Them Changes", "artist": "Thundercat", "genres": ["funk", "jazz fusion"], "moods": ["groovy", "bittersweet"], "energy": 0.58, "valence": 0.66, "danceability": 0.79, "popularity": 77},
    {"title": "Dragonball Durag", "artist": "Thundercat", "genres": ["funk", "jazz fusion"], "moods": ["playful", "smooth"], "energy": 0.48, "valence": 0.70, "danceability": 0.78, "popularity": 70},
    {"title": "Mystery Lady", "artist": "Masego, Don Toliver", "genres": ["r&b", "jazz rap"], "moods": ["smooth", "night"], "energy": 0.56, "valence": 0.55, "danceability": 0.76, "popularity": 75},
    {"title": "Tadow", "artist": "Masego, FKJ", "genres": ["r&b", "jazz fusion"], "moods": ["smooth", "live"], "energy": 0.52, "valence": 0.58, "danceability": 0.70, "popularity": 74},
    {"title": "Ylang Ylang", "artist": "FKJ", "genres": ["electronic", "jazz"], "moods": ["calm", "focus"], "energy": 0.32, "valence": 0.45, "danceability": 0.50, "popularity": 68},
    {"title": "Glue", "artist": "Bicep", "genres": ["house", "electronic"], "moods": ["euphoric", "night"], "energy": 0.76, "valence": 0.50, "danceability": 0.71, "popularity": 76},
    {"title": "Apricots", "artist": "Bicep", "genres": ["house", "electronic"], "moods": ["hypnotic", "club"], "energy": 0.82, "valence": 0.47, "danceability": 0.73, "popularity": 70},
    {"title": "Innerbloom", "artist": "RUFUS DU SOL", "genres": ["melodic house", "electronic"], "moods": ["cinematic", "emotional"], "energy": 0.61, "valence": 0.31, "danceability": 0.55, "popularity": 78},
    {"title": "On Hold", "artist": "The xx", "genres": ["indie electronic", "dance"], "moods": ["bittersweet", "groovy"], "energy": 0.70, "valence": 0.55, "danceability": 0.71, "popularity": 74},
    {"title": "Virile", "artist": "The Blaze", "genres": ["electronic", "french house"], "moods": ["cinematic", "deep"], "energy": 0.63, "valence": 0.36, "danceability": 0.61, "popularity": 65},
    {"title": "Territory", "artist": "The Blaze", "genres": ["electronic", "french house"], "moods": ["cinematic", "emotional"], "energy": 0.66, "valence": 0.38, "danceability": 0.58, "popularity": 70},
    {"title": "A Moment Apart", "artist": "ODESZA", "genres": ["electronic", "future bass"], "moods": ["cinematic", "uplifting"], "energy": 0.74, "valence": 0.52, "danceability": 0.50, "popularity": 72},
    {"title": "Line of Sight", "artist": "ODESZA, WYNNE, Mansionair", "genres": ["electronic", "future bass"], "moods": ["bright", "wide"], "energy": 0.68, "valence": 0.58, "danceability": 0.59, "popularity": 69},
    {"title": "Shelter", "artist": "Porter Robinson, Madeon", "genres": ["electronic", "future bass"], "moods": ["uplifting", "nostalgic"], "energy": 0.79, "valence": 0.55, "danceability": 0.55, "popularity": 78},
    {"title": "Something About Us", "artist": "Daft Punk", "genres": ["french house", "electronic"], "moods": ["romantic", "warm"], "energy": 0.46, "valence": 0.60, "danceability": 0.72, "popularity": 79},
    {"title": "Digital Love", "artist": "Daft Punk", "genres": ["french house", "electronic"], "moods": ["bright", "retro"], "energy": 0.88, "valence": 0.80, "danceability": 0.64, "popularity": 80},
    {"title": "Teardrop", "artist": "Massive Attack", "genres": ["trip hop", "electronic"], "moods": ["dark", "atmospheric"], "energy": 0.42, "valence": 0.22, "danceability": 0.62, "popularity": 79},
    {"title": "Roads", "artist": "Portishead", "genres": ["trip hop", "downtempo"], "moods": ["melancholy", "smoky"], "energy": 0.30, "valence": 0.18, "danceability": 0.40, "popularity": 72},
    {"title": "All I Need", "artist": "Radiohead", "genres": ["art rock", "alt rock"], "moods": ["dark", "intense"], "energy": 0.48, "valence": 0.19, "danceability": 0.44, "popularity": 78},
    {"title": "Weird Fishes/ Arpeggi", "artist": "Radiohead", "genres": ["art rock", "alt rock"], "moods": ["hypnotic", "deep"], "energy": 0.60, "valence": 0.34, "danceability": 0.52, "popularity": 81},
    {"title": "Space Song", "artist": "Beach House", "genres": ["dream pop", "indie"], "moods": ["dreamy", "melancholy"], "energy": 0.44, "valence": 0.30, "danceability": 0.51, "popularity": 86},
    {"title": "Myth", "artist": "Beach House", "genres": ["dream pop", "indie"], "moods": ["dreamy", "wide"], "energy": 0.54, "valence": 0.36, "danceability": 0.46, "popularity": 76},
    {"title": "Apocalypse", "artist": "Cigarettes After Sex", "genres": ["dream pop", "slowcore"], "moods": ["romantic", "melancholy"], "energy": 0.32, "valence": 0.23, "danceability": 0.37, "popularity": 86},
    {"title": "Sweet", "artist": "Cigarettes After Sex", "genres": ["dream pop", "slowcore"], "moods": ["romantic", "soft"], "energy": 0.28, "valence": 0.38, "danceability": 0.42, "popularity": 78},
    {"title": "Motion Picture Soundtrack", "artist": "Radiohead", "genres": ["art rock", "baroque pop"], "moods": ["sad", "cinematic"], "energy": 0.18, "valence": 0.10, "danceability": 0.25, "popularity": 67},
    {"title": "I Know The End", "artist": "Phoebe Bridgers", "genres": ["indie folk", "singer-songwriter"], "moods": ["melancholy", "crescendo"], "energy": 0.56, "valence": 0.22, "danceability": 0.38, "popularity": 76},
    {"title": "Kyoto", "artist": "Phoebe Bridgers", "genres": ["indie rock", "singer-songwriter"], "moods": ["bright", "anxious"], "energy": 0.72, "valence": 0.56, "danceability": 0.55, "popularity": 75},
    {"title": "Motion Sickness", "artist": "Phoebe Bridgers", "genres": ["indie rock", "singer-songwriter"], "moods": ["bittersweet", "sharp"], "energy": 0.64, "valence": 0.52, "danceability": 0.50, "popularity": 75},
    {"title": "Not Strong Enough", "artist": "boygenius", "genres": ["indie rock", "singer-songwriter"], "moods": ["bright", "bittersweet"], "energy": 0.73, "valence": 0.50, "danceability": 0.49, "popularity": 78},
    {"title": "Bags", "artist": "Clairo", "genres": ["bedroom pop", "indie"], "moods": ["soft", "nostalgic"], "energy": 0.55, "valence": 0.42, "danceability": 0.62, "popularity": 80},
    {"title": "Sofia", "artist": "Clairo", "genres": ["bedroom pop", "indie"], "moods": ["bright", "sweet"], "energy": 0.62, "valence": 0.70, "danceability": 0.74, "popularity": 82},
    {"title": "Lovers Rock", "artist": "TV Girl", "genres": ["indie pop", "lo-fi"], "moods": ["nostalgic", "playful"], "energy": 0.55, "valence": 0.71, "danceability": 0.69, "popularity": 87},
    {"title": "Chamber Of Reflection", "artist": "Mac DeMarco", "genres": ["indie", "lo-fi"], "moods": ["dreamy", "lonely"], "energy": 0.38, "valence": 0.35, "danceability": 0.62, "popularity": 82},
    {"title": "My Kind of Woman", "artist": "Mac DeMarco", "genres": ["indie", "lo-fi"], "moods": ["romantic", "lazy"], "energy": 0.42, "valence": 0.46, "danceability": 0.58, "popularity": 82},
    {"title": "Can I Call You Tonight?", "artist": "Dayglow", "genres": ["indie pop", "bedroom pop"], "moods": ["bright", "breezy"], "energy": 0.70, "valence": 0.82, "danceability": 0.77, "popularity": 78},
    {"title": "Brazil", "artist": "Declan McKenna", "genres": ["indie rock", "indie pop"], "moods": ["bright", "restless"], "energy": 0.78, "valence": 0.72, "danceability": 0.63, "popularity": 80},
    {"title": "Young Folks", "artist": "Peter Bjorn and John", "genres": ["indie pop", "indie rock"], "moods": ["whistly", "playful"], "energy": 0.70, "valence": 0.82, "danceability": 0.67, "popularity": 76},
    {"title": "Float On", "artist": "Modest Mouse", "genres": ["indie rock", "alt rock"], "moods": ["optimistic", "scrappy"], "energy": 0.82, "valence": 0.74, "danceability": 0.65, "popularity": 80},
    {"title": "Reptilia", "artist": "The Strokes", "genres": ["indie rock", "garage rock"], "moods": ["urgent", "cool"], "energy": 0.89, "valence": 0.62, "danceability": 0.49, "popularity": 82},
    {"title": "Someday", "artist": "The Strokes", "genres": ["indie rock", "garage rock"], "moods": ["nostalgic", "bright"], "energy": 0.74, "valence": 0.72, "danceability": 0.54, "popularity": 79},
    {"title": "Last Nite", "artist": "The Strokes", "genres": ["indie rock", "garage rock"], "moods": ["rowdy", "classic"], "energy": 0.91, "valence": 0.63, "danceability": 0.62, "popularity": 83},
    {"title": "Mr. Brightside", "artist": "The Killers", "genres": ["alt rock", "indie rock"], "moods": ["anthemic", "jealous"], "energy": 0.91, "valence": 0.23, "danceability": 0.36, "popularity": 91},
    {"title": "Somebody Told Me", "artist": "The Killers", "genres": ["alt rock", "dance rock"], "moods": ["urgent", "club rock"], "energy": 0.98, "valence": 0.70, "danceability": 0.51, "popularity": 81},
    {"title": "Dog Days Are Over", "artist": "Florence + The Machine", "genres": ["baroque pop", "indie rock"], "moods": ["explosive", "joyful"], "energy": 0.81, "valence": 0.55, "danceability": 0.50, "popularity": 82},
    {"title": "Shake It Out", "artist": "Florence + The Machine", "genres": ["baroque pop", "indie rock"], "moods": ["cathartic", "big"], "energy": 0.86, "valence": 0.36, "danceability": 0.43, "popularity": 75},
    {"title": "Dogtooth", "artist": "Tyler, The Creator", "genres": ["hip hop", "alt rap"], "moods": ["confident", "smooth"], "energy": 0.60, "valence": 0.58, "danceability": 0.73, "popularity": 75},
    {"title": "See You Again", "artist": "Tyler, The Creator, Kali Uchis", "genres": ["alt rap", "r&b"], "moods": ["dreamy", "romantic"], "energy": 0.56, "valence": 0.62, "danceability": 0.56, "popularity": 89},
    {"title": "After The Storm", "artist": "Kali Uchis, Tyler, The Creator, Bootsy Collins", "genres": ["r&b", "funk"], "moods": ["sunny", "smooth"], "energy": 0.60, "valence": 0.78, "danceability": 0.72, "popularity": 79},
    {"title": "Telepatia", "artist": "Kali Uchis", "genres": ["latin pop", "r&b"], "moods": ["warm", "romantic"], "energy": 0.52, "valence": 0.60, "danceability": 0.65, "popularity": 83},
    {"title": "Ego Death", "artist": "The Internet", "genres": ["neo soul", "funk"], "moods": ["smooth", "cool"], "energy": 0.62, "valence": 0.54, "danceability": 0.71, "popularity": 68},
    {"title": "Girl", "artist": "The Internet, KAYTRANADA", "genres": ["neo soul", "electronic"], "moods": ["smooth", "late night"], "energy": 0.54, "valence": 0.45, "danceability": 0.74, "popularity": 72},
    {"title": "Lite Spots", "artist": "KAYTRANADA", "genres": ["house", "dance"], "moods": ["groovy", "bright"], "energy": 0.78, "valence": 0.68, "danceability": 0.86, "popularity": 70},
    {"title": "10%", "artist": "KAYTRANADA, Kali Uchis", "genres": ["house", "r&b"], "moods": ["club", "smooth"], "energy": 0.72, "valence": 0.66, "danceability": 0.82, "popularity": 74},
    {"title": "Sevda Cicegi", "artist": "Mor ve Otesi", "genres": ["turkish rock", "alt rock"], "moods": ["melancholy", "anthemic"], "energy": 0.74, "valence": 0.34, "danceability": 0.45, "popularity": 63},
    {"title": "Bir Derdim Var", "artist": "Mor ve Otesi", "genres": ["turkish rock", "alt rock"], "moods": ["intense", "melancholy"], "energy": 0.82, "valence": 0.25, "danceability": 0.43, "popularity": 72},
    {"title": "Senden Daha Guzel", "artist": "Duman", "genres": ["turkish rock", "alt rock"], "moods": ["romantic", "gritty"], "energy": 0.78, "valence": 0.52, "danceability": 0.54, "popularity": 74},
    {"title": "Her Seyi Yak", "artist": "Duman", "genres": ["turkish rock", "grunge"], "moods": ["raw", "dark"], "energy": 0.86, "valence": 0.22, "danceability": 0.41, "popularity": 68},
    {"title": "Beni Sev", "artist": "Hande Yener", "genres": ["turkish pop", "dance pop"], "moods": ["club", "bright"], "energy": 0.88, "valence": 0.70, "danceability": 0.78, "popularity": 62},
    {"title": "Ask Kirintilari", "artist": "Teoman", "genres": ["turkish rock", "singer-songwriter"], "moods": ["melancholy", "romantic"], "energy": 0.50, "valence": 0.24, "danceability": 0.42, "popularity": 66},
    {"title": "Paramparca", "artist": "Teoman", "genres": ["turkish rock", "singer-songwriter"], "moods": ["dramatic", "melancholy"], "energy": 0.70, "valence": 0.30, "danceability": 0.43, "popularity": 70},
    {"title": "Belki Alisman Lazim", "artist": "Duman", "genres": ["turkish rock", "alt rock"], "moods": ["raw", "nostalgic"], "energy": 0.72, "valence": 0.42, "danceability": 0.49, "popularity": 66},
    {"title": "Firtinam", "artist": "Mabel Matiz", "genres": ["turkish pop", "art pop"], "moods": ["dramatic", "romantic"], "energy": 0.66, "valence": 0.48, "danceability": 0.60, "popularity": 70},
    {"title": "Antidepresan", "artist": "Mabel Matiz, Mert Demir", "genres": ["turkish pop", "alt pop"], "moods": ["melancholy", "catchy"], "energy": 0.61, "valence": 0.40, "danceability": 0.70, "popularity": 78},
    {"title": "Atese Dustum", "artist": "Mert Demir", "genres": ["turkish pop", "alt pop"], "moods": ["dramatic", "romantic"], "energy": 0.64, "valence": 0.46, "danceability": 0.65, "popularity": 76},
    {"title": "NKBI x Yapamam", "artist": "Lvbel C5, Gunes", "genres": ["turkish rap", "pop rap"], "moods": ["catchy", "club"], "energy": 0.80, "valence": 0.64, "danceability": 0.82, "popularity": 70},
    {"title": "Nerdesin", "artist": "Ezhel", "genres": ["turkish rap", "trap"], "moods": ["melancholy", "street"], "energy": 0.60, "valence": 0.35, "danceability": 0.72, "popularity": 72},
    {"title": "Aya", "artist": "Murda, Ezhel", "genres": ["turkish rap", "dancehall"], "moods": ["club", "summer"], "energy": 0.78, "valence": 0.72, "danceability": 0.86, "popularity": 75},
    {"title": "Perros Blancos Freestyle", "artist": "Ben Fero", "genres": ["turkish rap", "trap"], "moods": ["confident", "hard"], "energy": 0.86, "valence": 0.58, "danceability": 0.80, "popularity": 65},
    {"title": "Bana Ellerini Ver", "artist": "Ozdemir Erdogan", "genres": ["anatolian pop", "classic turkish"], "moods": ["warm", "nostalgic"], "energy": 0.40, "valence": 0.62, "danceability": 0.50, "popularity": 58},
    {"title": "Gulumse", "artist": "Sezen Aksu", "genres": ["turkish pop", "classic turkish"], "moods": ["warm", "nostalgic"], "energy": 0.45, "valence": 0.58, "danceability": 0.52, "popularity": 68},
    {"title": "Firuze", "artist": "Sezen Aksu", "genres": ["turkish pop", "classic turkish"], "moods": ["dramatic", "melancholy"], "energy": 0.35, "valence": 0.22, "danceability": 0.36, "popularity": 69},
    {"title": "Kara Toprak", "artist": "Asik Veysel", "genres": ["turkish folk", "anatolian"], "moods": ["earthy", "deep"], "energy": 0.26, "valence": 0.32, "danceability": 0.30, "popularity": 60},
    {"title": "Nem Kaldi", "artist": "Erkin Koray", "genres": ["anatolian rock", "psychedelic rock"], "moods": ["vintage", "melancholy"], "energy": 0.62, "valence": 0.44, "danceability": 0.46, "popularity": 60},
    {"title": "Estarabim", "artist": "Erkin Koray", "genres": ["anatolian rock", "psychedelic rock"], "moods": ["vintage", "groovy"], "energy": 0.76, "valence": 0.62, "danceability": 0.57, "popularity": 64},
    {"title": "Dere Geliyor Dere", "artist": "Altin Gun", "genres": ["anatolian rock", "psychedelic"], "moods": ["groovy", "vintage"], "energy": 0.77, "valence": 0.68, "danceability": 0.70, "popularity": 56},
    {"title": "Goca Dunya", "artist": "Altin Gun", "genres": ["anatolian rock", "psychedelic"], "moods": ["groovy", "sunny"], "energy": 0.80, "valence": 0.72, "danceability": 0.74, "popularity": 59},
]

FEATURES = ("energy", "valence", "danceability")


def normalize(value):
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def spotify_search_url(track):
    return f"https://open.spotify.com/search/{quote_plus(track['title'] + ' ' + track['artist'])}"


def track_label(track):
    return f"{track['title']} {track['artist']}"


def find_seed_track(query):
    query_key = normalize(query)
    if not query_key:
        return None

    best_track = None
    best_score = 0
    for track in CATALOG:
        label = normalize(track_label(track))
        title = normalize(track["title"])
        artist = normalize(track["artist"])
        score = max(
            difflib.SequenceMatcher(None, query_key, label).ratio(),
            difflib.SequenceMatcher(None, query_key, title).ratio(),
            difflib.SequenceMatcher(None, query_key, artist).ratio() * 0.82,
        )
        if query_key in label:
            score += 0.25
        if score > best_score:
            best_track = track
            best_score = score

    return best_track if best_score >= 0.45 else None


def average_features(tracks):
    if not tracks:
        return {feature: 0.5 for feature in FEATURES}
    return {
        feature: sum(track[feature] for track in tracks) / len(tracks)
        for feature in FEATURES
    }


def overlap_score(candidate, seed_tracks):
    candidate_terms = set(candidate["genres"] + candidate["moods"])
    seed_terms = set()
    for track in seed_tracks:
        seed_terms.update(track["genres"])
        seed_terms.update(track["moods"])
    if not seed_terms:
        return 0
    return len(candidate_terms & seed_terms) / len(candidate_terms | seed_terms)


def distance_score(candidate, target_features):
    distance = math.sqrt(
        sum((candidate[feature] - target_features[feature]) ** 2 for feature in FEATURES)
    )
    return max(0, 1 - distance)


def explain_recommendation(recommendation, seed_tracks):
    shared_genres = []
    shared_moods = []
    for track in seed_tracks:
        shared_genres.extend(set(recommendation["genres"]) & set(track["genres"]))
        shared_moods.extend(set(recommendation["moods"]) & set(track["moods"]))

    genre_text = ", ".join(sorted(set(shared_genres))[:2])
    mood_text = ", ".join(sorted(set(shared_moods))[:2])
    if genre_text and mood_text:
        return f"It keeps the {genre_text} side and the {mood_text} feeling from your inputs."
    if genre_text:
        return f"It sits close to your inputs through the shared {genre_text} sound."
    if mood_text:
        return f"It keeps the {mood_text} mood while moving the sound somewhere fresh."
    return "It is the closest match to the average energy, emotion, and danceability of your three songs."


def recommend_from_songs(song_inputs, count=1):
    seeds = [find_seed_track(song) for song in song_inputs]
    seeds = [track for track in seeds if track]
    if not seeds:
        seeds = [CATALOG[0], CATALOG[11], CATALOG[31]]

    target = average_features(seeds)
    seed_labels = {normalize(track_label(track)) for track in seeds}
    scored = []
    for candidate in CATALOG:
        if normalize(track_label(candidate)) in seed_labels:
            continue
        score = (
            distance_score(candidate, target) * 0.58
            + overlap_score(candidate, seeds) * 0.34
            + (candidate["popularity"] / 100) * 0.08
        )
        scored.append((score, candidate))

    scored.sort(key=lambda item: item[0], reverse=True)
    recommendations = []
    for score, track in scored[:count]:
        recommendations.append({
            **track,
            "match_score": round(score * 100),
            "spotify_url": spotify_search_url(track),
            "why": explain_recommendation(track, seeds),
        })

    return {
        "recommendations": recommendations,
        "matched_inputs": [
            {"title": track["title"], "artist": track["artist"]}
            for track in seeds
        ],
        "catalog_size": len(CATALOG),
    }
