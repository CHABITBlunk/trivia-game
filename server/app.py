import csv
import random
from flask import Flask, render_template, request, redirect, url_for, session
from game_logic import *

# List of questions
questions = load_questions("server\questions.csv")

# Each player Object
players = {}

# Current question index
question_index = 0

app = Flask(__name__)


@app.route("/config", methods=["POST"])
def config():
    """config screen"""
    config_data = request.json
    player_name = config_data["name"]
    operation = config_data["operation"]
    duration = config_data["duration"]
    intensity = config_data["intensity"]

    if player_name in players:
        players[player_name].pi_shock_setting = (operation, duration, intensity)
        return "Player found"
    else:
        return "Player not found"


app.route("/player_select", methods=["GET", "POST"])


def player_select():
    """select player"""
    # Store Player Information
    pass


def turn_announcement():
    """see whose turn it is"""
    # See who turn it is and display it
    return render_template("turn_announcement.html", player_id="Insert_id_here")


@app.route("/question", methods=["GET"])
def question():
    """question screen"""
    if question_index < len(questions):
        current_question = question[question_index]
        response = {
            "data": {
                "question": current_question["question"],
                "answer": current_question["answer"],
                "correct": current_question["correct"],
                "ended": False,
            }
        }
    else:
        response = {"data": {"ended": True}}
    return  ####


@app.route("/shock_user", methods=["GET"])
def shock_user():
    global current_player
    if current_player in players:
        player = players[current_player]
        send_pi_shock_command(player.pi_shock_code, *player.pi_shock_setting)
        return "Command Sent"
    else:
        return "Player not found"


@app.route("/scoring")
def scoring():
    """send scores"""
    return render_template("scoring.html", scores=session.get("player_scores", {}))


@app.route("/end_game", methods=["POST"])
def end_game():
    """end game, send scores"""

    return redirect(url_for("scoring"))


if __name__ == "__main__":
    app.run(debug=True)
