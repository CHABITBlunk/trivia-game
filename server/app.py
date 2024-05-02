import random
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_cors import CORS, cross_origin
from game_logic import send_pi_shock_command, load_questions

__name__ = "main"

# List of questions
questions = load_questions("./questions.csv")

# Each player Object
players = {
    "habit": {"name": "habit", "pi_shock_setting": {}, "pi_shock_code": "2C48E5F36C4"}
}

# Current question index
question_index = 0

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config["CORS_LOG"] = True


@app.route("/config", methods=["POST"])
def config():
    """config screen"""
    config_data = request.json
    player_name = config_data["name"]
    operation = config_data["operation"]
    duration = config_data["duration"]
    intensity = config_data["intensity"]

    if player_name in players:
        players[player_name]["operation"] = operation
        players[player_name]["duration"] = duration
        players[player_name]["intensity"] = intensity
        return "Player found"
    return "Player not found"


@app.route("/beep", methods=["GET"])
def beep():
    """beep pishock"""
    current_player = request.json["name"]
    send_pi_shock_command(players[current_player]["pi_shock_code"], 2, 1)
    response = jsonify({"status": "success", "message": "Request successful"})
    response.headers["Content-Type"] = "application/json"
    return response


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
        current_question = questions[question_index]
        # question_index += 1
        response = {
            "question": current_question["question"],
            "answers": current_question["answers"],
            "correct": current_question["correct"],
            "ended": False,
        }
    else:
        response = {"data": {"ended": True}}
    return response


@app.route("/shock_user", methods=["GET"])
def shock_user():
    current_player = request.json["name"]
    if current_player in players:
        player = players[current_player]
        send_pi_shock_command(
            player["pi_shock_code"],
            player["operation"],
            player["duration"],
            player["intensity"],
        )
        response = jsonify({"status": "success", "message": "Request successful"})
        response.headers["Content-Type"] = "application/json"
    else:
        response = jsonify({"status": "failure", "message": "Request failure"})
        response.headers["Content-Type"] = "application/json"
    return response


if __name__ == "main":
    app.run(host="192.168.224.157", debug=True)
