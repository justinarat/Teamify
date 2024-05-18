$(document).ready(function () {
  console.log("Page is now ready");

  const DEFAULT_LOBBY_CARD_COUNT = 21;

  loadLobbyCards(DEFAULT_LOBBY_CARD_COUNT, ""); // "world" is temp

  $("#lobby-search").submit(function(e) {
    e.preventDefault();
    clearLobbyCards();

    let searchString = "";
    let searchTags = [];
    // Decided to not include ignore tags due to time

    const search = $("#lobby-search input").val(); // Might error, could return a list instead of just one value
    // search format: <searchString>:<tag1>,<tag2>,...
    [searchString, searchTags] = parseSearch(search);

    loadLobbyCards(DEFAULT_LOBBY_CARD_COUNT, searchString, searchTags);
  });
});

function clearLobbyCards() {
  $("#lobbies").html("");
}

// search format: <searchString>:<tag1>,<tag2>,...
function parseSearch(search) {
  if (search.includes(":")) {
    const searchParts = search.split(":");
    return [searchParts[0], searchParts[1].split(",")];
  } else {
    return [search, []];
  }
}

function loadLobbyCards(count, searchString, searchTags=[]) {
  let url =  "/get-lobby-cards?count=" + count;
  url += "&search_string=" + searchString;
  for (tag in searchTags) {
    url += "&search_tags=" + tag;
  }

  $.ajax({url: url, success: function(lobbyCards) {
    for (let lobbyCardData of lobbyCards.lobby_cards) {
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
  lobbyCard.classList.add("card");
  lobbyCard.classList.add("bg-dark");
  lobbyCard.classList.add("text-light");

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
  lobbyHostDiv.classList.add("lobby-host");
  lobbyHostDiv.innerHTML = lobbyCardData.host;

  const otherLobbyPlayersDiv = document.createElement("div");
  otherLobbyPlayersDiv.classList.add("lobby-other-players");
  for (player in lobbyCardData.players) {
    otherLobbyPlayersDiv.innerHTML += player;
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

