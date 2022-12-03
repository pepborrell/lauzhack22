const auth = new Auth();
console.log(JSON.parse(localStorage.getItem("auth")));
document.querySelector(".logout").addEventListener("click", (e) => {
    auth.logOut();
});

var hello = localStorage.getItem("my_item");
var user = localStorage.getItem("username");
console.log(hello); 
console.log(user); 