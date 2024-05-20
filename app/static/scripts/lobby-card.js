/** Creates a lobby card html element
 *
 *  @param lobbyCardData Lobby card data received from /get-lobby-card
 *
 *  @returns lobby card html element
 */
function createLobbyCard(lobbyCardData) {
  const lobbyCard = document.createElement("div");
  lobbyCard.classList.add("card");
  lobbyCard.classList.add("bg-dark");
  lobbyCard.classList.add("text-light");

  const lobbyCardBodyDiv = document.createElement("div");
  lobbyCardBodyDiv.classList.add("card-body");
  lobbyCard.appendChild(lobbyCardBodyDiv);

  const gameNameHeader = document.createElement("h3");
  gameNameHeader.classList.add("game-name");
  gameNameHeader.innerHTML = lobbyCardData.game_title;
  gameNameHeader.style.cursor = "pointer";
  gameNameHeader.style.userSelect = "none";
  lobbyCardBodyDiv.appendChild(gameNameHeader);

  const lobbyNameHeader = document.createElement("h5");
  lobbyNameHeader.classList.add("lobby-name");
  lobbyNameHeader.innerHTML = lobbyCardData.lobby_name;
  lobbyCardBodyDiv.appendChild(lobbyNameHeader);

  const lobbyIDSpan = document.createElement("span");
  lobbyIDSpan.classList.add("lobby-id");
  lobbyIDSpan.innerHTML = "lobby ID = " + lobbyCardData.lobby_id;
  lobbyCardBodyDiv.appendChild(lobbyIDSpan);

  const lobbyDescriptionParagraph = document.createElement("p");
  lobbyDescriptionParagraph.classList.add("lobby-description");
  lobbyDescriptionParagraph.innerHTML =
    "desc = " + lobbyCardData.lobby_description;
  lobbyCardBodyDiv.appendChild(lobbyDescriptionParagraph);

  const lobbyHostDiv = document.createElement("div");
  lobbyHostDiv.classList.add("lobby-host");
  lobbyHostDiv.innerHTML = "host = " + lobbyCardData.host;
  lobbyCardBodyDiv.appendChild(lobbyHostDiv);

  const otherLobbyPlayersDiv = document.createElement("div");
  otherLobbyPlayersDiv.classList.add("lobby-other-players");
  otherLobbyPlayersDiv.innerHTML = "players = ";
  for (let i = 0; i < lobbyCardData.players.length; i++) {
    otherLobbyPlayersDiv.innerHTML += lobbyCardData.players[i] + " ";
  }
  lobbyCardBodyDiv.appendChild(otherLobbyPlayersDiv);

  const timeTableDiv = document.createElement("div");
  timeTableDiv.classList.add("lobby-time-schedule");
  timeTableDiv.innerHTML = "next time = " + lobbyCardData.next_available_time;
  lobbyCardBodyDiv.appendChild(timeTableDiv);

  gameNameHeader.addEventListener("click", function (e) {
    e.preventDefault();
    var lobbyID = lobbyCardData.lobby_id;
    var newUrl = "/lobby?lobby_id=" + lobbyID;
    window.location.href = newUrl;
  });

  return lobbyCard;
}
