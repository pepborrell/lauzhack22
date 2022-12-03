import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifySession:
    def __init__(self, token, secret_token):
        auth_manager = SpotifyClientCredentials(token, secret_token)#'f3986acfb3e44ef98aeed2d7aea7337b', '9d8effdc87184d9d89e4fc316be9fccd')
        self.sp = spotipy.Spotify(auth_manager=auth_manager)
    
    def search(self, song_name):
        song_list = self.sp.search(q=song_name, type="track", limit=10)
        return songf_list[-1]
    
    def add_to_queue(self, song_URI):
        self.sp.add_to_queue(song_URI)
        return 1
    
    def like_song(self, song_URI):
        self.sp.current_user_saved_tracks_add(song_URI)
        return 1
