import spotipy 
from dotenv import dotenv_values
import openai
import json
import argparse

# Load configuration from .env
config = dotenv_values(".env")
openai.api_key = config["OPEN_AI_KEY"]


parser = argparse.ArgumentParser(description="Simple Command Line Song Utility")
parser.add_argument("-p", type=str, help="The promt to describe the playlist")
parser.add_argument("-n", type=int,default=10, help="The number of songs to add to the playlist")
args = parser.parse_args()


def get_playlist(prompt, count=8):
    example_json = """
    [
        {"song": "Someone Like You", "artist": "Adele"},
        {"song": "The Night We Met", "artist": "Lord Huron"},
        {"song": "Skinny Love", "artist": "Bon Iver"},
        {"song": "Hurt", "artist": "Johnny Cash"},
        {"song": "All I Want", "artist": "Kodaline"}
    ]
    """
    
    messages = [
        {"role": "system", "content": """You are a helpful playlist generating assistant. You should generate a list of songs and their artists according to a text prompt. You should return a json array, where each element follows this format: {"song": <song_title>, "artist": <artist_name>}"""}, 
        {"role": "user", "content": f"Generate a playlist of {count} songs based on this prompt: {prompt}"}
    ]
    
    # Use openai.ChatCompletion.create instead of openai.Completion.create
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the chat model
        messages=messages,       # Pass the messages as the input
        max_tokens=400
    )
    
    print(response)  # Debugging step to check the full response
    playlist = json.loads(response["choices"][0]["message"]["content"])
    return playlist

# Example usage
playlist = get_playlist(args.p, args.n)
print(playlist)

# Spotipy setup for Spotify integration
sp = spotipy.Spotify(
    auth_manager=spotipy.SpotifyOAuth(
        client_id=config["SPOTIFY_CLIENT_ID"],
        client_secret=config["SPOTIFY_CLIENT_SECRET"],
        redirect_uri="http://127.0.0.1:9999",
        scope="playlist-modify-private"
    )
)

current_user = sp.current_user()
track_ids = []
assert current_user is not None

for item in playlist:
    artist, song = item["artist"], item["song"]
    query = f"{song} {artist}" 
    search_results = sp.search(q=query, type="track", limit=10)
    track_ids.append(search_results["tracks"]["items"][0]["id"])

created_playlist = sp.user_playlist_create(
    current_user["id"], 
    public=False,
    name=args.p
)

sp.user_playlist_add_tracks(current_user["id"], created_playlist["id"], track_ids)
