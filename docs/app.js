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
console.log("-----Trying to fetch data-------");
var userName = localStorage.getItem("username"); 
console.log(userName); 
var apiUrl = 'https://lh22.up.railway.app/'
var getUser = apiUrl + 'get_user/' + userName; 
var createUser = apiUrl + 'create_user/' + userName;


fetch(createUser,{
    method: 'POST'
});
var json2 = fetch(getUser)
.then((response) => response.json())
.then(a => { 
    var jsObject = JSON.parse(JSON.stringify(a)); 
    generateUserList(jsObject); 
 });
//console.log(json2);

//.then(a => {    JSON.parse(a);});
//console.log(json2);
//console.log(JSON.parse(json2))//.PromiseResult);
//.then(data => {return data;});
console.log("----Data supposedly fetched-----"); 

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
    box.innerText="Sent to you by " + songData['recommender'];
    box.appendChild(getSpotifyInstance(songData["embed_url"]));
    document.getElementById('friends_music').appendChild(box);
}

function generateUserList(data) {
    for (const song in data) {
        createSongDiv(data[song]);
    }
}

const adder = document.querySelector('.btn');
adder.addEventListener('click', function() {
    console.log("button clicked"); 
    var songId = encodeURI(document.getElementById('song_name').value);
    var userFriend = document.getElementById('send_to_friend').value; 
    var addSong = apiUrl + 'add_song/' + userName + '/' + userFriend + '/' + songId;
    console.log(addSong);
    fetch(addSong,{
        method: 'POST'
    }).then(a => { window.location.reload(true);});
});

const usernameMessage = document.createElement("div");
usernameMessage.id = "myUsername"; 
usernameMessage.innerText=localStorage.getItem("username");
document.getElementById("usernameMessage").appendChild(usernameMessage); 