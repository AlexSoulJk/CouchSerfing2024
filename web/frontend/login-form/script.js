document.getElementById("login-form").addEventListener("submit", function(event){
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    console.log("Username: " + username + ", Password: " + password);

    document.getElementById("login-container").style.display = "none";
});

