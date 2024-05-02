// TODO: find raspberry pi ip and put it at the beginning of each axios request url
let ended = true;
let numCorrect = 0,
  numIncorrect = 0;
let name = "";
$(document).ready(() => {
  // start of game, only render start
  $("div").not(".start").hide();

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

  // start game
  $(".js-start-game").on("click", () => {
    $("div").not(".game").hide();
    $(".game").show();
    $(".game__player-name").text(`Name: ${name}`);
    $(".game__player-score").text(`Score: ${numCorrect}`);
    appendQuestion();
    // axios request for a question. TODO: test tomorrow
    axios
      .get("http://192.168.224.157:5000/question")
      .then((response) => {
        ended = response.data.ended;
        console.log(response);
        if (ended) {
          $("div").not(".end-game").hide();
          $(".end-game").show();
          $(".js-num-correct").text(`Number correct: ${numCorrect}`);
          $(".js-num-incorrect").text(`Number incorrect: ${numIncorrect}`);
        } else {
          $(".game__problem").append(
            createQuestion(
              response.data.question,
              response.data.answers,
              response.data.correct,
            ),
          );
        }
      })
      .catch((error) => {
        $(".game__problem").append("<p>Error: problem did not load</p>");
      });
  });

  // test pishock beep
  $(".pishock-config__beep").on("click", () => {
    axios
      .get(
        "http://192.168.224.157:5000/beep",
        { name: name },
        {
          headers: {
            "Content-Type": "application/json",
          },
          withCredentials: true,
        },
      )
      .then((response) => {
        alert("success!");
        console.log(response);
      })
      .catch((error) => {
        alert("error");
        console.log(error);
      });
  });

  // test pishock settings
  $(".pishock-config__test").on("click", () => {
    axios
      .get(
        "http://192.168.224.157:5000/shock_user",
        {
          name: name,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
          withCredentials: true,
        },
      )
      .then((response) => {
        alert("success!");
        console.log(response);
      })
      .catch((error) => {
        alert("error");
        console.log(error);
      });
  });

  // send pishock config to backend after clicking save button
  $(".js-save").on("click", () => {
    name = $(".pishock-config__name").val();
    axios
      .post(
        "http://192.168.224.157:5000/config",
        {
          name: $(".pishock-config__name").val(),
          operation: $(".pishock-config__operation").val(),
          duration: $(".pishock-config__duration").val(),
          intensity: $(".pishock-config__intensity").val(),
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
          withCredentials: true,
        },
      )
      .then((response) => {
        alert("successfully saved!");
      })
      .catch((error) => {
        console.log(error);
      });
  });

  // continue after submitting
  $(".continue").on("click", () => {
    if (ended) {
      $("div").not(".end-game").hide();
      $(".end-game").show();
      $(".js-num-correct").text(`Number correct: ${numCorrect}`);
      $(".js-num-incorrect").text(`Number incorrect: ${numIncorrect}`);
    } else {
      $("div").not(".game").hide();
      $("game").show();
      $(".game__problem").clear();
      appendQuestion(); // TODO: switch this with the axios request once we test
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
const appendQuestion = (
  question = "What is 2+2?",
  answers = ["5", "4", "3", "Unsure"],
  correct = "4",
) => {
  $(".game__problem").show();
  let html = `<form class="question"> <p class="p game__problem__question">${question}</p>`;
  shuffle(answers);
  answers.forEach((answer) => {
    html += `<label for="${answer}">${answer}</label>`;
    html += `<input type="radio" name="answer" id="${answer === correct ? "correct" : "incorrect"}" class="game__problem__answer" value="${answer}" />`;
  });
  html += `<input type="submit" value="Submit answer" />`;
  $(".game__problem").append(html);
  $(".question").show();

  // submit answer click logic
  $(".question").on("submit", (event) => {
    event.preventDefault();
    if ($("#correct").is(":checked")) {
      console.log("correct");
      numCorrect++;
      $("div").not(".correct").hide();
      $(".correct").show();
    } else if ($("#incorrect").is(":checked")) {
      console.log("incorrect");
      numIncorrect++;
      $("div").not(".incorrect").hide();
      $(".incorrect").show();
      // make http request to shock user
      axios.get("http://192.168.224.157:5000/shock_user", {
        name: name,
      });
    }
    // clear quesetion after submit
    $(".game__problem").empty();
  });
};
