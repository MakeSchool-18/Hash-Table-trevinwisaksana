import re

text_file = open("Main Corpus.txt", "r")

def main(text):

    pretty_text = re.sub(r'[^\w\s]', ' ', text.read())
    print pretty_text

    editted_corpus = open("Main Corpus.txt", "w")
    editted_corpus.write(pretty_text)

if __name__ == "__main__":
    main(text_file)
