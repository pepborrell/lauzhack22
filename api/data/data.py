from .spotify import SpotifySession
import pandas as pd


class Song:
    def __init__(self, uid):
        self.uid = uid


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
        self.user_spotify_auth = {}
        self.search_engine = SpotifySession()

    def set_token(self, user, token):
        self.user_spotify_auth[user] = token
        self.spotify_sessions[user] = SpotifySession(token)

    def add_user(self, user_name):
        self.users[user_name] = User(user_name)

    def get_user(self, user_name):
        return self.users[user_name]

    def delete_song(self, user_name, song_id):
        user = self.get_user(user_name)
        song = self.get_song(song_id)
        user.delete_song(song)
        self.users[user_name] = user

    '''    
        def login(self, user_name: str):
        spotify_token = self.user_spotify_auth[user_name]
        self.spotify_sessions[user_name] = SpotifySession(spotify_token)
    '''
    
    def add_song(self, user1, user2, song_name):
        song_name = song_name.lower()
        if user1 not in self.spotify_sessions:
            uid = self.search_engine.search(song_name)
        else:
            uid = self.spotify_sessions[user1].search(song_name)
        song = Song(uid)
        self.user2[user2].songs.append(song)
