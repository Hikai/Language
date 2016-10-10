for (i = 1; i <= 20; i++) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/login", false);
    xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xhr.send();
}