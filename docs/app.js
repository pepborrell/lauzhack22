'use strict'; 

var userName = localStorage.getItem("username"); 
var apiUrl = 'https://lh22.up.railway.app/'
var getUser = apiUrl + 'get_user/' + userName; 
var createUser = apiUrl + 'create_user/' + userName;

// Top box
var top_buttons = document.createElement("div")
top_buttons.className = "top_buttons";

const button_queue_all = document.createElement("img");
button_queue_all.src = "icons/queue.png"
button_queue_all.style.width = "30%"
button_queue_all.style.height = "30%"
button_queue_all.addEventListener('click', function () {
        fetch(apiUrl+"queue_all/"+userName+"/", {
            method: 'POST'
        });
});

const button_delete_all = document.createElement("img");
button_delete_all.src = "icons/cross.png"
button_delete_all.style.width = "30%"
button_delete_all.style.height = "30%"
button_delete_all.addEventListener('click', function () {
        fetch(apiUrl+"delete_all/"+userName+"/", {
            method: 'POST'
        });
});

top_buttons.appendChild(button_queue_all);
top_buttons.appendChild(button_delete_all);
document.getElementById("title").appendChild(top_buttons);

fetch(createUser,{
    method: 'POST'
});
var json2 = fetch(getUser)
.then((response) => response.json())
.then(a => { 
    var jsObject = JSON.parse(JSON.stringify(a)); 
    generateUserList(jsObject); 
 });

function getSpotifyInstance(songUrl) {
    const audioBox = document.createElement("iframe");
    audioBox.id = "audio";
    audioBox.style="border-radius:12px";
    audioBox.src = songUrl;
    audioBox.width="100%";
    audioBox.height="100px";
    audioBox.frameBorder = "0";
    audioBox.allowfullscreen ="";
    audioBox.allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture";
    audioBox.loading = "lazy"; 
    return audioBox
};

var i = 0;
function createSongDiv(songData) {
    const box = document.createElement("div");
    box.className = "song_box";
    box.id = "song";
    box.innerText="Sent to you by " + songData['recommender'];
    box.appendChild(getSpotifyInstance(songData["embed_url"]));
    document.getElementById('friends_music').appendChild(box);

    // Buttons
    var buttons = document.createElement("div")
    buttons.className = "buttons";

    const button_like = document.createElement("img");
    button_like.style.width = "30%"
    button_like.style.height = "30%"
    button_like.src="icons/heart.png"
    button_like.addEventListener('click', function () {
            var songUri = songData["uri"];
            fetch(apiUrl+"like_song/"+userName+"/"+songUri+"/", {
                method: 'POST'
            });
    });
    buttons.appendChild(button_like);

    const button_queue = document.createElement("img");
    button_queue.src = "icons/queue.png"
    button_queue.style.width = "30%"
    button_queue.style.height = "30%"
    button_queue.addEventListener('click', function () {
            var songUri = songData["uri"];
            fetch(apiUrl+"queue_song/"+userName+"/"+songUri+"/", {
                method: 'POST'
            });
    });
    buttons.appendChild(button_queue);

    const button_remove = document.createElement("img");
    button_remove.src="icons/cross.png"
    button_remove.style.width = "30%"
    button_remove.style.height = "30%"
    button_remove.addEventListener('click', function () {
            var songUri = songData["uri"];
            fetch(apiUrl+"delete_song/"+userName+"/"+songUri+"/", {
                method: 'POST'
            })/*.then(a => { window.location.reload(true);});*/
    });
    buttons.appendChild(button_remove);

    document.getElementById('friends_music').appendChild(buttons)
    
}

function generateUserList(data) {
    for (const song in data) {
        createSongDiv(data[song]);
    }
}

const adder = document.querySelector('.btn');

adder.addEventListener('click', function() {
    var songId = encodeURI(document.getElementById('song_name').value);
    var userFriend = document.getElementById('send_to_friend').value; 
    var addSong = apiUrl + 'add_song/' + userName + '/' + userFriend + '/' + songId;
    fetch(addSong,{
        method: 'POST'
    }).then(a => { window.location.reload(true);});
});

const usernameMessage = document.createElement("div");
usernameMessage.id = "myUsername"; 
usernameMessage.innerText=localStorage.getItem("username");
document.getElementById("usernameMessage").appendChild(usernameMessage); 