import click
import spotipy
from src.auth import get_spotify_client
from src.commands.playlists import playlists
from src.commands.playback import playback

@click.group()
def cli():
    pass

cli.add_command(playlists)
cli.add_command(playback)

if __name__ == "__main__":
    cli()
