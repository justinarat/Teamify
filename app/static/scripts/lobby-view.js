const joinButton = document.getElementById("join-lobby");
const dontJoinButton = document.getElementById("dont-join-lobby");

joinButton.addEventListener("click", function() {
  const xhr = new XMLHttpRequest();
  xhr = open("POST", "/join-lobby-request");
  xhr.setRequestHeader("Content-Type", "application/json");

  const lobby_id = new URLSearchParams(window.location.search).get("lobby_id");
  const body = JSON.stringify({
    lobby_id: lobby_id, 
    is_joining: true,
  });

  xhr.send(body);
});

dontJoinButton.addEventListener("click", function() {
  const xhr = new XMLHttpRequest();
  xhr = open("POST", "/join-lobby-request");
  xhr.setRequestHeader("Content-Type", "application/json");

  const lobby_id = new URLSearchParams(window.location.search).get("lobby_id");
  const body = JSON.stringify({
    lobby_id: lobby_id, 
    is_joining: false,
  });

  xhr.send(body);
});

