/* The list variable below retrieves and represents the html element 
   with the id of 'content'. With this variable you can alter the 
   html of a page within a js file */

var list = document.getElementById('content');

/* You can use XMLHttpRequest objects to interact with servers and endpoints
   You can use an XMLHttpRequest object to retrieve the baseball data 
   rendered as json data to localhost:8000/last5games */

var xhttp = new XMLHttpRequest();

/* Once XMLHttpRequest object sends a request to the server, 
   then the onload function defines what we do with the response
   This is where you will begin writing your solution */

xhttp.onload= function()
{
  var info = JSON.parse(this.responseText);
  displayTeams(info);
}

//parses the json and lists every team object to the html page
function displayTeams(info){
  for(i=0;i<info.baseball.length;i++){
    appendList(info.baseball[i].team);
  }
}


//initializes a GET request to the /last5games endpoint, where the data we need to access is available
xhttp.open("GET", "/last5games", true);
//sends the initialized request
xhttp.send();

/* Function to append an html object to our html page and give it the desired 
   text ouput, attributes etc. First we create an html text node with the 
   passed in argument as the body. Then we create a div element that we can 
   append our text node to. Then we create a class attribute to set to our div
   element to identify what class our element belongs to so that the webpage can render
   and format the element properly. Finally, we append our newly created html element to 
   the end of our html list variable, which will be rendered to our webpage */

function appendList(message) {

  var textContent = document.createTextNode(message);

  var node = document.createElement("div");
  node.appendChild(textContent);


  var attribute = document.createAttribute("class");
  attribute.value = "card";

  node.setAttributeNode(attribute);

  list.appendChild(node);
}
