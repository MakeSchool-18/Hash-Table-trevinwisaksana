# -*- coding: utf-8 -*-
import re

text_file = open("Main Corpus.txt", "r")

def main(text):

    delete_chapter_regex = 'C\w*\s\d\.\s+'
    delete_comma_regex = ','
    delete_underscore_regex = '_'
    delete_question_mark_regex = '\?'
    delete_quotation_mark_regex = r'[\“\”]'
    delete_exclamation_mark_regex = '\!'

    pretty_text = re.sub(delete_exclamation_mark_regex, '', text.read())

    editted_corpus = open("Main Corpus.txt", "w")
    editted_corpus.write(pretty_text)

if __name__ == "__main__":
    main(text_file)
