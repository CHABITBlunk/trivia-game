$(document).ready(() => {
  // start of game, only render start
  $(".div").not(".start").hide();

  // show help
  $(".js-help").on("click", () => {
    $("div").not(".help").hide();
    $(".help").show();
  });

  // show pishock config
  $(".js-pishock-config").on("click", () => {
    $("div").not(".pishock-config").hide();
    $(".pishock-config").show();
  });

  // return home
  $(".js-return-start").on("click", () => {
    $("div").not(".start").hide();
    $(".start").show();
  });
});
