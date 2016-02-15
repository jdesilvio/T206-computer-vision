import os
import numpy as np

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Homepage route
@app.route('/')
def index():
    return render_template("index.html")

# Player route - displays player name
@app.route('/player')
@app.route('/player/<player>')
def player(player="Honus-Wagner"):
    return  "You are looking for {}".format(player)

# Back route - displays brand name on back of card
@app.route('/back')
@app.route('/back/<back>')
def back(back="Lenox"):
    return  "You are looking for the {} back".format(back)

# Card route - displays player name and back combination
@app.route('/card')
@app.route('/card/<player>/<back>')
def card(player="Walter-Johnson", back="Uzit"):
    return "You are looking for {} with a {} back!".format(player, back)

# Run app!
if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
