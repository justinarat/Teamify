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
  }
}
