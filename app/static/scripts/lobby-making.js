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

  if(dayCheckbox.checked == true) {
    daySec.classList.remove("not-showing");
  } else {
    daySec.classList.add("not-showing");
  }
}
