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

function showGeneral(day) {
  let daySec = document.getElementById(day);
  let dayCheckboxID = day + "-checkbox";
  let dayCheckbox = document.getElementById(dayCheckboxID);

  let fromFieldID = day + "-from";
  let toFieldID = day + "-to";

  let fromField = document.getElementById(fromFieldID);
  let toField = document.getElementById(toFieldID);

  if(dayCheckbox.checked == true) {
    daySec.classList.remove("not-showing");
    fromField.setAttribute('required','required');
    toField.setAttribute('required','required');

  } else {
    daySec.classList.add("not-showing");
    fromField.removeAttribute('required','required');
    toField.removeAttribute('required','required');
    fromField.value = "";
    toField.value = "";
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

function enableSkills() {
  var skillCheck = document.getElementById("enable-skill-level");
  var skillLevelField = document.getElementById("skill-levels");
  if (skillCheck.checked == true) {
    for (let i = 0; i <= 5; i++) {
      let currSkillLevel = skillLevels[i];
      let skillID = currSkillLevel.toLowerCase;
      let htmlChunk =
        "<input type='radio' id='" +
        skillID +
        "' name='skill-level'>" +
        "<label for='" +
        skillID +
        "'>" +
        currSkillLevel +
        "</label>" +
        "<br>";
      skillLevelField.insertAdjacentHTML("beforeend", htmlChunk);
    }
  } else {
    skillLevelField.innerHTML = "";
  }
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
