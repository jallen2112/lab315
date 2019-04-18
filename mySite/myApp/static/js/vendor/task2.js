//The list variable below retrieves and represents the html element with the id of 'content'
//with this variable you can alter the html of a page within a js file
var list = document.getElementById('content');

//This list variable represents the button dropdown menu which we will be adding 
//functionality to in this task.
var buttonDropdown = document.getElementById('content2');


//You can use XMLHttpRequest objects to interact with servers and endpoints
//You can use an XMLHttpRequest object to retrieve the baseball data rendered as json data to localhost:8000/last5games

var xhttp = new XMLHttpRequest();

//Once XMLHttpRequest object sends a request to the server, then the onload function defines what we do with the response
//This is where you will begin writing your solution
xhttp.onload= function()
{
  //This allows you to parse and store the response as a json object that you can interact with.
  var info = JSON.parse(this.responseText);

  /** Start writing your solution here **/

}

/** Write any functions you might need here **/

//initializes a GET request to the /last5games endpoint, where the data we need to access is available
xhttp.open("GET", "/last5games", true);
//sends the initialized request
xhttp.send();
