var list = document.getElementById('content');
var buttonDropdown = document.getElementById('content2');

var xhttp = new XMLHttpRequest();

xhttp.onload= function()
{
  var info = JSON.parse(this.responseText);
  displayTeams(info);
  ListButtons(info);
}

function displayTeams(info){
  for(i=0;i<info.baseball.length;i++){
    appendList(info.baseball[i].team);
  }
}

xhttp.open("GET", "/todaysgames", true);
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

function listSection(id, info, i) {
  clearEventList();
  for(j=0;j<5;j++){
    gameStatus = getGameStatus(info.baseball[i].starttimes[j].start, info.baseball[i].endtimes[j].end)

    //This calls the appendListColors function which works the same as the appendList function
    //except it also color codes the displayed event based on the gameStatus value passed in. 
    appendListColors(info.baseball[i].games[j].game, gameStatus);
  }
}

function assignTeamButton(buttonId, info, i){
  document.getElementById(buttonId).addEventListener("click", function() {
    listSection(buttonId, info, i);
  }, false);
}

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

/* 
   Most of the code above is the same as the solution for task 2
   The details can be found in task2solution.js */

/* 
   This function works almost identically to the appendList function, 
   but with the addition of color coding the list blocks based on the current time.
   This color is based on the passed in gameStatus variable. */

function appendListColors(message, gameStatus) {

  var textContent = document.createTextNode(message);

  var node = document.createElement("div");
  node.appendChild(textContent);

  var att = document.createAttribute("style");

  var att2 = document.createAttribute("class");
  att2.value = "card";

  if(gameStatus == "Finished"){
    att.value = "background: #C0C0C0; padding: 1em;";
  }
  else if(gameStatus == "Upcoming"){
    att.value = "background: #1daf06; padding: 1em;";
  }
  else{
    att.value = "background: #3b9dd1; padding: 1em;";
  }

  node.setAttributeNode(att);
  node.setAttributeNode(att2);

  list.appendChild(node);
}


/*
   Get the status of the game as either Upcoming, Finished, or Now based on the current time.
   Start and end times of the event are passed in to compare to a javascript datetime object that 
   represents the current time. Since we only care about the hours and minutes, this function
   does some parsing to get those two values. 
   */

function getGameStatus(start, end){
  var today = new Date();
  var time = today.getHours() + ":" + today.getMinutes();

  var res = time.split(":");
  var curHours = Number(res[0]);
  var curMin = Number(res[1]);

  var myStart = start.split(":");
  var myStartHours = Number(myStart[0]);
  var myStartMins = Number(myStart[1]);

  var myEnd = end.split(":");
  var myEndHours = Number(myEnd[0]);
  var myEndMins = Number(myEnd[1]);

  if(myStartHours > curHours/* && myEndHours > curHours*/){
    return "Upcoming";
  }
  else if(myEndHours < curHours){
    return "Finished";
  }
  else{
    if(myStartHours == curHours && myStartMins > curMin){
      return "Upcoming";
    }
    if(myEndHours == curHours && myEndMins < curMin){
      return "Finished"
    }
    return "Now"
  }

}
