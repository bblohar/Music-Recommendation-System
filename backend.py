# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import uuid

app = Flask(__name__)
CORS(app) # Enable CORS for frontend to communicate

# --- Simulated Database (In-memory) ---
# In a real application, this would connect to a DBMS.

# Songs: List of dictionaries
SONGS = [
    {"id": "s001", "title": "Blinding Lights", "artist": "The Weeknd", "genre": "Pop", "mood": "Upbeat, Energetic"},
    {"id": "s002", "title": "Shape of You", "artist": "Ed Sheeran", "genre": "Pop", "mood": "Catchy, Feel-good"},
    {"id": "s003", "title": "Bohemian Rhapsody", "artist": "Queen", "genre": "Rock", "mood": "Epic, Classic"},
    {"id": "s004", "title": "Hotel California", "artist": "Eagles", "genre": "Rock", "mood": "Relaxing, Nostalgic"},
    {"id": "s005", "title": "Someone Like You", "artist": "Adele", "genre": "Soul", "mood": "Emotional, Ballad"},
    {"id": "s006", "title": "Rolling in the Deep", "artist": "Adele", "genre": "Soul", "mood": "Powerful, Intense"},
    {"id": "s007", "title": "Billie Jean", "artist": "Michael Jackson", "genre": "Pop", "mood": "Dance, Iconic"},
    {"id": "s008", "title": "Thriller", "artist": "Michael Jackson", "genre": "Pop", "mood": "Spooky, Fun"},
    {"id": "s009", "title": "Lose Yourself", "artist": "Eminem", "genre": "Hip Hop", "mood": "Motivational, Intense"},
    {"id": "s010", "title": "Humble.", "artist": "Kendrick Lamar", "genre": "Hip Hop", "mood": "Confident, Bold"},
    {"id": "s011", "title": "Imagine", "artist": "John Lennon", "genre": "Classic", "mood": "Peaceful, Reflective"},
    {"id": "s012", "title": "What a Wonderful World", "artist": "Louis Armstrong", "genre": "Jazz", "mood": "Calm, Uplifting"},
    {"id": "s013", "title": "Fly Me to the Moon", "artist": "Frank Sinatra", "genre": "Jazz", "mood": "Romantic, Smooth"},
    {"id": "s014", "title": "Bad Guy", "artist": "Billie Eilish", "genre": "Pop", "mood": "Dark, Alternative"},
    {"id": "s015", "title": "Happier Than Ever", "artist": "Billie Eilish", "genre": "Pop", "mood": "Emotional, Reflective"},
    {"id": "s016", "title": "Stairway to Heaven", "artist": "Led Zeppelin", "genre": "Rock", "mood": "Epic, Progressive"},
    {"id": "s017", "title": "Sweet Child o' Mine", "artist": "Guns N' Roses", "genre": "Rock", "mood": "Energetic, Classic"},
    {"id": "s018", "title": "Lovely", "artist": "Billie Eilish", "genre": "Pop", "mood": "Melancholy, Beautiful"},
    {"id": "s019", "title": "Watermelon Sugar", "artist": "Harry Styles", "genre": "Pop", "mood": "Summer, Fun"},
    {"id": "s020", "title": "Adore You", "artist": "Harry Styles", "genre": "Pop", "mood": "Romantic, Upbeat"},
    # Added Hindi songs
    {"id": "s021", "title": "Kesariya", "artist": "Pritam, Arijit Singh", "genre": "Bollywood", "mood": "Romantic, Soothing"},
    {"id": "s022", "title": "Pasoori", "artist": "Ali Sethi, Shae Gill", "genre": "Indian Pop", "mood": "Fusion, Catchy"},
    {"id": "s023", "title": "Raatan Lambiyan", "artist": "Tanishk Bagchi, Jubin Nautiyal", "genre": "Bollywood", "mood": "Romantic, Dreamy"},
    {"id": "s024", "title": "Dil Bechara", "artist": "A.R. Rahman", "genre": "Bollywood", "mood": "Emotional, Melancholy"},
    {"id": "s025", "title": "Tera Fitoor", "artist": "Himesh Reshammiya, Arijit Singh", "genre": "Bollywood", "mood": "Passionate, Love"},
    {"id": "s026", "title": "Ghungroo", "artist": "Vishal-Shekhar, Arijit Singh", "genre": "Bollywood", "mood": "Upbeat, Dance"},
    {"id": "s027", "title": "Channa Mereya", "artist": "Pritam, Arijit Singh", "genre": "Bollywood", "mood": "Heartbreak, Emotional"},
    {"id": "s028", "title": "Bekhayali", "artist": "Sachet-Parampara, Sachet Tandon", "genre": "Bollywood", "mood": "Intense, Rock"},
    {"id": "s029", "title": "Duniyaa", "artist": "Akhil, Dhvani Bhanushali", "genre": "Bollywood", "mood": "Romantic, Pop"},
    {"id": "s030", "title": "Shayad", "artist": "Pritam, Arijit Singh", "genre": "Bollywood", "mood": "Love, Nostalgic"},
]

# User Data: Stores listening history and explicit likes/dislikes
# In a real system, this would be persistent and more complex.
# For simplicity, user_id is a string, and history is a list of song_ids.
# likes/dislikes could be used for more advanced recommendations.
USER_DATA = {
    "user123": {
        "history": ["s001", "s007", "s002", "s019"], # Recently listened
        "likes": ["s001", "s007"],
        "dislikes": []
    },
    "guest_user": {
        "history": [],
        "likes": [],
        "dislikes": []
    }
}

# --- Helper Functions for Recommendation Logic ---

def get_song_by_id(song_id):
    """Helper to find a song by its ID."""
    return next((song for song in SONGS if song["id"] == song_id), None)

def recommend_songs_simple(user_id, preferred_genre=None, preferred_artist=None, text_preference=None, limit=5):
    """
    Simple recommendation logic:
    1. Filter by explicit genre/artist preference.
    2. Filter by keywords in title/artist/genre/mood if text_preference is given.
    3. Exclude songs already in user's recent history/dislikes.
    4. Prioritize liked songs (if applicable, not fully implemented here).
    5. Fallback to random popular songs if not enough recommendations.
    """
    user_info = USER_DATA.get(user_id, {"history": [], "likes": [], "dislikes": []})
    
    # Songs to exclude from recommendations
    excluded_song_ids = set(user_info["history"] + user_info["dislikes"])

    potential_recommendations = []

    # Step 1: Filter by explicit genre/artist
    if preferred_genre:
        potential_recommendations.extend([s for s in SONGS if s["genre"].lower() == preferred_genre.lower() and s["id"] not in excluded_song_ids])
    if preferred_artist:
        potential_recommendations.extend([s for s in SONGS if s["artist"].lower() == preferred_artist.lower() and s["id"] not in excluded_song_ids])

    # Step 2: Filter by text preference (if provided and no strong genre/artist filter yet)
    if text_preference:
        keywords = text_preference.lower().split()
        for song in SONGS:
            if song["id"] in excluded_song_ids:
                continue
            match_score = 0
            for keyword in keywords:
                if keyword in song["title"].lower() or \
                   keyword in song["artist"].lower() or \
                   keyword in song["genre"].lower() or \
                   keyword in song["mood"].lower():
                    match_score += 1
            if match_score > 0 and song not in potential_recommendations:
                potential_recommendations.append(song)
    
    # Remove duplicates from potential recommendations
    unique_recommendations = []
    seen_ids = set()
    for song in potential_recommendations:
        if song["id"] not in seen_ids:
            unique_recommendations.append(song)
            seen_ids.add(song["id"])

    # If not enough recommendations, fill with random songs not in history/dislikes
    if len(unique_recommendations) < limit:
        remaining_songs = [s for s in SONGS if s["id"] not in excluded_song_ids and s["id"] not in seen_ids]
        random.shuffle(remaining_songs)
        unique_recommendations.extend(remaining_songs[:limit - len(unique_recommendations)])

    # Shuffle the final list to provide variety
    random.shuffle(unique_recommendations)

    return unique_recommendations[:limit]


# --- API Endpoints ---

@app.route('/songs', methods=['GET'])
def get_all_songs():
    """Returns a list of all available songs."""
    return jsonify(SONGS)

@app.route('/genres', methods=['GET'])
def get_all_genres():
    """Returns a list of all unique genres."""
    genres = sorted(list(set(song['genre'] for song in SONGS)))
    return jsonify(genres)

@app.route('/artists', methods=['GET'])
def get_all_artists():
    """Returns a list of all unique artists."""
    artists = sorted(list(set(song['artist'] for song in SONGS)))
    return jsonify(artists)


@app.route('/recommend', methods=['POST'])
def recommend_music():
    """
    Recommends songs based on user preferences.
    Requires 'user_id' and can optionally take 'preferred_genre', 'preferred_artist', 'text_preference'.
    """
    data = request.get_json()
    user_id = data.get('user_id', 'guest_user') # Default to guest user
    preferred_genre = data.get('preferred_genre')
    preferred_artist = data.get('preferred_artist')
    text_preference = data.get('text_preference')

    recommendations = recommend_songs_simple(user_id, preferred_genre, preferred_artist, text_preference)
    
    if not recommendations:
        # Fallback if no specific recommendations found
        all_songs_not_in_history = [s for s in SONGS if s["id"] not in USER_DATA.get(user_id, {}).get("history", [])]
        random.shuffle(all_songs_not_in_history)
        recommendations = all_songs_not_in_history[:5] # Return 5 random songs

    return jsonify(recommendations)

@app.route('/listen', methods=['POST'])
def record_listen():
    """
    Records that a user listened to a song.
    Requires 'user_id' and 'song_id'.
    """
    data = request.get_json()
    user_id = data.get('user_id')
    song_id = data.get('song_id')

    if not user_id or not song_id:
        return jsonify({'error': 'User ID and Song ID are required.'}), 400

    if user_id not in USER_DATA:
        USER_DATA[user_id] = {"history": [], "likes": [], "dislikes": []}

    # Add to history (limit to last 10 songs for simplicity)
    if song_id in USER_DATA[user_id]["history"]:
        USER_DATA[user_id]["history"].remove(song_id) # Move to end if already exists
    USER_DATA[user_id]["history"].append(song_id)
    USER_DATA[user_id]["history"] = USER_DATA[user_id]["history"][-10:] # Keep last 10

    return jsonify({'message': f'Listen recorded for song {song_id} by user {user_id}'}), 200

@app.route('/user_history/<string:user_id>', methods=['GET'])
def get_user_history(user_id):
    """
    Returns the listening history for a given user.
    """
    user_info = USER_DATA.get(user_id)
    if not user_info:
        return jsonify({"history": []}), 200 # Return empty if user not found
    
    history_songs = [get_song_by_id(s_id) for s_id in user_info["history"]]
    # Filter out any None if song_id doesn't exist in SONGS
    history_songs = [s for s in history_songs if s is not None]
    return jsonify(history_songs), 200

if __name__ == '__main__':
    # To run this Flask app:
    # 1. Save it as app.py
    # 2. Install Flask and Flask-CORS: pip install Flask Flask-CORS
    # 3. Run from your terminal: python app.py
    # The app will run on http://127.0.0.1:5000/
    app.run(debug=True, port=5000)
