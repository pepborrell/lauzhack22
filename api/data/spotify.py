import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifySession:
    def __init__(self, token=None):
        CLIENT_ID = 'f3986acfb3e44ef98aeed2d7aea7337b'#set at your developer account
        CLIENT_SECRET = '9d8effdc87184d9d89e4fc316be9fccd' #set at your developer account
        auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        self.sp = spotipy.Spotify(auth_manager=auth_manager)

    def search(self, song_name):
        song_list = self.sp.search(q=song_name, type="track", limit=10)
        return {'uri': song_list['tracks']['items'][0]['uri'], 'name': song_list['tracks']['items'][0]['name']}

    def add_to_queue(self, song_URI):
        self.sp.add_to_queue(song_URI)
        return 1

    def like_song(self, song_URI):
        self.sp.current_user_saved_tracks_add(song_URI)
        return 1
