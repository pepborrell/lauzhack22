import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


class SpotifySession:
    def __init__(self, token=None):
        CLIENT_ID = "f3986acfb3e44ef98aeed2d7aea7337b"  # set at your developer account
        CLIENT_SECRET = "9d8effdc87184d9d89e4fc316be9fccd"  # set at your developer account

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


# class SpotifySession:
#     def __init__(self, USERNAME, token=None):
#         CLIENT_ID = 'f3986acfb3e44ef98aeed2d7aea7337b'#set at your developer account
#         CLIENT_SECRET = '9d8effdc87184d9d89e4fc316be9fccd' #set at your developer account

#         CLIENT_ID = 'f3986acfb3e44ef98aeed2d7aea7337b'#set at your developer account
#         CLIENT_SECRET = '9d8effdc87184d9d89e4fc316be9fccd' #set at your developer account
#         REDIRECT_URI = 'http://localhost:8000' #set at your developer account, usually "http://localhost:8000"
#         SCOPE = "user-library-read,user-modify-playback-state,playlist-modify-public"

#         self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
#                                    username = USERNAME,
#                                    scope = SCOPE,
#                                    client_id = CLIENT_ID,
#                                    client_secret = CLIENT_SECRET,
#                                    redirect_uri = REDIRECT_URI))

#     def search(self, song_name):
#         song_list = self.sp.search(q=song_name, type="track,artist", limit=10)
#         return {'uri': song_list['tracks']['items'][0]['uri'], 'name': song_list['tracks']['items'][0]['name'], 'url': song_list['tracks']['items'][0]['url']}

#     def add_to_queue(self, song_URI):
#         self.sp.add_to_queue(song_URI)
#         return 1

#     def like_song(self, song_URI):
#         self.sp.current_user_saved_tracks_add(song_URI)
#         return 1

#     def __get_playlists_names(self):
#         playlists = self.sp.current_user_playlists()
#         names = []
#         while playlists:
#             names += [playlist['name'] for playlist in playlists['items']]
#             if playlists['next']:
#                 playlists = self.sp.next(playlists)
#             else:
#                 playlists = None

#         return names

#     def add_song_playlist(self, song_URI):
#         new_playlist = "Social Spotify!"
#         if new_playlist not in self.__get_playlists_names():
#             user_id = self.sp.current_user()['id']
#             sp.user_playlist_create(user_id, new_playlist, description="")

#         self.sp.current_user_saved_tracks_add(song_URI)
#         return 1
