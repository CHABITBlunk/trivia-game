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

  // send pishock config to backend after clicking save button
  $(".js-save").on("click", () => {
    axios
      .post("/user/pishock-config", {
        operation: $(".pishock-config-operation").val(),
        duration: $(".pishock-config-duration").val(),
        intensity: $(".pishock-config-intensity").val(),
      })
      .then((response) => {
        console.log("successful", response.data);
      })
      .catch((error) => {
        console.log("error", error);
      });
  });

  // start game
  $(".js-start-game").on("click", () => {
    $("div").not(".game").hide();
    $(".game").show();
    // axios request for a question
    axios
      .get("/game/question")
      .then((response) => {})
      .catch((error) => {});
  });
});

// create the html for a problem, including question and answers
const createQuestion = (question, answers, correctAnswer) => {
  return `<p class="p game__problem__question">${question}</p>`;
};
