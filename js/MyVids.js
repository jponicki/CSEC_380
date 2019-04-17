var xhr = new XMLHttpRequest();

xhr.onreadystatechange = function () {
	if (this.readyState != 4) return;
	if (this.status == 200) {
    		if(this.responseText.includes("invalid token")){
			document.cookie = "session=; max-age=-9999; path=/;";
        	    	window.location.replace("/html/LoginPage.html");
        	}else{
        	    	document.getElementById('videos').innerHTML = this.responseText;
        	}
    	};
};

var cookie = document.cookie;
try{
   	var token = cookie.split('session=')[1].split(';')[0];
   	if(token == null){
        	window.location.replace("/html/LoginPage.html");
   	}else{
        	xhr.open('GET', '/python/MyVids.py', true);
        	xhr.send(null);
   	};
}
catch(err){
   	window.location.replace("/html/LoginPage.html"); // just make them login amright?
}
