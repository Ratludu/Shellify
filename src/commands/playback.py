import click
from src.auth import get_spotify_client
import time


@click.group()
def playback():
    pass

@playback.command()
def resume():
    sp = get_spotify_client()
    try:
        sp.start_playback()
        click.echo("Playback resumed")
    except Exception as e:
        click.echo(f"Error: {e}")

@playback.command()
def pause():
    sp = get_spotify_client()
    try:
        sp.pause_playback()
        click.echo("Playback paused")
    except Exception as e:
        click.echo(f"Error: {e}")

@playback.command()
def next():
    sp = get_spotify_client()
    try:
        sp.next_track()
        click.echo("Next track")
        current_song = sp.current_playback()
        click.echo(f"♬ Now playing: {current_song['item']['name']} by {current_song['item']['artists'][0]['name']}")
    except Exception as e:
        click.echo(f"Error: {e}")

@playback.command()
def previous():
    sp = get_spotify_client()
    try:
        sp.previous_track()
        click.echo("Previous track")
        current_song = sp.current_playback()
        click.echo(f"♬ Rewind!: {current_song['item']['name']} by {current_song['item']['artists'][0]['name']}")
    except Exception as e:
        click.echo(f"Error: {e}")

@playback.command()
def current():
    """Show currently playing track"""
    sp = get_spotify_client()
    try:
        track = sp.current_user_playing_track()
        if track is not None and track['item'] is not None:
            name = track['item']['name']
            artists = ', '.join([artist['name'] for artist in track['item']['artists']])
            is_playing = "♬ Playing" if track['is_playing'] else "Paused"
            click.echo(f"{is_playing}: {name} - {artists}")
        else:
            click.echo("No track currently playing")
    except Exception as e:
        click.echo("❌ Error: Could not get current track")

@playback.command()
def search():
    """Search for a track"""
    sp = get_spotify_client()
    query = click.prompt("Enter search query")
    results = sp.search(q=query, limit=5)
    for idx, track in enumerate(results['tracks']['items'], 1):
        artists = ', '.join([artist['name'] for artist in track['artists']])
        click.echo(f"{idx}. {track['name']} - {artists} (ID: {track['id']})")
    play = click.prompt("Enter track number to play", type=int)
    track_id = results['tracks']['items'][play - 1]['id']
    sp.start_playback(uris=[f"spotify:track:{track_id}"])
    time.sleep(1)
    track = sp.current_user_playing_track()
    if track is not None and track['item'] is not None:
        name = track['item']['name']
        artists = ', '.join([artist['name'] for artist in track['item']['artists']])
        is_playing = "♬ Playing" if track['is_playing'] else "Paused"
        click.echo(f"{is_playing}: {name} - {artists}")

@playback.command()
@click.option('--track-id', prompt='Enter track ID', help='Track ID')
def play(track_id):
    """Play a track"""
    sp = get_spotify_client()
    try:
        sp.start_playback(uris=[f"spotify:track:{track_id}"])
        time.sleep(1)
        track = sp.current_user_playing_track()
        if track is not None and track['item'] is not None:
            name = track['item']['name']
            artists = ', '.join([artist['name'] for artist in track['item']['artists']])
            is_playing = "♬ Playing" if track['is_playing'] else "Paused"
            click.echo(f"{is_playing}: {name} - {artists}")
    except Exception as e:
        click.echo(f"Error: {e}")


@playback.command()
def queue():
    """Show current queue"""
    sp = get_spotify_client()
    try:
        results = sp.queue()
        if results is not None and results['queue'] is not None:
            for idx, track in enumerate(results['queue'], 1):
                click.echo(f"{idx}. {track['name']} - {track['artists'][0]['name']} (ID: {track['id']})")
    except Exception as e:
        click.echo(f"Error: {e}")
