#!/usr/bin/env python3
# reverse words or sentences

import random
import sys


def reverse_words(input_array):
    output_array = []
    for item in input_array:
        playstring = ''
        for i in range(0, len(item)):
            playstring += item[len(item) - 1 - i]
        output_array.append(playstring)
    return output_array


def reverse_sentences(input_array):
    reversed_array = reverse_words(input_array)
    output_string = ''
    for i in range(0, len(reversed_array)):
        output_string += reversed_array[len(reversed_array) - 1 - i] + ' '
    return output_string

param = sys.argv[1]
inputs = sys.argv[2:len(sys.argv)]
if param == '-w':
    word_array = reverse_words(input_array=inputs)
    output = ''
    for item in word_array:
        output += item + ' '
    print(output)
elif param == '-s':
    output = reverse_sentences(inputs)
    print(output)
else:
    print(
        'Unrecognized argument \'{}\'. Use \'-w\' to reverse words, or \'-s\' to reverse sentences.'.format(sys.argv[1]))
