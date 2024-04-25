from flask import Flask, render_template, request, redirect, url_for, session
from game_logic import *
import csv
import random

# List of questions

questions = []

# Current question index
question_index = 0

# Each player Object
players = {}

app = Flask(__name__)


# Intro Screen
@app.route("/")
def index():
    return render_template("intro.html")


# Help Screen
@app.route("/help")
def help():
    return render_template("help.html")


# Configuration Screen
@app.route("/config", methods=["GET", "POST"])
def config():
    if request.method == "POST":
        # Save Pishock Setting and move to player select
        return redirect(url_for("player_select"))
    return render_template("config.html")


# Player Select Screen
app.route("/player_select", methods=["GET", "POST"])


def player_select():
    # Store Player Information
    if request.method == "POST":
        return redirect(url_for("turn_announcement"))
    return render_template("player_select.html")


# Turn Announcement Screen
def turn_announcement():
    # See who turn it is and display it
    return render_template("turn_announcement.html", player_id="Insert_id_here")


# Question Screen
@app.route("/question", methods=["GET", "POST"])
def question():

    if request.method == "POST" and "end_game" in request.form:
        # If request to end game, redirect to scoring page
        return redirect(url_for("scoring"))

    # *** STILL NEED TO BE DONE***

    # Display the question and answers

    # No More question go to scoring


# Scoring Page
@app.route("/scoring")
def scoring():
    # Display scores and other game end details
    return render_template("scoring.html", scores=session.get("player_scores", {}))


# Rarly termination and and redirect to scoring
@app.route("/end_game", methods=["POST"])
def end_game():

    return redirect(url_for("scoring"))


if __name__ == "__main__":
    app.run(debug=True)
