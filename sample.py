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

def markov_path(token_list, order):
    markov_map = {}
    previous = []
    for n in range(order):
        previous.append(token_list[n])
    previous = tuple(previous)
    for token in token_list:
        if token not in markov_map:
            markov_map[token] = dictogram.Dictogram()
        markov_map[previous_word].add_count(token)
        previous_word = token
    return markov_map

def markov_walk(path, distance, start_stop_tokens):
    sentence = ''
    START_TOKEN = start_stop_tokens[0]
    STOP_TOKEN = start_stop_tokens[1]
    current_word = START_TOKEN
    for step in range(distance):
        if current_word == START_TOKEN:
            # choose a random word from the dictionary
            current_word = random.choice(list(path.keys()))
            current_word = current_word.capitalize()
        else:
            set_of_possibities = path[current_word]
            current_word = word(set_of_possibities)
        # properly write out start and stop tokens
        if current_word == STOP_TOKEN:
            sentence += '.'
        elif current_word != START_TOKEN:
            if current_word == 'i':
                sentence += ' ' + current_word.upper()
            else: 
                sentence += ' ' + current_word
            current_word = current_word.lower()
    return sentence


