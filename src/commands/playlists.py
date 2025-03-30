from src.auth import get_spotify_client
import click

@click.group()
def playlist():
    pass

@playlist.command()
@click.option('--limit', default=5, help='Number of playlists to display')
def playlists(limit):
    """Show user playlists"""
    sp = get_spotify_client()
    results = sp.current_user_playlists(limit=limit)

    for idx, item in enumerate(results['items'], 1):
        click.echo(f"{idx}. {item['name']} (ID: {item['id']})")
