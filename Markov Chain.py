import random


class Markov(object):

    def __init__(self, open_file, chain_size=3):
        self.chain_size = chain_size
        self.cache = {}
        self.open_file = open_file.read()
        self.words = self.open_file.split()
        self.word_size = len(self.words)
        self.database()

    def database(self):
        for chain_set in self.chains():
            # print(type(chain_set)) # Type Tuple
            # print(type(self.chains())) # Type Generator
            key = chain_set[:self.chain_size - 1]
            next_word = chain_set[-1]  # Last item in the array
            if key in self.cache:
                self.cache[key].append(next_word)
            else:
                self.cache[key] = [next_word]

    def chains(self):
        """Generates chains from the given data string based on passed chain size."""
        for i in range(len(self.words) - self.chain_size - 1):
            yield tuple(self.words_at_position(i))

    def words_at_position(self, i):
        """Uses the chain size to find a list of the words at an index."""
        chain = []
        for chain_index in xrange(0, self.chain_size):
            chain.append(self.words[i + chain_index])
            # print self.words[i + chain_index]
        return chain

    def generate_markov_text(self, size=15):
        seed = random.randint(0, self.word_size - 3)  # Get random number
        # print(self.words_at_position(1))
        gen_words = []
        seed_words = self.words_at_position(seed)[:-1]  # Everything on list except for the last one
        gen_words.extend(seed_words)  # Merges the two lists together
        for i in xrange(size):  # xrange basically uses yield, which makes it more efficient
            last_word_len = self.chain_size - 1
            # print(last_word_len)
            last_words = gen_words[-1 * last_word_len:] # Always 2
            # print(type(gen_words))
            next_word = random.choice(self.cache[tuple(last_words)])
            # print(next_word)
            # print(tuple(last_words))
            gen_words.append(next_word)
        return ' '.join(gen_words)

if __name__ == '__main__':
    corpus = open('Main Corpus.txt')
    mrkv = Markov(corpus)
    print(mrkv.generate_markov_text())
