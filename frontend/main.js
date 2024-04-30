// start of game, only render start
$(document).ready(() => {
  $(".div").not(".start").hide();
});

// show help or pishock config
$(".js-help").on("click", "p", () => {
  if (this.className.contains("js-help")) {
    console.log($(this).text());
    $(".start").hide();
    $(".help").show();
  } else {
    console.log($(this).text());
    $(".start").hide();
    $(".pishock-config").show();
  }
});
