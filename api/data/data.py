from .spotify import SpotifySession, UserSpotifySession


class Song:
    def __init__(self, uri: str, name: str, url: str, embed_url: str = None, recommender: str = None):
        self.uri = uri
        self.title = name
        self.url = url
        self.embed_url = embed_url
        if self.embed_url is None:
            track_id = self.uri.split(":")[-1]
            self.embed_url = "https://open.spotify.com/embed/track/" + track_id
        self.recommender = recommender


class User:
    def __init__(self, name: str = ""):
        self.name = name
        self.songs = []
        self.following = set()
        self.liked_songs = []

    def get_name(self):
        return self.name

    def get_songs(self):
        return self.songs

    def add_followed(self, friend: str):
        self.following.add(friend)

    def add_song(self, song: Song):
        self.songs.append(song)

    def delete_song(self, song_uri: str):
        for song in self.songs:
            if song_uri == song.uri:
                self.songs.erase(song)

    def like_song(self, song: Song):
        self.liked_songs.append(song)

    def get_liked_songs(self):
        return self.liked_songs


class DB:
    def __init__(self):
        self.users = {}
        self.spotify_sessions = {}  # Interaction with spotify
        self.user_spotify_auth = {}
        self.search_engine = SpotifySession()

    def set_token(self, user: str, token: str):
        self.spotify_sessions[user] = UserSpotifySession(user)

    def add_user(self, user_name: str):
        if user_name not in self.users:
            self.users[user_name] = User(user_name)
        # self.set_token(user_name)

    def get_user(self, user_name: str):
        return self.users[user_name]

    def delete_song(self, user_name: str, song_uri: str):
        user: User = self.get_user(user_name)
        user.delete_song(song_uri)

    def delete_all(self, user_name: str):
        self.users[user_name].songs = []

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
        song = Song(song_dict["uri"], song_dict["name"], song_dict["url"], recommender=user1)
        self.users[user2].songs.append(song)

    def add_follower(self, u_following: str, u_followed: str):
        self.users[u_following].add_followed(u_followed)

    def like_song(self, user: str, song_uri: str):
        self.spotify_sessions[user].like_song(song_uri)

    def queue_song(self, user: str, song_uri: str):
        self.spotify_sessions[user].add_to_queue(song_uri)

    def queue_all(self, user: str):
        for song in self.users[user].songs:
            self.queue_song(user, song.uri)