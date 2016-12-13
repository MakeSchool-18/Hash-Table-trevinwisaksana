# Imported Flask class
from flask import Flask, jsonify, url_for
# Imported Request methods
from flask import request
# Imported JSON
import json
# Importing sentence creator
from word_probability import sentence_creator, distribution_creator


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


# A function that uses dictionaries as a word frequency counter.
def dict_histogram(text):
    # Entire text
    entire_splitted_text = text.split()
    # Dictionary that contains the new word
    word_dict = {}
    # Counter contains the int for the frequency
    # word_frequency = 0
    # Loops through each word in the entire text
    for word in entire_splitted_text:
        # Removing all the capital letters from words.
        word = word.lower()
        # Going to every word and makes the Value 1 because it's the first word
        # there.
        if word in word_dict.keys():
            # If the word matches a dictionary key, then append the Value by 1
            word_dict[word] += 1
        else:
            # If not, add a new key value pair to the dictionary
            word_dict[word] = 1
    return word_dict

if __name__ == '__main__':
    app.run(debug=True)
