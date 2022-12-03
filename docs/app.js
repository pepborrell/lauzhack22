'use strict'; 
document.getElementById('login').style.display='none'
/*
const switcher = document.querySelector('.btn');
const className = document.body.className; 
console.log('current class name: ' + className); 
if (className == "light-theme2") {
    switcher.textContent = "Dark";
} else {
    switcher.textContent = "Light"; 
}
switcher.addEventListener('click', function() {
    document.body.classList.toggle('light-theme2');
    document.body.classList.toggle('dark-theme');

    const className = document.body.className;
    if (className == "light-theme2") {
        this.textContent = "Dark"; 
    } else {
        this.textContent = "Light";
    }

    console.log("current class name: " + className)
});
*/
/* Storing multi-line JSON string in a JS variable
using the new ES6 template literals */
var json = `{
    "song1": {
        "title": "Thriller",
        "url": "https://open.spotify.com/embed/track/2LlQb7Uoj1kKyGhlkBf9aC?"
    },
    "song2": {
        "title": "Thriller",
        "url": "https://open.spotify.com/embed/track/2LlQb7Uoj1kKyGhlkBf9aC?"
    },
    "song3": {
        "title": "Thriller",
        "url": "https://open.spotify.com/embed/track/2LlQb7Uoj1kKyGhlkBf9aC?"
    },
    "song4": {
        "title": "Thriller",
        "url": "https://open.spotify.com/embed/track/2LlQb7Uoj1kKyGhlkBf9aC?"
    }
}`;
/*
var username = localStorage.getItem("username"); 
var apiLink = "https://lauzhack22-production.up.railway.app/users/" + username;
var json2 = fetch("https://lauzhack22-production.up.railway.app/users/guifresa",{mode: 'no-cors'}).then((response) => response.json());
console.log(JSON.stringify(json2));
*/
var json2 = fetch('https://lauzhack22-production.up.railway.app/users/guifresa', {
    mode: 'no-cors',
    method: 'GET',
    headers: {
        'Accept': 'application/json',
    },
})
.then(response => response.text())
.then(text => console.log(text))

console.log(JSON.stringify(json2));

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
}

var mydata = JSON.parse(json);
var i = 0;
function createSongDiv(songData) {
const box = document.createElement("div");
box.id = "song";
box.innerText=songData["title"]
box.appendChild(getSpotifyInstance(songData["url"]));
document.getElementById('friends_music').appendChild(box);
}

for (const song in mydata) {
createSongDiv(mydata[song]);
}

const usernameMessage = document.createElement("div");
usernameMessage.id = "myUsername"; 
usernameMessage.innerText=localStorage.getItem("username");
document.getElementById("usernameMessage").appendChild(usernameMessage); 
