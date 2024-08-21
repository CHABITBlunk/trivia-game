import random
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_cors import CORS
from game_logic import send_pi_shock_command, load_questions

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# List of questions
questions = load_questions("./questions.csv")

# Each player Object
players = {
    "habit": {"name": "habit", "pi_shock_setting": {}, "pi_shock_code": "2C48E5F36C4"}
}

# Current question index
question_index = 0


@app.route("/config", methods=["POST"])
def config():
    """Config screen."""
    config_data = request.json
    player_name = config_data["name"]
    operation = config_data["operation"]
    duration = config_data["duration"]
    intensity = config_data["intensity"]

    if player_name in players:
        players[player_name].update(
            {"operation": operation, "duration": duration, "intensity": intensity}
        )
        return (
            jsonify({"status": "success", "message": "Player configuration updated"}),
            200,
        )
    return jsonify({"status": "failure", "message": "Player not found"}), 404


@app.route("/beep", methods=["GET"])
def beep():
    """Beep pishock."""
    name = request.args.get("name")
    if name in players:
        send_pi_shock_command(players[name]["pi_shock_code"], 2, 1)
        return jsonify({"status": "success", "message": "Beep triggered"}), 200
    return jsonify({"status": "failure", "message": "Player not found"}), 404


@app.route("/question", methods=["GET"])
def question():
    """Question screen."""
    global question_index
    if question_index < len(questions):
        current_question = questions[question_index]
        question_index += 1  # Move to next question
        return jsonify(current_question), 200
    else:
        return jsonify({"ended": True}), 200


@app.route("/shock_user", methods=["GET"])
def shock_user():
    """Shock user."""
    name = request.args.get("name")
    if name in players:
        player = players[name]
        send_pi_shock_command(
            player["pi_shock_code"],
            0,
            1,
            20,
        )
        return jsonify({"status": "success", "message": "Shock sent"}), 200
    return jsonify({"status": "failure", "message": "Player not found"}), 404


if __name__ == "__main__":
    app.run(host="192.168.224.226", port=5000, debug=True)
