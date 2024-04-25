import requests


# Game logic functions


def check_game_end_conditions():
    pass


# Get Random Question
def get_random_question():
    pass


"""

Operations 

The shock collar included with PiShock has three operations: shock, vibrate, and beep. You specify the operation using the Op variable.
Key 	Value 	Operation
Op 	0 	Shock
Op 	1 	Vibrate
Op 	2 	Beep

Key 	Value Type 	Example 	Description
Op 	integer 	0 	Activate the shock function.
Duration 	integer (1 - 15) 	2 	An integer representing the number of seconds to shock the wearer. Must be between 1 and 15.
Intensity 	integer (1 - 100) 	7 	An integer representing the intensity of shock. Must be between 1 and 100.


"""


# Sends Command to Pishock
def send_pi_shock_command(self, op, duration, intensity=None):
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


# Ends Game
def terminate_game():
    pass


# Reset Game to default state
def resets_game():
    pass


# Clears Player info
def clear_player_info(player_id):
    if player_id in player_select:
        del players[player_id]


# Reuses player configuration if user want to keep it
def reuse_player_config(player_id):
    pass


# Plays a sound
def play_sound():
    pass


# Test if Pishocks are working
def test_pi_shock(player_id):
    pass


# Check Answers and updates score
def check_answer(player_id, given_answer):
    pass


# Shuffles Questions
def shuffle_questions():
    random.shuffle(questions)


# Log game events
def log_game_event(event):

    pass
