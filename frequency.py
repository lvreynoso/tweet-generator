#!/usr/bin/env python3
# frequency.py
# word frequency analysis script
# i love dictionaries

import string
import json

def alphanumericize(source_text):
    source = source_text.lower()
    source = source.replace('-', ' ') # because Dostoevsky loves his dashes
    # I think this is backwards - I should instead filter all but alphanumerics. But Crime & Punishment has
    # an expanded character set due to its use of phrases in other languages, and digraphs.
    translate_table = str.maketrans(dict.fromkeys(string.punctuation + '\u201c\u201d\u2018\u2019'))
    text = source.translate(translate_table)
    return text

def histogram(source_text):
    # initialize our empty dictionary
    histogram_dictionary = {}
    # strip all punctuation from the file
    source = alphanumericize(source_text)
    # split the source text into words (splits on whitespace)
    # then iterate through each word
    for word in source.split():
        if word in histogram_dictionary:
            histogram_dictionary[word] += 1
        else:
            histogram_dictionary[word] = 1

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
            if unique_word in histogram[index]:
                word_frequency = histogram[index][1]
                not_found = False
            else:
                index += 1
    return word_frequency

def histogram_lists(source_text):
    histogram_list = []
    # split the source into words (splits on whitespace)
    # strip all punctuation from the file
    source = alphanumericize(source_text)
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

def histogram_tuples(source_text):
    histogram_tuple = []
    # strip all punctuation from the file
    source = alphanumericize(source_text)
    text = source.split()
    # this algorithm just keeps track of 'runs' of the same word,
    # then when it encounters a different word, appends what it has 
    # as a tuple to our histogram_tuple list. since the text is 
    # sorted, this will cover every case.
    text.sort()
    index = 0
    word = text[0]
    count = 0
    while index < len(text):
        if word == text[index]:
            count += 1
            index += 1
        else:
            histogram_tuple.append((word, count))
            word = text[index]
            count = 1
            index += 1
        if index == len(text): # for our last item
            histogram_tuple.append((word, count))
    return histogram_tuple

def histogram_counts(source_text):
    # implemented using a list of lists, this function returns an inverted histogram
    # where words are grouped together in a list with a count as follows:
    # [[1, [fish, blue]], [2, [red, dinosaur]], ...] etc.
    histogram_counts = []
    # strip all punctuation from the file
    source = alphanumericize(source_text)
    text = source.split()
    # same algorithm as list of lists histogram
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
        # this time it's different
        counted = False
        for entry in histogram_counts:
            if entry[0] == count:
                entry[1].append(word)
                counted = True
        if counted == False:
            histogram_counts.append([count, [word]]) 
        del text[-(count):]
    histogram_counts.sort()
    return histogram_counts

def save_histogram(histogram, output_file):
    json.dump(histogram, output_file)


if __name__ == '__main__':
    # open our file and transfer it to memory
    with open('crime_and_punishment.txt', 'r') as file:
        source = file.read()
    # make the histogram
    source_histogram = histogram_tuples(source_text = source)
    source_unique_words = unique_words(histogram = source_histogram)
    fourteen_frequency = frequency(word = '14', histogram = source_histogram)
    mystery_frequency = frequency(word = 'mystery', histogram = source_histogram)
    sonia_frequency = frequency(word = 'Sonia', histogram = source_histogram)
    murder_frequency = frequency(word = 'murder', histogram = source_histogram)
    eternelle_frequency = frequency(word = '\u00e9ternelle', histogram = source_histogram)
    # result
    print('{} unique words. The word \'14\' appears {} times, the word \'mystery\' appears \n{} times, the word \'Sonia\' {} times, the word \'murder\' {} times, and the \nword \'\u00e9ternelle\' {} times.'.format(source_unique_words, fourteen_frequency, mystery_frequency, sonia_frequency, murder_frequency, eternelle_frequency))
    with open('histogram.txt', 'w') as histogram_file:
        save_histogram(histogram = source_histogram, output_file = histogram_file)
    print('Histogram saved as histogram.txt.')
