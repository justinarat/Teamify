$(document).ready(function() {
  let url = "http://localhost:5000";
  let socket = io.connect(url);

  socket.on("connect", function() {
    socket.emit("player-join");
  });

  // Events for players joining or leaving
  socket.on("player-join", function(data) {
    let username = data.sender_username;
    $("#players").append("<span>" + username + "</span>");
    let text = "<div class='chat-text'><span class='server-text'>" +
                "<span class='username'>" + username + 
                "</span> has joined</span></div>";
    $("#chat-log").append(text);
  });

  socket.on("player_leave", function(data) {
    let username = data.sender_username;
    $(".players").map(function() {
      if (this.innerHTML === "<span>" + username + "</span>") 
        this.remove();
    });
    let text = "<div class='chat-text'><span class='server-text'>" +
                "<span class='username'>" + username + 
                "</span> has left</span></div>";
    $("#chat-log").append(text);
  });

  socket.on("player_kick", function(data) {
    // TODO: figure out how to implement this so that the kicked player can't
    //       just remove this code to avoid being kicked.
  });

  // Events all users can send
  socket.on("player_text", function(data) {
    let username = data.sender_username;
    let playerText = data.body;
    let text = "<div class='chat-text'><span class='username'>" +
                username + "</span>:" +
                playerText + "</div>";
    $("#chat-log").append(text);
  });

  // Events only the host (or lobby mods) can send
  socket.on("add_tag", function(data) {
    let tag = data.body;
    $("#tags").append("<span class='tag'>" + tag + "</span>");
  });

  socket.on("remove_tag", function(data) {
    let tag = data.body;
    $(".tag").map(function() {
      if (this.innerHTML === tag) this.remove();
    });
  });

  socket.on("change_lobby_name", function(data) {
    let newLobbyName = data.body;
    $("#lobby-name").html(newLobbyName);
  });

  socket.on("change_description", function(data) {
    let newDescription = data.body;
    $("#lobby-description").html(newDescription);
  });

  socket.on("change_time_schedule", function(data) {
    // TODO: change schedule, also need to decide on data.body format,
    //       or maybe data.body is just html
  });

  // Events that the user sends to the server
  // TODO: setup commands for sendings events to server
  $("#chat-input").keypress(function(e) {
    // TODO: clean up this code
    let keyCode = e.keyCode || e.which;
    if (keyCode === 13) { // "Enter" key code
      let text = $("chat-input").val();
      $("chat-input").val("");
      let dataToSend = {
        body: text
      };
      socket.emit("player-text", dataToSend);
    }
  });
});