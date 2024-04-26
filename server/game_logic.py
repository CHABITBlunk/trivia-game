"""backend game logic"""
import random
import requests

# Game logic functions

def check_game_end_conditions():
    """check for conditions on which a game ends"""
    pass


def get_random_question():
    """get a random question and serve it to the frontend"""
    pass


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
        "Op": op, "Duration": duration,
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


def clear_player_info(player_id):
    """clears player info"""
    if player_id in player_select:
        del players[player_id]


def reuse_player_config(player_id):
    """reuses player config if player wants to keep it. TODO: implement"""
    pass


def play_sound():
    """plays sound. TODO: implement"""
    pass


def test_pi_shock(player_id):
    """test if pishocks working. TODO: implement"""
    pass


def check_answer(player_id, given_answer):
    """checks answer and updates score. TODO: implement"""
    pass


def shuffle_questions():
    """shuffles questions"""
    random.shuffle(questions)


def log_game_event(event):
    """log game events. TODO: implement"""
    pass
