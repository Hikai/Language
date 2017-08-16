function req_xhr(){
	var xhr = new XMLHttpRequest();
	xhr.open("GET", url + parameter)
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhr.send();
	if ((xhr.readyState == 4) && (xhr.status == 200)) {
		if (xhr.responseText.indexOf("Login failed") == -1) {
			console.log("correct!")
	}
}
