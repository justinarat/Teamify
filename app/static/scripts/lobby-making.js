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

function showCustomTag() {
  let tagSec = document.getElementById("tag1");
  tagSec.classList.remove("not-showing");
  tagSec.value = "true";
}

function removeCustom(tag) {
  let tagSec = document.getElementById(tag);
  tagSec.classList.add("not-showing");
  tagSec.value = "false";
}
