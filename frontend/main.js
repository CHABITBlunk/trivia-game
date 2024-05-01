const axios = require("axios");

// TODO: find ip address to and put it at the beginning of each axios request url

$(document).ready(() => {
  // start of game, only render start
  $(".div").not(".start").hide();

  let ended = true;
  let numCorrect = 0,
    numIncorrect = 0;
  let name = "";

  // show help
  $(".js-help").on("click", () => {
    $(".div").not(".help").hide();
    $(".help").show();
  });

  // show pishock config
  $(".js-pishock-config").on("click", () => {
    $(".div").not(".pishock-config").hide();
    $(".pishock-config").show();
  });
  // return home
  $(".js-return-start").on("click", () => {
    $(".div").not(".start").hide();
    $(".start").show();
  });

  // continue after submitting
  $(".continue").on("click", () => {
    if (ended) {
      $(".div").not(".end-game").hide();
      $(".end-game").show();
      $(".js-num-correct").text(`Number correct: ${numCorrect}`);
      $(".js-num-incorrect").text(`Number incorrect: ${numIncorrect}`);
    } else {
      $(".div").not(".game").hide();
      $("game").show();
      $(".game__problem .question:first").remove();
      appendQuestion(); // TODO: switch this with the axios request once we test
    }
  });

  // send pishock config to backend after clicking save button
  $(".js-save").on("click", () => {
    name = $(".pishock-config__name").val();
    axios
      .post("/pishock-config", {
        name: $(".pishock-config__name").val(),
        operation: $(".pishock-config__operation").val(),
        duration: $(".pishock-config__duration").val(),
        intensity: $(".pishock-config__intensity").val(),
      })
      .then((response) => {
        alert("successfully saved!");
      })
      .catch((error) => {
        console.log(error);
      });
  });

  // start game
  $(".js-start-game").on("click", () => {
    $(".div").not(".game").hide();
    $(".game").show();
    $(".game__player-name").text(`Name: ${name}`);
    appendQuestion();
    // axios request for a question. TODO: test tomorrow
    /*
    axios
      .get("/question")
      .then((response) => {
        $(".game__problem").append(
          createQuestion(
            response.data.question,
            response.data.answers,
            response.data.correct,
            response.data.ended,
          ),
        );
      })
      .catch((error) => {
        $(".game__problem").append("<p>Error: problem did not load</p>");
      });
    */
    // submit answer
    $(".js-submit-answer").on("click", () => {
      if ($(".game__problem__answer:checked").attr("id") == "correct") {
        $(".div").not(".correct").hide();
        $(".correct-answer").show();
      } else {
        $(".div").not(".incorrect").hide();
        $(".incorrect").show();
        // make http request to shock user
        axios.get("/shock");
      }
    });
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
const appendQuestion = (
  question = "What is 2+2?",
  answers = ["5", "4", "3", "Unsure"],
  correct = "4",
) => {
  let html = `<div class="question"> <p class="p game__problem__question">${question}</p>`;
  shuffle(answers);
  answers.forEach((answer) => {
    html += `<input type="radio" id="${answer === correct ? "correct" : "incorrect"}" class="game__problem__answer" value="${answer}" />`;
  });
  html += `<button class="btn js-submit-answer">Submit answer</button> </div>`;
  $(".game__problem").append(html);
};
