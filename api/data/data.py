from .spotify import SpotifySession
import pandas as pd


class Song:
    def __init__(self, name: str = ""):
        self.name = name.lower()
        # self.id


class User:
    def __init__(self, name: str = ""):
        self.name = name
        self.songs = []
        self.friends = set()

    def get_name(self):
        return self.name

    def get_songs(self):
        return self.songs

    def add_friend(self, friend):
        self.friends.add(friend)

    def add_song(self, song: Song):
        self.songs.append(song)

    def delete_song(self, song: Song):
        self.songs.remove(song)


class DB:
    def __init__(self):
        self.users = {}
        self.songs = {}
        self.spotify_sessions = {}  # Interaction with spotify
        self.user_spotify_auth = self.read_spotify_auth()

    def read_spotify_auth(csv_name: str = "spotify_auth.csv"):
        # df = pd.read_csv(csv_name, sep=";") # TODO: fix this
        # return df.to_dict()
        return {}

    def add_user(self, user_name):
        self.users[user_name] = User(user_name)

    def get_user(self, user_name):
        return self.users[user_name]

    def delete_song(self, user_name, song_id):
        user = self.get_user(user_name)
        song = self.get_song(song_id)
        user.delete_song(song)
        self.users[user_name] = user

    def login(self, user_name: str):
        spotify_token = self.user_spotify_auth[user_name]
        self.spotify_sessions[user_name] = SpotifySession(spotify_token)
