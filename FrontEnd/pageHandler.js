let enter = document.getElementById("enter");
let page = document.getElementById("page");
let settings = document.getElementById("settings");
let settingsPage = document.getElementById("settings_page");
let titles = document.getElementsByClassName("title");
let profile = document.getElementById("profile");

for (let index = 0; index < titles.length; index++) {
    titles[index].addEventListener("click", function (event) {
        page.hidden = false;
        settingsPage.hidden = true;
    });
}

enter.addEventListener("click", function(event) {
    enter.hidden = true;
    page.hidden = false;
    event.stopPropagation();
});

settings.addEventListener("click", function(event) {
    page.hidden = true;
    settingsPage.hidden = false;
    event.stopPropagation();
});

profile.addEventListener("click", function(event) {
    event.stopPropagation();
});