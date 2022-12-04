from typing import List

from .data import Song, User


class Post:
    def __init__(self, user: User, text: str, song: Song) -> None:
        self.user = user
        self.text = text
        self.song = song


class Feed:
    def __init__(self) -> None:
        self.posts = []

    def add_post(self, post: Post) -> None:
        self.posts.append(post)

    def get_feed(self, limit=20) -> List[Post]:
        n = len(self.posts)
        return self.posts[max(-n, -limit) :][::-1]
