#!/usr/bin/env python3
# frequency.py
# word frequency analysis script

import string

def histogram(source_text):
    # initialize our empty dictionary
    histogram_dictionary = {}
    # split the source text into words (splits on whitespace)
    # then iterate through each word
    for word in source_text.split():
        if word in histogram_dictionary:
            histogram_dictionary[word] += 1
        else:
            histogram_dictionary[word] = 1

    return histogram_dictionary
    # do stuff

def unique_words(histogram):
    # list(histogram) returns a list of dictionary keys.
    # then all we have to do is check the length of the list!
    number_of_uniques = len(list(histogram))
    return number_of_uniques
    # do stuff

def frequency(word, histogram):
    word_frequency = histogram[word]
    return word_frequency
    # do stuff


if __name__ == '__main__':
    # open our file and transfer it to memory
    file = open('crime_and_punishment.txt', 'r')
    source = file.read()
    # strip all punctuation from the file
    translate_table = str.maketrans(dict.fromkeys(string.punctuation))
    source = source.translate(translate_table)
    # make the histogram
    source_histogram = histogram(source_text = source)
    source_unique_words = unique_words(histogram = source_histogram)
    mystery_frequency = frequency(word = 'mystery', histogram = source_histogram)
    sonia_frequency = frequency(word = 'Sonia', histogram = source_histogram)
    murder_frequency = frequency(word = 'murder', histogram = source_histogram)
    # result
    print('{} unique words. The word \'mystery\' appears {} times, the word \'Sonia\' \n{} times, and the word \'murder\' {} times.'.format(source_unique_words, mystery_frequency, sonia_frequency, murder_frequency))

