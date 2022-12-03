from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Song:
    def __init__(self, name: str=''):
        self.name = name.lower()


class User:
    def __init__(self, name: str =''):
        self.name = name
        self.songs = []
        self.friends = set() # Users
    
    def get_name(self):
        return self.name

    def get_songs(self):
        return self.songs

    def add_friend(self, friend):
        self.friends.add(friend)
    
    def add_song(self, song: Song):
        self.songs.append(song)

class DB:
    def __init__(self):
        self.users = {}
    
    def add_user(self, user_name):
        self.users[user_name] = User(user_name)
    
    def get_user(self, user_name):
        return self.users[user_name]
    
app = FastAPI()
db = DB()
@app.post("/users/{user_name}")
def create_user(user_name: str):
    db.add_user(user_name)
    return user_name

@app.get('/users/{user_name}')
def get_user(user_name: str):
    return {'user_name': user_name, 'songs': db.get_user(user_name).get_songs()}
