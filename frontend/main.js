// start of game, only render start
$(document).ready(() => {
  $(".div").not(".start").hide();
});

// show help
$(".js-help").on("click", () => {
  console.log("test");
  $(".start").hide();
  $(".help").show();
});

// show pishock config
$(".js-pishock-config").on("click", () => {
  console.log("test");
  $(".start").hide();
  $(".pishock-config").show();
});
