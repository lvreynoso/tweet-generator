#!/usr/bin/env python3
# frequency.py
# word frequency analysis script
# i love dictionaries

import string
import json

def histogram(source_text):
    # initialize our empty dictionary
    histogram_dictionary = {}
    # strip all punctuation from the file
    source = source_text
    source = source.replace('-', ' ')
    translate_table = str.maketrans(dict.fromkeys(string.punctuation))
    source = source.translate(translate_table)
    # split the source text into words (splits on whitespace)
    # then iterate through each word
    for word in source.split():
        unique_word = word.lower()
        if unique_word in histogram_dictionary:
            histogram_dictionary[unique_word] += 1
        else:
            histogram_dictionary[unique_word] = 1

    return histogram_dictionary

def unique_words(histogram):
    number_of_uniques = len(list(histogram))
    return number_of_uniques

def frequency(word, histogram):
    unique_word = word.lower()
    word_frequency = 0
    if type(histogram) == dict:
        word_frequency = histogram[unique_word]
    elif type(histogram) == list:
        # if we have a list, iterate through the list until we find our word
        # then check the value
        not_found = True
        index = 0
        while not_found and index < len(histogram):
            if histogram[index][0] == unique_word:
                word_frequency = histogram[index][1]
                not_found = False
            else:
                index += 1
    return word_frequency

def histogram_lists(source_text):
    histogram_list = []
    # split the source into words (splits on whitespace)
    # strip all punctuation from the file
    source = source_text
    # need to figure out a comprehensive translation table
    source = source.lower().replace('-', ' ').replace('\u201c', '').replace('\u201d', '').replace('\u2018', '').replace('\u2019', '')
    translate_table = str.maketrans(dict.fromkeys(string.punctuation))
    source = source.translate(translate_table)
    text = source.split()
    # sort the list of words, then count the number of unique words.
    # we start by looking at the word at the end of the list,
    # and then check if the penultimate word is the same, and the 
    # word before that, etc. until we get a different word.
    # we keep a count of words that are the same, and when we get
    # a different word we append the word and the count to our
    # histogram list, then we delete all the list entries at the
    # end we just counted!
    text.sort()
    while len(text) > 0:
        count = 0
        samesies = True
        index = len(text) - 1
        word = text[index]
        while samesies and index >= 0:
            if word == text[index]:
                count += 1
                index -= 1
            else:
                samesies = False
        histogram_list.append([word, count])
        del text[-(count):]
    return histogram_list

def histogram_tuple(source_text):
    histogram_tuples = []
    # strip all punctuation from the file
    source = source_text
    source = source.replace('-', ' ')
    translate_table = str.maketrans(dict.fromkeys(string.punctuation))
    source = source.translate(translate_table)
    text = source.lower().split()
    # same algorithm as above
    text.sort()
    while len(text) > 0:
        count = 0
        samesies = True
        index = len(text) - 1
        word = text[index]
        while samesies and index >= 0:
            if word == text[index]:
                count += 1
                index -= 1
            else:
                samesies = False
        histogram_tuples.append((word, count))
        del text[-(count):]
    return histogram_tuples

def histogram_counts(source_text):
    # implemented using a dictionary where the values are lists
    histogram_counts = {}
    # strip all punctuation from the file
    source = source_text
    source = source.replace('-', ' ')
    translate_table = str.maketrans(dict.fromkeys(string.punctuation))
    source = source.translate(translate_table)
    text = source.lower().split()
    # same algorithm as above
    text.sort()
    while len(text) > 0:
        count = 0
        samesies = True
        index = len(text) - 1
        word = text[index]
        while samesies and index >= 0:
            if word == text[index]:
                count += 1
                index -= 1
            else:
                samesies = False
        # this time we check if the *count* is in the dictionary,
        # and if so we append our word to the count; if not we create
        # the dictionary key and a new value, which is a list containing
        # our word
        if count in histogram_counts:
            histogram_counts[count].append(word)
        else:
            histogram_counts[count] = [word]
        del text[-(count):]
    return histogram_counts

def save_histogram(histogram, output_file):
    json.dump(histogram, output_file)


if __name__ == '__main__':
    # open our file and transfer it to memory
    with open('crime_and_punishment.txt', 'r') as file:
        source = file.read()
    # make the histogram
    source_histogram = histogram_lists(source_text = source)
    source_unique_words = unique_words(histogram = source_histogram)
    mystery_frequency = frequency(word = 'mystery', histogram = source_histogram)
    sonia_frequency = frequency(word = 'Sonia', histogram = source_histogram)
    murder_frequency = frequency(word = 'murder', histogram = source_histogram)
    # result
    print('{} unique words. The word \'mystery\' appears {} times, the word \'Sonia\' \n{} times, and the word \'murder\' {} times.'.format(source_unique_words, mystery_frequency, sonia_frequency, murder_frequency))
    with open('histogram.txt', 'w') as histogram_file:
        save_histogram(histogram = source_histogram, output_file = histogram_file)
    print('Histogram saved as histogram.txt.')
