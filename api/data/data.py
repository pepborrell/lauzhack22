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
                self.songs.delate(song)

    def like_song(self, song: Song):
        self.liked_songs.append(song)

    def get_liked_songs(self):
        return self.liked_songs
