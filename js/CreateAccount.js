document.getElementById("createAccount").onclick = function(){

var xhr = new XMLHttpRequest();

xhr.onreadystatechange = function () {
    if (this.readyState != 4) return;
    if (this.status == 200) {
	if(this.responseText.includes("User Created")){
		alert('Account Created! Please now log into your account')
		window.location.replace("/");
	}else if(this.responseText.includes("Already Exists")){
		alert('Username already taken');
	}else if(this.responseText.includes("Recaptcha Failed")){
		alert('Invalid captcha'); // nice try succa
	};
    };
};


var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
var confirmPassword = document.getElementById("confirmPassword").value;
var displayName = document.getElementById("displayName").value;
var recap = grecaptcha.getResponse(); // Capturing a moment

if(username == ""){
	alert('Enter a username');
}else if(displayName == ""){
	alert('Enter a display name')
}else if(password != confirmPassword){
	alert('Passwords do not match');
}else if(password == ""){
	alert('You need a password');
}else{
	//put in dem creds. Show your legitness
	xhr.open('GET', '/python/newAccount.py?username='+username+'&displayName='+displayName+'&password='+password+'&recap='+recap, true);
	xhr.send(null);
}
};
