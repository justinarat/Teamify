$(document).ready(function () {
  const DEFAULT_LOBBY_CARD_COUNT = 21;

  loadLobbyCards(DEFAULT_LOBBY_CARD_COUNT, "");

  $("#lobby-search").submit(function (e) {
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

function loadLobbyCards(count, searchString, searchTags = []) {
  let url = "/get-lobby-cards?count=" + count;
  url += "&search_string=" + searchString;
  for (let i = 0; i < searchTags.length; i++) {
    url += "&search_tags=" + searchTags[i];
  }

  $.ajax({
    url: url,
    success: function (lobbyCards) {
      for (let lobbyCardData of lobbyCards.lobby_cards) {
        const lobbyCard = createLobbyCard(lobbyCardData);
        $("#lobbies").append(lobbyCard);
      }
    },
  });
}

