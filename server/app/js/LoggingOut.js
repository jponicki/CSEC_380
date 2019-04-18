document.getElementById("logout").onclick = function(){

var xhr = new XMLHttpRequest();

xhr.onreadystatechange = function () {
    if (this.readyState != 4) return;
    if (this.status == 200) {
      	if(this.responseText.includes("invalid")){
	        document.cookie = "session=; max-age=-9999; path=/;"; //cookies amiright
      		window.location.replace("/html/LoginPage.html");
      	}else{
		document.cookie = "session=; max-age=-9999; path=/;";
      		window.location.replace("/html/LoginPage.html");
      	};
    };
};



xhr.open('GET', '/python/LoggingOut.py', true);
xhr.send(null);

}
