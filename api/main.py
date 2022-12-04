from data.db import DB
from data.feed import Post, PostBody
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


@app.get("/get_user/{user_name}")
def get_user(user_name: str):
    return db.get_user(user_name).get_songs()


@app.delete("/delete_song/{user_name}/{song_uri}")
def delete_song(user_name, song_uri):
    db.delete_song(user_name, song_uri)


@app.delete("/delete_all/{user_name}")
def delete_all(user_name):
    db.delete_all(user_name)


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


@app.post("/queue_song/{user}/{song_uri}")
def queue_song(user, song_uri):
    db.queue_song(user, song_uri)
    return 1


@app.post("/queue_all/{user}")
def queue_all(user):
    db.queue_all(user)
    return 1


@app.post("/like_song/{user}/{song_uri}")
def like_song(user, song_uri):
    db.like_song(user, song_uri)
    return 1


@app.get("/liked_songs/{user}")
def get_liked_songs(user):
    db.get_user(user).get_liked_songs()


@app.post("/add_post/{username}/{text}/{song}")
def add_post(username: str, text: str, song: str):
    db.add_post(Post(username=username, text=text, song=song))


@app.get("/get_feed/")
def get_feed():
    return db.get_feed()
