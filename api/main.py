from data.data import DB
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
db = DB()


@app.get("/")
def root():
    return {"Message": "Hello!"}


@app.post("/create_user/{user_name}")
def create_user(user_name: str):
    db.add_user(user_name)
    return 1


@app.get("/get_user/{user_name}")
def get_user(user_name: str):
    return db.get_user(user_name).get_songs()


@app.delete("/delete_song/{user_name}/{song_id}")
def delete_song(user_name, song_id):
    db.delete_song(user_name, song_id)
    return 1


"""@app.post("/login/{user_name}")
def login(user_name: str):
    db.login(user_name)
    return 1"""


@app.post("/set_token/{user_name}/{token}")
def set_token(user_name, token):
    db.set_token(user_name, token)
    return 1


@app.post("/add_song/{user}/{user_name}/{song_id}")
def add_song(user, user_name, song_id):
    db.add_song(user, user_name, song_id)
    return 1


@app.post("/add_follower/{user_following}/{user_followed}")
def add_follower(user_following, user_followed):
    db.add_follower(user_following, user_followed)
    return 1


@app.get("/dummy.json")
def dummy():
    return {"400": 400}


@app.post("/like_song/{user}/{song_uri}")
def like_song(user, song_uri):
    db.like_song(user, song_uri)
    return 1


@app.get("/liked_songs/{user}")
def get_liked_songs(user):
    liked_songs = db.get_liked_songs(user)
    return [{"title": song.name, "url": song.url, "uri": song.uri} for song in liked_songs]
