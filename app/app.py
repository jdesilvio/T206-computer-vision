import os
import numpy as np
from cardsearch.descriptor import CardDescriptor
from cardsearch.matcher import CardMatcher
import cv2
from skimage import io
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Homepage route
@app.route('/')
def index():
    return render_template("index.html")

# search route
@app.route('/search', methods=['POST'])
def search():

    if request.method == "POST":

        # Initialize results array for best matching images
        RESULTS_ARRAY = []

        # Get image url when a click of an image is performed
        image_url = request.form.get('img')

        try:

            # Initialize the image descriptor
            cd = CardDescriptor()

            # Load the query image and describe it
            query = io.imread(image_url)
            # Convert query to grayscale
            gray = cv2.cvtColor(query, cv2.COLOR_BGR2GRAY)
            # Extract the keypoints and descriptors
            (queryKps, queryDescs) = cd.describe(gray)

            # Perform image search
            searcher = CardMatcher(cd)
            # Return search results
            results = searcher.search(queryKps, queryDescs)

            # loop over the results, displaying the score and image name
            for (score, resultID) in results:
                RESULTS_ARRAY.append(
                    {"image": str(resultID), "score": str(score)})

            # return success
            #return jsonify(results=(RESULTS_ARRAY[::-1][:3]))
            #return jsonify(results=(RESULTS_ARRAY[:3]))
            return jsonify(results=(RESULTS_ARRAY[0]))

        except:

            # return error
            jsonify({"sorry": "Sorry, no results! Please try again."}), 500







### Test routes - maybe use later ###

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
