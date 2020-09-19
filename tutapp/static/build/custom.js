document.addEventListener("DOMContentLoaded", function () {
  var mediaElements = document.querySelectorAll("video, audio"),
    total = mediaElements.length;
  for (var i = 0; i < total; i++) {
    new MediaElementPlayer(mediaElements[i]);
  }
});

console.log("hello");
