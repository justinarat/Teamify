const joinButton = document.getElementById("join-lobby");
const dontJoinButton = document.getElementById("dont-join-lobby");

function sendJoinLobbyRequest(isJoining) {
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/join-lobby-request");
  xhr.setRequestHeader("Content-Type", "application/json");

  const lobby_id = new URLSearchParams(window.location.search).get("lobby_id");
  const body = JSON.stringify({
    lobby_id: lobby_id, 
    is_joining: isJoining,
  });

  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      window.location = xhr.responseURL;
    }
  }

  xhr.send(body);
}

joinButton.addEventListener("click", function() {
  sendJoinLobbyRequest(true)
});
dontJoinButton.addEventListener("click", function () {
  sendJoinLobbyRequest(false)
});

