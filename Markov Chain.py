import random


class Markov(object):

    def __init__(self, open_file, chain_size=3):
        self.chain_size = chain_size  # How many words are in the key
        self.cache = {}
        self.open_file = open_file.read()
        self.words = self.open_file.split()
        self.word_size = len(self.words)
        self.database()  # Generates a list of key value pairs

    def database(self):
        # chain_set is Type Tuple
        for chain_set in self.chains():  # self.chains() is Type Generator as it returns a generator
            key = chain_set[:self.chain_size - 1]  # A tuple that contains the current word and the word next to it
            next_word = chain_set[-1]  # Last item in the the chain_set or the next word
            if key in self.cache:  # If the key is already in the dictionary
                self.cache[key].append(next_word)  # Appends the next word to the list
                # self.cache contains ('for', 'it'): ['is']
            else:
                self.cache[key] = [next_word]  # If it doesn't exist, set the key to the next word

    def chains(self):
        """Generates chains from the given data string based on passed chain size.
        ('since.', 'He', 'was')
        (He', 'was', 'charming.')
        """
        for i in xrange(len(self.words) - self.chain_size - 1):  # Loops 461743 times
            yield tuple(self.words_at_position(i))  # Uses a generator that creates the example on top

    def words_at_position(self, i):
        """Uses the chain size to find a list of the words at an index."""
        chain = []  # Contains the list of words
        for chain_index in xrange(0, self.chain_size):  # Iterates from 0-2
            chain.append(self.words[i + chain_index])  # Appends the current word and word after
        return chain

    def generate_markov_text(self, size=15):
        seed = random.randint(0, self.word_size - 3)  # Get random number based on word size
        gen_words = []  # Contains the list of words
        seed_words = self.words_at_position(seed)[:-1]  # Chooses a random key and takes everything but the last word
        gen_words.extend(seed_words)  # Merges the seed_words and gen_words together
        for i in xrange(size):  # xrange basically uses yield, which makes it more efficient
            last_word_len = self.chain_size - 1  # Always 2
            last_words = gen_words[-1 * last_word_len:]  # Takes the second from last word
            next_word = random.choice(self.cache[tuple(last_words)])  # Uses the last words as a key
            gen_words.append(next_word)
        return ' '.join(gen_words)

if __name__ == '__main__':
    corpus = open('Main Corpus.txt')
    mrkv = Markov(corpus)
    print(mrkv.generate_markov_text())
