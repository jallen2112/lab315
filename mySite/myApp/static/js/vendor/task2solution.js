var list = document.getElementById('content');
var buttonDropdown = document.getElementById('content2');

var xhttp = new XMLHttpRequest();

xhttp.onload= function()
{
  var info = JSON.parse(this.responseText);
  displayTeams(info);
  //Call function to add buttons to our webpage
  ListButtons(info);
}

function displayTeams(info){
  for(i=0;i<info.baseball.length;i++){
    appendList(info.baseball[i].team);
  }
}

xhttp.open("GET", "/last5games", true);
xhttp.send();

function appendList(message) {

  var textContent = document.createTextNode(message);

  var node = document.createElement("div");
  node.appendChild(textContent);

  var attribute = document.createAttribute("class");
  attribute.value = "card";
  node.setAttributeNode(attribute);

  var attributeStyle = document.createAttribute("style");
  attributeStyle.value = "padding: 1em;";
  node.setAttributeNode(attributeStyle);

  list.appendChild(node);
}

/* Most of the code above is the same as the solution for task 1  
   The details can be found in task1solution.js */


/* This function calls clearEventList() to clear the card on the webpage
   and then calls appendList() to display all the passed in game information.
   The index of which team to pull games from is also passed in. */

function listSection(info, i) {
  clearEventList();
  for(j=0;j<5;j++){
    appendList(info.baseball[i].games[j].game);
  }
}

/* This function creates the dropdown menu for the button 
   For each team that needs it's own button, a list element is created
   with game information appended as a text object and then the list element is given 
   the button attribute and appended to the clickable dropdown menu 
   Each button is given a unique identifier so that it can be identified by an id.
   assignTeamButton is called on each button to add functionality when pressed. */

function ListButtons(info){
  var baseballData = info.baseball;
  for(var i=0;i<baseballData.length;i++){

    var textContent = document.createTextNode(baseballData[i].team);
    var newObject = document.createElement("LI");
    var classAtt = document.createAttribute("class");
    var styleAtt = document.createAttribute("style");
    classAtt.value = "no-bullets";
    newObject.setAttributeNode(classAtt);
    styleAtt.value = "list-style-type: none;";
    newObject.setAttributeNode(styleAtt);

    var node = document.createElement("a");
    var idAtt = document.createAttribute("id");
    var a = document.createAttribute("button");
    idAtt.value = baseballData[i].team;
    node.setAttributeNode(a);
    node.setAttributeNode(idAtt);
    node.appendChild(textContent);
    newObject.appendChild(node);
    buttonDropdown.appendChild(newObject);
    assignTeamButton(baseballData[i].team, info, i);
  }
}


/*
   The main purpose of this function is to use the passed in button id to add an event listenr
   to the button we created. This event listener adds a unique call to the listSection button with the passed in 
   arguments each time a button is pressed.  */

function assignTeamButton(buttonId, info, i){
  document.getElementById(buttonId).addEventListener("click", function() {
    listSection(info, i);
  }, false);
}

/*
   This is a helper function to clear the card on the webpage. We need
   to clear the page whenever a user presses a different button so that the old 
   data doesn't stay on the card. */

function clearEventList(){
  if (list.hasChildNodes())
  {
      var nodeCount = list.childNodes.length;
      for(var i=0; i<nodeCount; i++)
      {
              list.removeChild(list.childNodes[0]);
      }
  }
}
