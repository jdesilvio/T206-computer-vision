import os
import numpy as np

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

        RESULTS_ARRAY = []

        # get url
        image_url = request.form.get('img')

        try:

            # initialize the image descriptor
            cd = ColorDescriptor((8, 12, 3))

            # load the query image and describe it
            from skimage import io
            import cv2
            query = io.imread(image_url)
            query = (query * 255).astype("uint8")
            (r, g, b) = cv2.split(query)
            query = cv2.merge([b, g, r])
            features = cd.describe(query)

            # perform the search
            searcher = Searcher(INDEX)
            results = searcher.search(features)

            # loop over the results, displaying the score and image name
            for (score, resultID) in results:
                RESULTS_ARRAY.append(
                    {"image": str(resultID), "score": str(score)})

            # return success
            return jsonify(results=(RESULTS_ARRAY[::-1][:3]))

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
