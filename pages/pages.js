console.log("Script is running");
document.getElementById("mon-toggle").addEventListener("change", showTime);

function showTime(){
  console.log("Change detected!");
  var element = document.getElementById("monday");
  var selectedOption = document.getElementById("mon-toggle").value;
  if (selectedOption == 'yes' && element.classList.contains('not-showing')){
    element.classList.remove("not-showing");
    element.classList.add("showing");
  }
  else if (selectedOption == 'no' && element.classList.contains('showing')){
    element.classList.remove("showing");
    element.classList.add("not-showing");
  }
}
// function showTime(day, event) {
//   event.preventDefault();
//   var element = document.getElementById(day);
//   if (element.style.display === "none") {
//     element.style.display = "block"; // or "inline" depending on your needs
//   } else {
//     element.style.display = "none";
//   }
// }
