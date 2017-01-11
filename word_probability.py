# Importing the dict_histogram function
from word_frequency import dict_histogram, tuple_histogram
# Importing random
import random

# Modify the Shuffle method to:
# Be able to pick more the words with higher probabilities

# Function that chooses a random index.
def random_index(text):
    rand_index = random.randint(0, len(text) - 1)
    return rand_index

'''
SUDO CODE:
# We know the word frequency.
# Create a list that will put the repeated words consecutively
# Loop through the list to:
    # Use an random index picker
    # Append that to a list
    # Return that list
'''


# Probability based shuffler chooses words based on probability.
def probability_using_word_repositioning(number_of_words_in_sentence, source_of_text):
    # List that contains the new random words.
    probability_based_word_list = []
    # Assigning the value of dict_histogram to text_dict
    text_dict = dict_histogram(source_of_text)
    # Basically making the dictionary a list
    # Converting the list because it lays out the same words beside each other.
    # This is useful when the randomizor picks the word as it has a higher
    # probability of being picked.
    dictionary_convereted_to_list = [value for value, count in text_dict.items() for i in range(count)]
    # Loop as much as the user wants the sentence length to be.
    for word in range(0, number_of_words_in_sentence):
        # Get a random index from the dictionary_convereted_to_list
        random_word_index = random_index(dictionary_convereted_to_list)
        # Append the words to the probability_based_word_list
        probability_based_word_list.append(dictionary_convereted_to_list[random_word_index])
    # Returning the list
    return probability_based_word_list


# Using probability to find pick the most probable words.
def distribution_creator(histogram):
    """
    From e.g. [("Hello", 1),("You", 4),("No", 3),("Lol", 5)]
    Becomes e.g. [("Hello", 1),("You", 5),("No", 8),("Lol", 13)]
    """
    distribution = []
    new_value = 0
    for key, value in histogram.items():
        # Incrementing the upper range value based on the word count
        new_value = new_value + value
        # Appending to the distribution array
        distribution.append((key, new_value))
    return distribution


# Chooses a random word based on frequency
def distribution_word_picker(distribution):
    # Total number of words in text
    number_of_words = distribution[-1][1]
    # Getting a random number betweeen 1 to the total number of words
    random_word_index = random.randint(1, number_of_words)
    # Looping through every tuple in distribution array
    print(random_word_index)
    print(distribution)
    for word in distribution:
        if random_word_index <= word[1]:
            # print("RANDOM NUMBER: ", random_word_index)
            # print("WORD CODE ================ ", word[1])
            # Getting the word based on the words with larger range
            random_word = word[0]
            # Appending just the word (using random_word only
            # will print (word, number)) therefore using random_word[0]
            # will just append the word into the sentence array.
            return random_word


# Creates a sentence with X amount of words
def sentence_creator(distribution, number_of_types_in_sentence):
    # Used to remove punctuations
    # punctuations = ["!", "(", ")", "-", "[", "]", "{", "}", ";", ":", "'", "<", ">", ".", "?"]
    # Array that will contain a list of words
    sentence = []
    # Looping through the number of words the user wants to have in the sentence.
    for word in range(0, number_of_types_in_sentence):
        random_word = distribution_word_picker(distribution)
        sentence.append(random_word)
    return sentence


if __name__ == "__main__":
    # Opening the source text which is Beawulf.txt
    source_text = open("Fish.txt", "r")
    # histogram contains a list of key value pairs
    histogram = dict_histogram(source_text)
    # new_distribution contains the distribution
    new_distribution = distribution_creator(histogram)
    # 5 words picked to form a new sentence
    new_sentence = sentence_creator(new_distribution, 5)
    # printing sentence
    print(new_sentence)
