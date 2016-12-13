import random

class Markov(object):

	def __init__(self, open_file, chain_size=5):
		self.chain_size = chain_size # chain is used to
		self.cache = {} # Cache used to contain the key value pairs
		self.open_file = open_file # Assigns the corpus to the open_file
		self.words = self.file_to_words() # Storing the converted .txt into a variable
		self.word_size = len(self.words) # Storing the length of the corpus into a variable
		self.database() # 

	def file_to_words(self): # Converts the .txt into Strings
		self.open_file.seek(0) # Opens the .txt from the beginning
		data = self.open_file.read() # Stores the .
		words = data.split()
		return words

	def words_at_position(self, i):
		"""Uses the chain size to find a list of the words at an index."""
		chain = []
		for chain_index in range(0, self.chain_size):
			chain.append(self.words[i + chain_index])
		return chain

	def chains(self):
		"""Generates chains from the given data string based on passed chain size.
		So if our string were:
			"What a lovely day"
		With a chain size of 3, we'd generate:
			(What, a, lovely)
		and
			(a, lovely, day)
		"""

		if len(self.words) < self.chain_size:
			return

		for i in range(len(self.words) - self.chain_size - 1):
			yield tuple(self.words_at_position(i))

	def database(self):
		for chain_set in self.chains():
			key = chain_set[:self.chain_size - 1]
			next_word = chain_set[-1]
			if key in self.cache:
				self.cache[key].append(next_word)
			else:
				self.cache[key] = [next_word]

	def generate_markov_text(self, size=25):
		seed = random.randint(0, self.word_size - 3)
		gen_words = []
		seed_words = self.words_at_position(seed)[:-1]
		gen_words.extend(seed_words)
		for i in xrange(size):
			last_word_len = self.chain_size - 1
			last_words = gen_words[-1 * last_word_len:]
			next_word = random.choice(self.cache[tuple(last_words)])
			gen_words.append(next_word)
		return ' '.join(gen_words)

if __name__ == '__main__':
    corpus = open('Main Corpus.txt')
    mrkv = Markov(corpus)
    print mrkv.generate_markov_text()
