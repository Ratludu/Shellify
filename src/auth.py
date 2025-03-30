import click
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def get_spotify_client():
    """Initialize Spotify client"""
    auth_manager = SpotifyOAuth(
        scope="user-library-read playlist-read-private user-modify-playback-state user-read-playback-state"
    )
    return spotipy.Spotify(auth_manager=auth_manager)
