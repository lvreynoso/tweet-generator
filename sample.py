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
        markov_map[state].add_count(new_token)
        state = new_state
    return markov_map

def markov_walk(path, distance, start_stop_tokens, order):
    # tbd
    sentence = ''
    START_TOKEN = start_stop_tokens[0]
    STOP_TOKEN = start_stop_tokens[1]

    state_queue = queue.Queue(size=order)

    # get our first Markov state. find all the keys that start with
    # a START token, then randomly select from them
    keys = list(path.keys())
    starting_possibilities = []
    for key in keys:
        if key[0] == START_TOKEN:
            starting_possibilities.append(key)
    state = random.choice(starting_possibilities)
    for token in state:
        state_queue.enqueue(token)

    # now walk the path
    for step in range(distance):
        # save the queue state
        state = tuple(state_queue.items())
        # step through the queue
        current_word = state_queue.dequeue()
        # add another word to the queue
        if current_word == START_TOKEN:
            # Uncomment for random sentence jumping. I like its output more.
            keys = list(path.keys())
            starting_possibilities = []
            for key in keys:
                if key[0] == START_TOKEN:
                    starting_possibilities.append(key)
            state = random.choice(starting_possibilities)
            for token in state:
                state_queue.enqueue(token)
            state = tuple(state_queue.items())
            current_word = state_queue.dequeue()
            # START tokens aren't written, so we need to advance by another token
            set_of_possibities = path[state]
            next_token = word(set_of_possibities)
            state_queue.enqueue(next_token)
            state = tuple(state_queue.items())
            current_word = state_queue.dequeue()
            current_word = current_word.capitalize()
        # enqueue our next token
        set_of_possibities = path[state]
        next_token = word(set_of_possibities)
        state_queue.enqueue(next_token)

        # properly write out start and stop tokens
        if current_word == STOP_TOKEN:
            sentence += '.'
        else:
            if current_word == 'i':
                sentence += ' ' + current_word.upper()
            else: 
                sentence += ' ' + current_word
    return sentence


