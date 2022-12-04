import json
import os

import spotipy
from spotipy.cache_handler import CacheHandler
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


class DummyCacheHandler(CacheHandler):
    def __init__(self, username: str) -> None:
        if "spotipy_cache_" + username not in os.environ:
            raise NameError()
        json_str = os.environ["spotipy_cache_" + username]
        json_str = json_str.replace("'", '"')
        self.pass_dict = json.loads(json_str)

    def get_cached_token(self):
        return self.pass_dict

    def save_token_to_cache(self, token_info):
        return NotImplementedError()


class SpotifySession:
    def __init__(self, token=None):
        CLIENT_ID = "f3986acfb3e44ef98aeed2d7aea7337b"  # set at your developer account
        CLIENT_SECRET = os.environ["CLIENT_SECRET"]  # set at your developer account

        self.sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        )

    def search(self, song_name):
        song_list = self.sp.search(q=song_name, limit=1, type="track,artist")
        print(song_list)
        return {
            "uri": song_list["tracks"]["items"][0]["uri"],
            "name": song_list["tracks"]["items"][0]["name"],
            "url": song_list["tracks"]["items"][0]["external_urls"]["spotify"],
        }


class UserSpotifySession:
    def __init__(self, USERNAME, token=None):
        CLIENT_ID = "f3986acfb3e44ef98aeed2d7aea7337b"  # set at your developer account
        CLIENT_SECRET = os.environ["CLIENT_SECRET"]  # set at your developer account

        REDIRECT_URI = "http://localhost:8000"  # set at your developer account, usually "http://localhost:8000"
        SCOPE = "user-library-read,user-modify-playback-state,playlist-modify-public,user-library-modify"

        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                username=USERNAME,
                scope=SCOPE,
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                redirect_uri=REDIRECT_URI,
                cache_path=DummyCacheHandler(USERNAME),
            )
        )

    def search(self, song_name):
        song_list = self.sp.search(q=song_name, limit=1, type="track,artist")
        return {
            "uri": song_list["tracks"]["items"][0]["uri"],
            "name": song_list["tracks"]["items"][0]["name"],
            "url": song_list["tracks"]["items"][0]["external_urls"]["spotify"],
        }

    def add_to_queue(self, song_URI):
        self.sp.add_to_queue(song_URI)
        return 1

    def like_song(self, song_URI):
        self.sp.current_user_saved_tracks_add([song_URI])
        return 1

    def __find_playlist_id(self, playlist_name):
        playlists = self.sp.current_user_playlists()
        names = []
        while playlists:
            for playlist in playlists["items"]:
                if playlist["name"] == playlist_name:
                    return playlist["id"]
            if playlists["next"]:
                playlists = self.sp.next(playlists)
            else:
                playlists = None

        return None

    def add_song_playlist(self, song_URI):
        new_playlist = "Social Spotify!"
        playlist_id = self.__find_playlist_id(new_playlist)
        user_id = self.sp.current_user()["id"]
        if not playlist_id:
            self.sp.user_playlist_create(
                user_id,
                new_playlist,
                description="Playlist created by Social Spotify where the music you liked gets saved!",
            )
            playlist_id = self.__find_playlist_id(new_playlist)

        self.sp.user_playlist_add_tracks(user_id, playlist_id, [song_URI])
        return 1
