# recognition/utils.py
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.conf import settings

def get_spotify_client():
    client_credentials_manager = SpotifyClientCredentials(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp

def search_spotify_song(song_clip):
    """Search for a song in Spotify based on a given clip or metadata."""
    sp = get_spotify_client()
    
    # Search Spotify using song title or audio clip (filename, etc.)
    result = sp.search(q=song_clip, limit=1, type='track')

    if result['tracks']['items']:
        song = result['tracks']['items'][0]
        return {
            'name': song['name'],
            'artist': song['artists'][0]['name'],
            'album': song['album']['name'],
            'url': song['external_urls']['spotify'],
            'album_cover': song['album']['images'][0]['url']  # Album cover URL
        }
    else:
        return None
