import re

text_file = open("Main Corpus.txt", "r")

def main(text):

    pretty_text = re.sub(r'[^\w]', ' ', text.read())

    '''editted_corpus = open("Main Corpus.txt", "w")
    editted_corpus.write(processed_result)'''

if __name__ == "__main__":
    main(text_file)
