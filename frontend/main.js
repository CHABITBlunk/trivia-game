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
      .post("/pishock-config", {
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
      .get("/question")
      .then((response) => {
        $(".game__problem").append(
          createQuestion(
            response.data.question,
            response.data.answers,
            response.data.correct,
            response.data.ended
          ),
        );
      })
      .catch((error) => {
        $(".game__problem").append("<p>Error: problem did not load</p>");
      });
  });

  // submit answer
  $(".js-submit-answer").on("click", () => {
    if ($(".game__problem__answer:checked").attr("id") == "correct") {
      $("div").not(".correct-answer").hide();
      $(".correct-answer").show();
    } else {
      $("div").not(".incorrect-answer").hide();
      $(".incorrect-answer").show();
      // make http request to shock user
    }
  });
});

// fisher-yates shuffle
const shuffle = (array) => {
  let i = array.length;
  while (i != 0) {
    let ri = Math.floor(Math.random() * i);
    i--;
    [array[i], array[ri]] = [array[ri], array[i]];
  }
};

// create the html for a problem, including question and answers
// HACK: gave default values for question
const createQuestion= (question = "What is 2+2?", answers = {"5", "4", "3", "Unsure"}, correct = "4") => {
  let output = `<p class="p game__problem__question">${question}</p>`;
  shuffle(answers);
  answers.map((answer) => {
    output += `<input type="radio" id="${answer === correct ? "correct" : "incorrect"}" class="game__problem__answer" value="${answer}" />`;
  });
  output += `<button class="btn js-submit-answer">Submit answer</button>`;
  return output;
};
