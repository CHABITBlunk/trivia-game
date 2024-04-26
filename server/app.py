import csv
import random
from flask import Flask, render_template, request, redirect, url_for, session
from game_logic import *

# List of questions

questions = []

# Current question index
question_index = 0

# Each player Object
players = {}

app = Flask(__name__)

@app.route("/config", methods=["GET", "POST"])
def config():
    """config screen"""
    if request.method == "POST":
        # Save Pishock Setting and move to player select
        return redirect(url_for("player_select"))
    return render_template("config.html")


app.route("/player_select", methods=["GET", "POST"])
def player_select():
    """select player"""
    # Store Player Information
    pass


def turn_announcement():
    """see whose turn it is"""
    # See who turn it is and display it
    return render_template("turn_announcement.html", player_id="Insert_id_here")


@app.route("/question", methods=["GET", "POST"])
def question():
    """question screen"""
    if request.method == "POST" and "end_game" in request.form:
        # If request to end game, redirect to scoring page
        return redirect(url_for("scoring"))

    # *** STILL NEED TO BE DONE***

    # Display the question and answers

    # No More question go to scoring


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
