// start of game, only render start
$(document).ready(() -> {
  $(".start").not().hide();
});

// show help
$(".js-help").on("click", () -> {
  $(".start").hide();
  $(".help").show();
});

// show pishock config
$(".js-pishock-config").on("click", () -> {
  $(".start").hide();
  $(".pishock-config").show();
});
