(function fetchNptel_metadata(){
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "//localhost:5000/fetchNptel_metadata", true); 
  xhttp.setRequestHeader("Access-Control-Allow-Origin", "*");
  xhttp.send(null);
  xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementsByTagName("body")[0].innerHTML =this.responseText;
	    }
  };
}());