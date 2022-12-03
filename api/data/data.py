from .spotify import SpotifySession


class Song:
    def __init__(self, uri: str, name: str, url: str):
        self.uri = uri
        self.name = name
        self.url = url


class User:
    def __init__(self, name: str = ""):
        self.name = name
        self.songs = []
        self.following = set()
        self.liked_songs = set()

    def get_name(self):
        return self.name

    def get_songs(self):
        return self.songs

    def add_followed(self, friend: str):
        self.following.add(friend)

    def add_song(self, song: Song):
        self.songs.append(song)

    def delete_song(self, song: Song):
        self.songs.remove(song)

    def like_song(self, song: Song):
        self.liked_songs.add(song)


class DB:
    def __init__(self):
        self.users = {}
        self.songs = {}
        self.spotify_sessions = {}  # Interaction with spotify
        self.user_spotify_auth = {}
        self.search_engine = SpotifySession()

    def set_token(self, user: str, token: str):
        self.user_spotify_auth[user] = token
        self.spotify_sessions[user] = SpotifySession(token)

    def add_user(self, user_name: str):
        self.users[user_name] = User(user_name)

    def get_user(self, user_name: str):
        return self.users[user_name]

    def delete_song(self, user_name: str, song_id: str):
        user = self.get_user(user_name)
        song = self.get_song(song_id)
        user.delete_song(song)
        self.users[user_name] = user

    """    
        def login(self, user_name: str):
        spotify_token = self.user_spotify_auth[user_name]
        self.spotify_sessions[user_name] = SpotifySession(spotify_token)
    """

    def add_song(self, user1: str, user2: str, song_name: str):
        song_name = song_name.lower()
        song_dict = self.search_engine.search(song_name)
        # if user1 not in self.spotify_sessions:
        #     uid = self.search_engine.search(song_name)
        # else:
        #     uid = self.spotify_sessions[user1].search(song_name)
        song = Song(song_dict["uri"], song_dict["name"], song_dict["url"])
        self.users[user2].songs.append(song)

    def add_follower(self, u_following: str, u_followed: str):
        self.users[u_following].add_followed(u_followed)

    def like_song(self, user: str, song_uri: str):
        user_songs = self.users[user].songs
        for song in user_songs:
            if song.uri == song_uri:
                self.users[user].like_song(song)
                return
