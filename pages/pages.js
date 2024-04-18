function showTime(day, event) {
  event.preventDefault();
  var element = document.getElementById(day);
  if (element.style.display === "none") {
    element.style.display = "block"; // or "inline" depending on your needs
  } else {
    element.style.display = "none";
  }
}
