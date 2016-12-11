import re

text_file = open("Main Corpus.txt", "r")

def main(text):

    delete_chapter_regex = 'C\w*\s\d\.\s+'

    pretty_text = re.sub(delete_chapter_regex, '', text.read())

    editted_corpus = open("Main Corpus.txt", "w")
    editted_corpus.write(pretty_text)

if __name__ == "__main__":
    main(text_file)
