console.log("Script is running");

const days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];



days.forEach(function(day){
  var toggleOption = day + "-toggle"
  document.getElementById(toggleOption).addEventListener("change", showTime(day, toggleOption));
});


function showTime(day, toggleOption){
  return function(){
    console.log("Change detected!");
    var element = document.getElementById(day);
    var selectedOption = document.getElementById(toggleOption).value;
    if (selectedOption == 'yes' && element.innerHTML == ""){
      element.innerHTML = "<label for='" + day + "-from'>From:</label>" +
      "<input type='time' id='" + day + "-from' />" +
      "<label for='" + day + "-to'> To: </label>" +
      "<input type='time' id='" + day + "-to' />";
    }
    else if (selectedOption == 'no' && element.innerHTML != ""){
      element.innerHTML = "";
    }
  }
}

