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
  var selectedOption = document.getElementById("reoccuring-time");
  var timeOptionChunk = document.getElementById("time-option");
  if (selectedOption.checked == true) {
    timeOptionChunk.innerHTML = "";
    for (let i = 0; i < 7; i++) {
      let currDay = days[i];
      let currDayFull = daysFull[i];
      let htmlChunk =
        "<div id='"+ currDay + "-section'>"+
        "<input type='checkbox' id='" + currDay + "-checkbox' onclick='showGeneral(this)'>" +
        "<label for='" + currDay + "-checkbox'>" + currDayFull + ":</label>" +
        "<div id='" + currDay + "'></div>" +
        "<br />"+
        "</div>";
      timeOptionChunk.insertAdjacentHTML("beforeend", htmlChunk);
    }
    let htmlChunk =
      "<div id='custom-events'></div>" +
      "<button id='add-special-event' onclick='makeSpecialEvent()' type='button'>+ Add Special Event</button>";
    timeOptionChunk.insertAdjacentHTML("beforeend", htmlChunk);
  } else {
    timeOptionChunk.innerHTML = "";
    let htmlChunk =
      "<div id='onetimeSet'>" +
      "  <label for='onetimeFrom'>From:</label>" +
      "  <input type='datetime-local' id='onetimeFrom' />" +
      "  <label for='onetimeTo'> To: </label>" +
      "  <input type='datetime-local' id='onetimeFrom' />" +
      "</div>";
    timeOptionChunk.insertAdjacentHTML("beforeend", htmlChunk);
  }
}

function showGeneral(dayCheckbox) {
  let sectionID = dayCheckbox.id;
  let day = sectionID.substring(0, 3);
  // let dayElement = document.getElementById("day");
  let dayMainID = dayCheckbox.parentNode.id;
  let dayMain = document.getElementById(dayMainID);
  let dayElement = dayMain.children[2];
  if (dayCheckbox.checked == true) {
    dayElement.innerHTML =
      "<label for='" + day + "-from'>From:</label>" +
      "<input type='time' id='" + day + "-from' />" +
      "<label for='" + day + "-to'> To: </label>" +
      "<input type='time' id='" + day + "-to' />";
  } else {
    dayElement.innerHTML = "";
  }
}

let customCount = 0;
let addCustomTagButton = document.getElementById("add-custom-tag");

addCustomTagButton.addEventListener("click", function () {
  customCount++;
});

function makeCustomTag() {
  let customTags = document.getElementById("custom-tags");
  let customTagHTML =
    "<div id='customSection" +
    customCount +
    "'>" +
    "  <input type='text' id ='custom-tag-" + customCount + "' placeholder='Enter custom tag'>" +
    "  <button id='remove-custom-tag" + customCount + "' onclick='removeCustom(this)' type='button'>- Remove Custom Tag</button>" +
    "  <br>" +
    "</div>";

  customTags.insertAdjacentHTML("beforeend", customTagHTML);
}

function removeCustom(removeButton) {
  let sectionID = removeButton.parentNode.id;
  let customSection = document.getElementById(sectionID);
  customSection.remove();
}

let customEventCount = 0;

function makeSpecialEvent() {
  let customEvents = document.getElementById("custom-events");

  let customEventHTML =
    "<div id='customEventSection" + customEventCount + "'>" +
    "  <input type='date' id ='custom-event-" + customCount + "'>" +
    "  <br>" +
    "  <label for='eventFrom" + customEventCount + "'>From:</label>" +
    "  <input type='time' id='eventFrom" + customEventCount + "' />" +
    "  <label for='eventTo" + customEventCount + "'> To: </label>" +
    "  <input type='time' id='eventFrom" + customEventCount + "' />" +
    "  <input type='text' id ='custom-event-description" + customCount + "' placeholder='Event Description (Opitonal)'>" +
    "  <button id='remove-custom-event" + customCount + "' onclick='removeCustom(this)' type='button'>- Remove Special Event</button>" +
    "  <br><br>" +
    "</div>";

  customEvents.insertAdjacentHTML("beforeend", customEventHTML);
  customEventCount++;
}
