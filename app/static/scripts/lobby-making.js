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


function timeDisplay() {
  var selectedOption = document.getElementById("time-type");
  var timeOptionChunk = document.getElementById("time-option");
  if (selectedOption.checked == true) {
    for (let i = 0; i < 7; i++) {
      let currDay = days[i];
      let currDayFull = daysFull[i];
      let htmlChunk =
        "<input type='checkbox' id='" + currDay + "-checkbox'>" +
        "<label for='" +currDay + "-checkbox'>" + currDayFull + ":</label>" +
        "<div id='" + currDay + "'></div>" +
        "<br />";
      timeOptionChunk.insertAdjacentHTML("beforeend", htmlChunk);
    }
    days.forEach(function (day) {
      var toggleOption = day + "-checkbox";
      document
        .getElementById(toggleOption)
        .addEventListener("change", showGeneral(day, toggleOption));
    });
  } else {
    timeOptionChunk.innerHTML = "";
  }
}

function showGeneral(day, toggleOption) {
  return function () {
    var dayElement = document.getElementById(day);
    let selectedOption = document.getElementById(toggleOption);
    if (selectedOption.checked == true) {
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
    } else {
      dayElement.innerHTML = "";
    }
  };
}

let customCount = 0;
let addCustomTagButton = document.getElementById("add-custom-tag");

addCustomTagButton.addEventListener("click", function(){
  customCount++;
});

function makeCustomTag(){
  let customTags = document.getElementById("custom-tags");
  // let sectionID = "customSection" + customCount;
  let customTagHTML =
    "<div id='customSection" + customCount + "'>"+
    "  <input type='text' id ='custom-tag-" + customCount + "' placeholder='Enter custom tag'>"+
    "  <button id='remove-custom-tag" + customCount + "' onclick='removeCustomTag(this)' type='button'>- Remove Custom Tag</button>"+
    "  <br>"+
    "</div>";
  
  customTags.insertAdjacentHTML("beforeend", customTagHTML);
}

function removeCustomTag(removeButton){
  let sectionID = removeButton.parentNode.id;
  let customSection = document.getElementById(sectionID);
  customSection.remove();
}
