const leaveButton = document.getElementById("leave-lobby");

leaveButton.addEventListener("click", function() {
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/leave-lobby-request");
  xhr.setRequestHeader("Content-Type", "application/json");

  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      window.location = xhr.responseURL;
    }
  }

  xhr.send();
});

