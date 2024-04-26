"""backend game logic"""

import random
import requests
import csv  # Need this for csv.DictReader

# Game logic functions


# Reads from CSV and assigns it into the questions
# Must be in format question, answer1, answer2, (optional)answer3, (optional)answer4, numeric which one is correct
# Returns a dictionary of questions


def load_questions(file_path):
    """Reads CSV and returns a dictonary of question and the index of the correct answer"""
    questions = []

    with open(file_path, newline="") as csvfile:
        file = csv.DictReader(csvfile)
        for row in file:
            # List to hold the answers
            answers = []

            # Iterate through possible answer index
            for i in range(1, 5):
                question_answers = "answer" + str(i)
                if question_answers in row:
                    answers.append(row[question_answers])

            question_answer = {
                "question": row["question"],
                "answers": answers,
                "correct": row["correct"],
            }
            questions.append(question_answer)
    return questions


def shuffle_questions(questions):
    """Input a question dictionary and shuffle them"""
    random.shuffle(questions)
    return questions


# Players is the array of player object, Name of player, What answer the user entered
# Question that was given. Updates player score information and return if the answer was
# Correct or not.


def check_answer(players, name, given_answer, question):
    """checks answer and updates score."""

    # What is the correct answer
    index_correct = int(question["correct"]) - 1
    index_of_player = None
    is_correct = False

    # Find which index is the current player
    for index, player in enumerate(players):
        if players["player_name"] == name:
            index_of_player = index

    # Check if user inputed correct answer
    if question["answer"][index_correct] == given_answer:
        # If correct increment players score
        players[index_of_player]["player_score"] += 1
        is_correct = True
    else:
        # If Incorrect increcement number of incorrect
        players[index_of_player]["num_incorrect"] += 1

    return is_correct


def check_game_end_conditions(index, questions, playertermination):
    """check for conditions on which a game ends"""
    # How many Question nare there
    number_of_question = len(questions)

    # Game ends if all question have been asked or player terminates early
    # Increment the number of question after question is asked
    if index >= number_of_question - 1 or playertermination:
        return True
    else:
        return False


def clear_all_player_info(players):
    """clears all player info"""
    players.clear()


# Operations

# The shock collar included with PiShock has three operations: shock, vibrate, and beep.
# You specify the operation using the Op variable.
# Key 	Value 	Operation
# Op 	0 	Shock
# Op 	1 	Vibrate
# Op 	2 	Beep

# Key 	Value Type 	Example 	Description
# Op 	integer 	0 	Activate the shock function.
# Duration integer (1-15): An integer representing the number of seconds to shock the wearer
# Intensity integer (1-100) An integer representing the intensity of shock


def send_pi_shock_command(self, op, duration, intensity=None):
    """sends command to pishock"""
    payload = {
        "Username": self.username,
        "Apikey": self.apikey,
        "Code": self.code,
        "Name": self.name,
        "Op": op,
        "Duration": duration,
    }
    if intensity is not None:
        payload["Intensity"] = intensity

    response = requests.post(self.base_url, json=payload, headers=self.headers)
    print(response.text)


def terminate_game():
    """ends game. TODO: implement"""
    pass


def resets_game():
    """reset game to default state. TODO: implement"""
    pass


def reuse_player_config(player_id):
    """reuses player config if player wants to keep it. TODO: implement"""
    pass


def play_sound():
    """plays sound. TODO: implement"""
    pass


def test_pi_shock(player_id):
    """test if pishocks working. TODO: implement"""
    pass


def log_game_event(event):
    """log game events. TODO: implement"""
    pass
