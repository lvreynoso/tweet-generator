#!/usr/bin/env python3
# frequency.py
# word frequency analysis script
# i love dictionaries

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

def unique_words(histogram):
    number_of_uniques = len(list(histogram))
    return number_of_uniques

def frequency(word, histogram):
    word_frequency = 0
    if type(histogram) == dict:
        word_frequency = histogram[word]
    elif type(histogram) == list:
        # if we have a list, iterate through the list until we find our word
        # then check the value
        not_found = True
        index = 0
        while not_found and index < len(histogram):
            if histogram[index][0] == word:
                word_frequency = histogram[index][1]
                not_found = False
            else:
                index += 1
    return word_frequency

def histogram_lists(source_text):
    histogram_list = []
    # split the source into words (splits on whitespace)
    text = source_text.split()
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
        while samesies and index > 0:
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
    text = source_text.split()
    # same algorithm as above
    text.sort()
    while len(text) > 0:
        count = 0
        samesies = True
        index = len(text) - 1
        word = text[index]
        while samesies and index > 0:
            if word == text[index]:
                count += 1
                index -= 1
            else:
                samesies = False
        histogram_tuples.append((word, count))
        del text[-(count):]
    return histogram_tuples


if __name__ == '__main__':
    # open our file and transfer it to memory
    file = open('crime_and_punishment.txt', 'r')
    source = file.read()
    # strip all punctuation from the file
    translate_table = str.maketrans(dict.fromkeys(string.punctuation))
    source = source.translate(translate_table)
    # make the histogram
    source_histogram = histogram_lists(source_text = source)
    source_unique_words = unique_words(histogram = source_histogram)
    mystery_frequency = frequency(word = 'mystery', histogram = source_histogram)
    sonia_frequency = frequency(word = 'Sonia', histogram = source_histogram)
    murder_frequency = frequency(word = 'murder', histogram = source_histogram)
    # result
    # print('{} unique words.'.format(source_unique_words))
    print('{} unique words. The word \'mystery\' appears {} times, the word \'Sonia\' \n{} times, and the word \'murder\' {} times.'.format(source_unique_words, mystery_frequency, sonia_frequency, murder_frequency))

