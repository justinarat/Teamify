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
