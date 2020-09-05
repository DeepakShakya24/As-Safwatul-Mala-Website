$(function () {
  "use strict";

  var winH = $(window).height();

  $("header, .slide").height(winH);
});
$(function () {
  $("ul.nav a").bind("click", function (event) {
    event.preventDefault();
    var $anchor = $(this);
    console.log($anchor.attr("href"));
    $("html, body")
      .stop()
      .animate(
        {
          scrollTop: $($anchor.attr("href")).offset().top,
        },
        1000
      );
    event.preventDefault();
  });
});
$(function () {
  $(document).scroll(function () {
    var $nav = $(".navbar-fixed-top");
    $nav.toggleClass("scrolled", $(this).scrollTop() > $nav.height());
  });
});
