'use strict'; 
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
