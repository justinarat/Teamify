const days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];
const daysFull = [
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday",
  "Sunday",
];

function showGeneral(day, toggleOption) {
  return function () {
    var dayElement = document.getElementById(day);
    let selectedOption = document.getElementById(toggleOption).value;
    if (selectedOption == "yes" && dayElement.innerHTML == "") {
      dayElement.innerHTML =
        "<label for='" +
        day +
        "-from'>From:</label>" +
        "<input type='time' id='" +
        day +
        "-from' />" +
        "<label for='" +
        day +
        "-to'> To: </label>" +
        "<input type='time' id='" +
        day +
        "-to' />";
    } else if (selectedOption == "no" && dayElement.innerHTML != "") {
      dayElement.innerHTML = "";
    }
  };
}

document.getElementById("time-type").addEventListener("change", timeDisplay);

function timeDisplay() {
  var timeOptionChunk = document.getElementById("time-option");
  let selectedOption = document.getElementById("time-type").value;
  if (selectedOption == "general" && timeOptionChunk.innerHTML == "") {
    for (let i = 0; i < 7; i++) {
      let currDay = days[i];
      let currDayFull = daysFull[i];
      let htmlChunk =
        "<label for='" +
        currDay +
        "-toggle'>" +
        currDayFull +
        ":</label>" +
        "<select id='" +
        currDay +
        "-toggle'>" +
        "  <option value='no'>No</option>" +
        "  <option value='yes'>Yes</option>" +
        "</select>" +
        "<div id='" +
        currDay +
        "'></div>" +
        "<br />";
      timeOptionChunk.insertAdjacentHTML("beforeend", htmlChunk);
    }
    days.forEach(function (day) {
      var toggleOption = day + "-toggle";
      document
        .getElementById(toggleOption)
        .addEventListener("change", showGeneral(day, toggleOption));
    });
  } else if (selectedOption != "general" && timeOptionChunk.innerHTML != "") {
    timeOptionChunk.innerHTML = "";
  }
}
