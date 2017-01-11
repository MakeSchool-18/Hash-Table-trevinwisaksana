# Imported Flask class
from flask import Flask, jsonify, url_for
# Imported Request methods
from flask import request
# Imported JSON
import json
# Importing sentence creator
from word_probability import sentence_creator, distribution_creator
# Importing dict_histogram and tuple_histogram
from word_frequency import dict_histogram, tuple_histogram


''' Creating an instance of Flask class.
    The first argument is the module
    or package name. '''
app = Flask(__name__)

# New sentence
sentence_created = []


# Just for testing if the GET request works
@app.route('/')
def testing():
    return "Hello, how are you?"


# Produces a sentence using a POST request
@app.route('/generate-sentence', methods=["POST"])
def generate_new_sentence():
    # input_json contains the text
    input_json = request.get_json(force=True)
    stringified_input = json.dumps(input_json['text'])
    histogram = dict_histogram(stringified_input)
    distribution = distribution_creator(histogram)
    # sentence_creator recieves the input_json which generates
    # a sentence containing 5 words.
    sentence = sentence_creator(distribution, 5)
    sentence_created.append(sentence)
    return "Sentence created"


# Produces a sentence using a POST request
@app.route('/generate-sentence', methods=["GET"])
def get_new_sentence():
    # Used to contain the converted dictionary into strings.
    # returned_sentence = []
    # Loops through every element in the listOfJSON array
    for i in sentence_created:
        # Appending the converted JSON into string into the list
        # returned_sentence.append(json.dumps(i))
        # Seperating each dictionary in array using ','
        return json.dumps(i)


if __name__ == '__main__':
    app.run(debug=True)
