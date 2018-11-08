#!/usr/bin/env python3
# sample.py
# module for generating a sample word from a histogram

import random

def word(histogram):
    words = histogram.keys()
    weights = histogram.values()
    random_word = ''
    sum_of_weights = 0

    for weight in weights:
        sum_of_weights += weight
    random_weight = random.randrange(sum_of_weights)

    index = 0
    while random_weight >= 0:
        random_word = words[index]
        random_weight -= weights[index]
        index += 1
    
    return random_word