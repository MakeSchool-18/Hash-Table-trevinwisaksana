

"""
A histogram() function which takes a source_text argument
(can be either a filename or the contents of the file as a string, your choice)
and return a histogram data structure that stores each unique word along with
the number of times the word appears in the source text.

A unique_words() function that takes a histogram argument and returns the total
count of unique words in the histogram. For example, when given the histogram
for The Adventures of Sherlock Holmes, it returns the integer 8475.

A frequency() function that takes a word and histogram argument and returns the
number of times that word appears in a text. For example, when given the word
"mystery" and the Holmes histogram, it will return the integer 20.
"""

# Opening the source text which is Beawulf.txt
source_text = open("Test Corpus.txt", "r")

# Contains a list of repeated words
repeated_words_list = []
# repeated_words_list = [[] for i in range(0, len(entire_text))]

# An function that stores counts the word frequency using lists.
def list_histogram(text):
    # Reading and splitting the words to be selectable.
    entire_text = text.read().split()
    print(entire_text)
    # For loop through each object in array.
    for new_word in entire_text:
        # Bool
        already_appended = False
        # Lowercasing the new word
        new_word = new_word.lower()
        # any_word = entire_text[i]
        # If a word from entire_text matches with a word in repeated_words_list
        for word_num_list in repeated_words_list:
            if new_word == word_num_list[0]:
                word_num_list[1] += 1
                already_appended = True
        # If we don't use the if statement, it would still append the added numbered array.
        # e.g. there will be three [of, 1]'s such as [of, 1], [of, 2], [of, 3].
        if already_appended is False:
            repeated_words_list.append([new_word, 1])
            print("New array")
    print(repeated_words_list)


# A function that uses dictionaries as a word frequency counter.
def dict_histogram(text):
    # Entire text
    entire_splitted_text = text.read().split()
    # Dictionary that contains the new word
    word_dict = {}
    # Counter contains the int for the frequency
    # word_frequency = 0
    # Loops through each word in the entire text
    for word in entire_splitted_text:
        # Removing all the capital letters from words.
        word = word.lower()
        # Going to every word and makes the Value 1 because it's the first word there.
        if word in word_dict.keys():
            # If the word matches a dictionary key, then append the Value by 1
            word_dict[word] += 1
        else:
            # If not, add a new key value pair to the dictionary
            word_dict[word] = 1
    return word_dict

'''
SUDO CODE:
# Loop through the words that are in the entire_text
# If there are words that matches, add it to an existing array
  with the same word
# If the it doesn't match with any other word, create a new array
# Count the number of words within each nested array to get the frequency and
  unique words
# If the words are used less than 5 times, they are unique
# If not, they are are commonly used words
'''

if __name__ == "__main__":
    testing = dict_histogram(source_text)
