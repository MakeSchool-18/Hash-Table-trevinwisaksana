

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
source_text = open("Fish.txt", "r")

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
# returns {'blue': 1, 'fish': 4, 'two': 1, 'red': 1, 'one': 1}
def dict_histogram(text):
    # Entire text
    entire_splitted_text = text.read().split()
    # Dictionary that contains the new word
    word_dict = {}
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


# A function that uses tuples as a word frequency counter.
def tuple_histogram(text):
    # Entire text
    entire_splitted_text = text.read().split()
    # List that contains the new word
    word_list_of_tuples = []
    # Stores the word count
    word_frequency = 0
    # New key value pair
    new_word_frequency = 0  # A tuple
    # For each word in the list of words
    for word in word_list_of_tuples:
        print("Used")
        # Change the words to lowecase letters
        word = word.lower()
        # Check if word has been counted already
        if word in word_list_of_tuples[0]:
            word_frequency = word[1]  # Finding its current count
            new_word_frequency = word_frequency + 1
            self.set(word, new_word_frequency)
        else:
            # If not, add a new key value pair
            word_list_of_tuples.append((word, 1))
    return word_list_of_tuples


# Set method to update a tuple
def set(self, key, value):
    """Insert or update the given key with its associated value"""
    # TODO: Insert or update the given key-value entry into a bucket
    key_value = (key, value)  # Store tuple containing key and value in key_value
    list_of_tuples = self.word_list_of_tuples[key]

    if list_of_tuples.find(lambda (tuple_key, _): tuple_key == key):  # If the tuple_key matches the key
        self.delete(key)  # Removing the key from the list
        return True

    list_of_tuples.append(key_value)  # Append the new tuple
    return True


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
    # testing = tuple_histogram(source_text)
    print(testing)
