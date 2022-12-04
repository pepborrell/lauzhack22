from .data import Song, User
from .feed import Feed, Post
from .spotify import SpotifySession, UserSpotifySession


class DB:
    def __init__(self):
        self.users = {}
        self.spotify_sessions = {}  # Interaction with spotify
        self.user_spotify_auth = {}
        self.search_engine = SpotifySession()
        self.feed = Feed()

    def set_token(self, user: str):
        self.spotify_sessions[user] = UserSpotifySession(user)

    def add_user(self, user_name: str):
        if user_name not in self.users:
            self.users[user_name] = User(user_name)
        self.set_token(user_name)

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

    def add_post(self, post: Post):
        self.feed.add_post(post)

    def get_feed(self, limit: int = 20):
        return self.feed.get_feed(limit=limit)
