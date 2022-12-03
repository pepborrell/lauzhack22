from fastapi import FastAPI
from data.data import DB


app = FastAPI()
db = DB()


@app.post("/users/{user_name}")
def create_user(user_name: str):
    db.add_user(user_name)
    return 1


@app.get("/users/{user_name}")
def get_user(user_name: str):
    return {"user_name": user_name, "songs": db.get_user(user_name).get_songs()}


@app.delete("/users/{user_name}/{song_id}")
def delete_song(user_name, song_id):
    db.delete_song(user_name, song_id)
    return 1


'''@app.post("/login/{user_name}")
def login(user_name: str):
    db.login(user_name)
    return 1'''

@app.post("/users/{user_name}/{token}")
def set_token(user_name, token):
    db.set_token(user_name, token)
    return 1

@app.post("/songs/{user}/{user_name}/{song_id}")
def add_song(user, user_name, song_id):
    db.add_song(user, user_name, song_id)
    return 1
