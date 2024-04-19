console.log("Script is running");

const days = ["mon", "tue"];



days.forEach(function(day){
  var elementID = day + "-toggle"
  document.getElementById(elementID).addEventListener("change", showTime(day, elementID));
});


function showTime(day, elementID){
  return function(){
    console.log("Change detected!");
    var element = document.getElementById(day);
    var selectedOption = document.getElementById(elementID).value;
    if (selectedOption == 'yes' && element.classList.contains('not-showing')){
      element.classList.remove("not-showing");
      element.classList.add("showing");
    }
    else if (selectedOption == 'no' && element.classList.contains('showing')){
      element.classList.remove("showing");
      element.classList.add("not-showing");
    }
  }
}

