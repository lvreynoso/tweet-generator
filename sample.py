#!/usr/bin/env python3
# sample.py
# module for generating a sample word from a histogram

import dictogram
import queue
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
    starting_items = []
    for n in range(order):
        starting_items.append(token_list[n])

    state_tracker = queue.Queue(size=order, items=starting_items)
    state = tuple(state_tracker.items())
    markov_map[state] = dictogram.Dictogram()

    for index in range(order, len(token_list)):
        new_token = token_list[index]
        state_tracker.enqueue(new_token)
        new_state = tuple(state_tracker.items())
        if new_state not in markov_map:
            markov_map[new_state] = dictogram.Dictogram()
        markov_map[state].add_count(new_state)
        state = new_state
    return markov_map

def markov_walk(path, distance, start_stop_tokens):
    sentence = ''
    START_TOKEN = start_stop_tokens[0]
    STOP_TOKEN = start_stop_tokens[1]

    # find a key with a start token in it
    # keys = path.keys()
    # found = False
    # index = 0
    # starting_items = []
    # while not found and index < len(keys):
    #     key = keys[index]
    #     if START_TOKEN == key[0]:
    #         starting_items = keys[index]
    #         found = True
    #     index += 1

    # state_tracker = queue.Queue(size=order, items=START_TOKEN)
    state = (START_TOKEN)

    for step in range(distance):
        # step through the queue
        current_word = state[0]
        # add another word to the queue
        if current_word == START_TOKEN:
            # choose a random tuple from the markov map with a START token in it
            keys = list(path.keys())
            start_states = []
            for entry in keys:
                if START_TOKEN == entry[0]:
                    start_states.append(entry)
            state = random.choice(start_states)
            # advance so the first item in the tuple is not a START token
            set_of_possibities = path[state]
            state = word(set_of_possibities)
            # voila, our starting word of this new sentence
            current_word = state[0]
            current_word = current_word.capitalize()
            
        set_of_possibities = path[state]
        state = word(set_of_possibities)

        # if current_word == START_TOKEN:
        #     # choose a random word from the dictionary
        #     current_word = random.choice(list(path.keys()))
        #     current_word = current_word.capitalize()
        # else:
        #     set_of_possibities = path[current_word]
        #     current_word = word(set_of_possibities)
        # properly write out start and stop tokens
        if current_word == STOP_TOKEN:
            sentence += '.'
        else:
            if current_word == 'i':
                sentence += ' ' + current_word.upper()
            else: 
                sentence += ' ' + current_word
    return sentence


