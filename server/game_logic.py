"""backend game logic"""

import random
import requests
import csv  # Need this for csv.DictReader

# Game logic functions


def load_questions(file_path):
    """
    Reads CSV from the specified file path and contructs a list of dictionaries.
    Each representing a question and it's assocated answers. CSV File must be in a specific format
    with columns name 'question','answer1','answer2' and optionally 'answer3', 'answer4'. At the end there must be a
    'correct column indicating which index is the correct answer (Index 0 is 1

    Parameters:
    -file_path(str): Path to the CSV file containing the questions and answers.

    Returns:
    -list[dict]: A list of dictionaries, where each of the dictionary has keys:
    -'question' (str): The questions text
    -'answer list[str]: a list of answer options
    -'correct': int the index of the correct answer ub the 'answer' list (starting at 1 )

    """

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


def check_game_end_conditions(index, questions, playertermination):
    """

    Evaluates whether the game should end based on current question or player action.
    Game ends if all question have been asked or if the player chooses to terminate the game early

    Parameters:
    -index(int): Current index of the question being asked. The first question is at index 0
    -questions(list): a list of question dictionaries, where each dictionary represents a question and the answer
    -player_termination (bool): A boolean flag indicating whethere the plater has chosen to end the game

    Returns:
    -bool: True if the game should end (based on described conditions), otherwise false

    """

    number_of_question = len(questions)

    if index >= number_of_question - 1 or playertermination:
        return True
    else:
        return False


def send_pi_shock_command(self, op, duration, intensity=None):
    """

    Sends a command to PiShock device to perform one of the three options: shock, vibrate, or beep,
    based on the operations code. The function creates a payload with operations parameters and send it as a POST
    request to the PiShock's API ( https://apidocs.pishock.com/ )

    Parameters:
    -op(int): The Operation code that determins the action to be performed by the PiShock
        - 0: Shock
        - 1: Vibrate
        - 2: Beep
    -duration(int): The duration in seconds for the operation above. Must be between 1 - 15 seconds.
    -intensity (int): The intesity of the operation, only applicable during the shock operation.
    Must be between 1-100. Default is None, which is ignored on operation operation other than shock.

    """
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


# Repopulation Question, and maybe keep player / pishock info
def resets_game(players, keep_config, pishock_config, questions):
    """

    Resets the game based on users choice.

    If 'keep_config' is True, reseting players scores and questions are reshuffed
    for the next game. All PiShock setting and player information is retained

    If 'keep_config' is False, all player data and PiShockConig objects
    are cleared

    """

    if keep_config:
        # Reseting only scores and incorrect answers and reshuffling questions
        for player in player.values():
            player.player_score = 0
            player.num_incorrect = 0
        random.shuffle(questions)
    else:
        # Clears all config data
        players.clear()
        pishock_config.username = ""
        pishock_config.apikey = ""
        pishock_config.code = ""
