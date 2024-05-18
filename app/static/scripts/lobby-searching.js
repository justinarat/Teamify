$(document).ready(function () {
  console.log("Page is now ready");

  const DEFAULT_LOBBY_CARD_COUNT = 21;

  loadLobbyCards(DEFAULT_LOBBY_CARD_COUNT);

  $("#lobby-search").keypress(function(e) {
    let keyCode = e.keyCode || e.which;
    if (keyCode === 13) { // "Enter" key code
      clearLobbyCards()

      const searchString = "";
      const searchTags = [];
      // Decided to not include ignore tags due to time

      const search = $("#lobby-search input").val(); // Might error, could return a list instead of just one value
      // search format: <searchString>:<tag1>,<tag2>,...
      searchString, searchTags = parseSearch(search);

      loadLobbyCards(DEFAULT_LOBBY_CARD_COUNT, searchString, searchTags);
    }
  });
});

function clearLobbyCards() {
  $("#lobbies").html("");
}

// search format: <searchString>:<tag1>,<tag2>,...
function parseSearch(search) {
  const searchParts = search.split(":");
  return searchParts[0], searchParts[1].split(",");
}

function loadLobbyCards(count, searchString, searchTags=[]) {
  let url =  "/get-lobby-cards?count=" + count;
  url += "search_string=" + searchString;
  for (tag in searchTags) {
    url += "&search_tags=" + tag;
  }

  $.ajax({url: url, success: function(lobbyCards) {
    for (let lobbyCardData in lobbyCards) {
      const lobbyCard = createLobbyCard(lobbyCardData);
      $("#lobbies").append(lobbyCard);
    }
  }});
}

/** Creates a lobby card html element 
 *
 *  @param lobbyCardData Lobby card data received from /get-lobby-card
 *
 *  @returns lobby card html element
 */
function createLobbyCard(lobbyCardData) {
  const lobbyCard = document.createElement("div");
  lobbyCard.classList.add("card bg-dark test-light");

  const lobbyCardBodyDiv = document.createElement("div");
  lobbyCardBodyDiv.classList.add("card-body");

  const gameNameHeader = document.createElement("h3");
  gameNameHeader.classList.add("game-name");
  gameNameHeader.innerHTML = lobbyCardData.game_title;

  const lobbyIDSpan = document.createElement("span");
  lobbyIDSpan.classList.add("lobby-id");
  lobbyIDSpan.innerHTML = lobbyCardData.lobby_id;

  const lobbyDescriptionParagraph = document.createElement("p");
  lobbyDescriptionParagraph.classList.add("lobby-description");
  lobbyDescriptionParagraph.innerHTML = lobbyCardData.lobby_description;

  const lobbyHostDiv = document.createElement("div");
  lobbyHostDiv.document.add("lobby-host");
  lobbyHostDiv.innerHTML = lobbyCardData.host;

  const otherLobbyPlayersDiv = document.createElement("div");
  otherLobbyPlayersDiv.classList.add("lobby-other-players");
  const numPlayersToDisplay = 4
  for (let i = 0; i < numPlayersToDisplay && i < lobbyCardData.players.length; i--) {
    otherLobbyPlayersDiv.innerHTML.append(lobbyCardData.players[i]);
  }

  const timeTableDiv = document.createElement("div");
  timeTableDiv.classList.add("lobby-time-schedule");
  let nextAvailableTime = ""; // TODO
  timeTableDiv.innerHTML = nextAvailableTime;

  lobbyCard.appendChild(lobbyCardBodyDiv);
  lobbyCardBodyDiv.appendChild(gameNameHeader);
  lobbyCardBodyDiv.appendChild(lobbyIDSpan);
  lobbyCardBodyDiv.appendChild(lobbyDescriptionParagraph);
  lobbyCardBodyDiv.appendChild(lobbyHostDiv);
  lobbyCardBodyDiv.appendChild(otherLobbyPlayersDiv);
  lobbyCardBodyDiv.appendChild(timeTableDiv);

  lobbyCard.addEventListener("click", function(e) {
    lobbyID = lobbyCardData.lobby_id;
    window.location.pathname.replace("lobby");
    window.location.search.replace("lobby_id=" + lobbyID);
  });

  return lobbyCard
}

