function req_xhr(){
	var xhr = new XMLHttpRequest();
	xhr.open("GET", url + parameter)
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhr.send();
	console.log(xhr.responseText);
}
