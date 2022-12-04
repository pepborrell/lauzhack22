
var userName = localStorage.getItem("username"); 
console.log(userName); 
var apiUrl = 'https://lh22.up.railway.app/'
var getUser = apiUrl + 'get_user/' + userName; 
var createUser = apiUrl + 'create_user/' + userName;
const poster = document.querySelector('.post_btn');


document.getElementById('feed_div').innerText = ""; 
generateFeed(); 
poster.addEventListener('click', function() {
    console.log("post button clicked"); 
    var songId = encodeURI(document.getElementById('feed_song').value);
    var postText = encodeURI(document.getElementById('feed_text').value); 
    var addPost = apiUrl + "add_post/" + userName + "/" + postText + "/" + songId;
    var jsonPost = JSON.stringify({
        "username": userName,
        "text": postText,
        "song": songId
    });
    console.log(jsonPost); 
    fetch(addPost, {
        method: 'POST',
    }).then(a=> {
        document.getElementById('feed_div').innerText = ""; 
        generateFeed(); 
        window.location.reload();
    });
});

function generateFeed() {
    var getFeed = apiUrl + "get_feed/" + userName;
    fetch(getFeed).then((response) => response.json())
    .then(a => {
        console.log("trying to get the feed"); 
        var jsObject = JSON.parse(JSON.stringify(a));
        generatePostList(jsObject);
    });
}

function generatePostList(feedData) {
    for (post in feedData) {
        generatePost(feedData[post]);
    }
}


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

function createSongDiv(songData) {
    const box = document.createElement("div");
    box.id = "song";
    //box.innerText="Sent to you by " + songData['recommender'];
    box.appendChild(getSpotifyInstance(songData["embed_url"]));
    

    const icon = document.createElement("img");
    icon.src = 'icons/plus.png';
    icon.addEventListener('click', function () {
        var songUri = songData["uri"];
        var songRec = songData["recommender"];
        fetch(apiUrl+"add_uri/"+songRec+"/"+userName+"/"+songUri, {
            method: 'POST'
        });
    });
    icon.className = 'icon';
    box.prepend(icon)
    document.getElementById('feed_div').appendChild(box);
}

function createTextDiv(textData) {
    const box = document.createElement("div");
    box.className = "post_text"; 
    box.innerText = textData; 
    document.getElementById('feed_div').appendChild(box); 
}

function createUserNameDiv(postUser) {
    const box = document.createElement("div"); 
    box.innerText = postUser; 
    box.className = "post_header"; 
    document.getElementById('feed_div').appendChild(box); 
}

function generatePost(postData) {
    createUserNameDiv(postData["username"]); 
    createTextDiv(postData["text"]); 
    createSongDiv(postData["song"]);

}