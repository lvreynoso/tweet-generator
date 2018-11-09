#!/usr/bin/env python3
# sample.py
# module for generating a sample word from a histogram

import dictogram
import random

def word(histogram):
    random_word = ''
    sum_of_weights = sum(histogram.values())
    random_weight = random.randrange(sum_of_weights)

    for key, value in histogram.items():
        if random_weight - value < 0:
            random_word = key
            break
        else:
            random_weight -= value
    
    return random_word

def markov_path(token_list):
    markov_map = {}
    previous_word = None
    for token in token_list:
        if token not in markov_map:
            markov_map[token] = dictogram.Dictogram()
        if previous_word is not None:
            markov_map[previous_word].add_count(token)
        previous_word = token
    return markov_map

def markov_walk(path, distance):
    sentence = ''
    current_word = None
    for step in range(distance):
        if current_word is None or len(path[current_word]) == 0:
            # choose a random word from the dictionary
            current_word = random.choice(list(path.keys()))
            sentence += ' ' + current_word
        else:
            set_of_possibities = path[current_word]
            next_word = word(set_of_possibities)
            sentence += ' ' + next_word
            current_word = next_word
    return sentence