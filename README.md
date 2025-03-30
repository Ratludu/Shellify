# Shellify 🎵

A sleek command-line interface for controlling Spotify from your terminal.

> ⚠️ **Note**: This project is currently under development and not ready for production use.

## Features (Planned/Completed)

### Playback Controls 🎧
- Resume/pause playback
- Navigate between tracks (next/previous)
- View currently playing track
- Search Spotify's library
- View and manage queue
- Play specific tracks by ID

### Playlist Management 📋
- View your Spotify playlists
- (More features coming soon)

## Prerequisites

- Python 3.6+
- Spotify Premium Account
- Spotify Developer Account & Application

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/shellify.git
cd shellify
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your `.env` file:
```
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=your_redirect_uri
```

## Usage

> ⚠️ Currently under development. The following commands are planned/in progress:

```bash
# Playback Controls
shellify playback current    # Display now playing
shellify playback play      # Play a track by ID
shellify playback pause     # Pause playback
shellify playback resume    # Resume playback
shellify playback next      # Skip forward
shellify playback previous  # Skip backward
shellify playback search    # Search for tracks
shellify playback queue     # View queue

# Playlist Management
shellify playlist playlists # List your playlists
```

## Technical Stack

- [Click](https://click.palletsprojects.com/) - Python CLI framework
- [Spotipy](https://spotipy.readthedocs.io/) - Spotify Web API wrapper
- Python 3.6+

## Development Status

This project is actively being developed. Here's what's coming:
- [ ] Additional playlist management features
- [ ] Device selection and management
- [ ] Volume controls
- [ ] Shuffle and repeat modes
- [ ] Rich terminal UI improvements
- [ ] Configuration management
- [ ] Error handling improvements

## Contributing

While this project is still in development, we're not accepting contributions yet. Stay tuned for updates!

## License

[MIT License](LICENSE)

## Disclaimer

Shellify is an unofficial project and is not affiliated with, sponsored, or endorsed by Spotify. This is an independent tool created for educational purposes and personal use.

Made with ♥️ by [Ratludu]
