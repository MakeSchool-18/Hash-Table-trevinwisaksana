import random
from word_frequency import dict_histogram

"""
– Use the 'one fish two fish blue fish red fish' example
– Get a list of key, value pairs.
    – The key contains the word, the value contains a histogram or word count
    – Uses a dictionary
– The next word to 'one' is only 'fish'
"""

class Markov_Model(object):

    def __init__(self, open_file, chain_size = 3):
        self.chain_size = chain_size  # How many words are in the key
        self.cache = {}  #
        self.database()  # Generates a list of key value pairs

    def database():  # Takes
