document.getElementById("signin").onclick = function(){
// we riding up on this bitch

var xhr = new XMLHttpRequest();

xhr.onreadystatechange = function () {
    if (this.readyState != 4) return;
    if (this.status == 200) {
        if(this.responseText.includes("Recaptcha Failed")){
		alert('Invalid captcha') //ha succa
		window.location.replace("/html/LoginPage.html");
	}else if(this.responseText.includes("Failed")){
		alert('Incorrect username and password combination')
		window.location.replace("/html/LoginPage.html");
	}else{
		document.cookie = this.responseText.replace(/(\r\n|\n|\r)/gm, "");
		window.location.replace("/python/index.py");
	};
    };
};


var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
var recap = grecaptcha.getResponse();

if(username == ""){
	alert('Enter a username');
}else if(password == ""){
	alert('Enter a password');
}else{
	xhr.open('GET', '/python/signin.py?username='+username+'&password='+password+'&recap='+recap, true);
	xhr.send(null);
}
};
