$(document).ready(function () {
  loadJoinedLobbies(); 
});

function loadJoinedLobbies() {
  $.ajax({
    url: "/get-joined-lobbies",
    success: function (lobbyCards) {
      for (let lobbyCardData of lobbyCards.lobby_cards) {
        const lobbyCard = createLobbyCard(lobbyCardData);
        $("#lobbies").append(lobbyCard);
      }
    },
  });
}
