console.log("here");
let registerButton = document.getElementById("register-button");
registerButton.addEventListener("click", function () {
    let registerDiv = document.getElementById("register");
    let mainPage = document.getElementById("main-page");
    mainPage.innerHTML = registerDiv.innerHTML;
});


