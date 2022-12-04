from typing import List

from pydantic import BaseModel
from .spotify import SpotifySession

from .data import Song


class PostBody(BaseModel):
    username: str
    text: str
    song: str


class Post:
    def __init__(self, username: str, text: str, song: str) -> None:
        self.username = username
        self.text = text
        song_dict = SpotifySession().search(song)
        self.song = Song(song_dict["uri"], song_dict["name"], song_dict["url"], recommender=self.username)


class Feed:
    def __init__(self) -> None:
        self.posts = []

    def add_post(self, post: Post) -> None:
        self.posts.append(post)

    def get_feed(self, limit=20) -> List[Post]:
        n = len(self.posts)
        return self.posts[max(-n, -limit) :][::-1]
