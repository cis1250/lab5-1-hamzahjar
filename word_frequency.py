#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

import re

def get_sentence():
    user_sentence = input("Enter a sentence: ")

    while (is_sentence(user_sentence) == False):
        print("This does not meet the criteria for a sentence.")
        user_sentence = input("Enter a sentence: ")
    return user_sentence


def calculate_frequencies(sentence):
    words = sentence.split()

    unique_words = []
    frequencies = []

    for word in words:
        cleaned_word = re.sub(r'[^\w\s]', '', word).lower()

        if cleaned_word in unique_words:
            index = unique_words.index(cleaned_word)
            frequencies[index] += 1
        else:
            unique_words.append(cleaned_word)
            frequencies.append(1)

    return unique_words, frequencies


def print_frequencies(words, frequencies):
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")


def main():
    user_sentence = get_sentence()
    unique_words, frequencies = calculate_frequencies(user_sentence)
    print_frequencies(unique_words, frequencies)


main()
