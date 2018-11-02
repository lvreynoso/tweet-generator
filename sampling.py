#!/usr/bin/env python3
# sampling.py

import random
import sys
import frequency

# non-weighted
def random_word(histogram):
    random_word = ''
    random_index = random.randrange(len(histogram))
    random_word += histogram[random_index][0]
    return random_word

# the easy way
def weighted_random_word_choices(histogram):
    random_word = ''
    population = []
    weights = []
    for entry in histogram:
        population.append(entry[0])
        weights.append(entry[1])
    random_word += ''.join(random.choices(population = population, weights = weights, k = 1))
    return random_word

# the hard way
# we are going to add up all the weights, pick a number at random between 1 and the sum of
# the weights, and then subtract words (and their weights) until we get to less than zero.
# algorithm from https://medium.com/@peterkellyonline/weighted-random-selection-3ff222917eb6
def weighted_random_word(histogram):
    random_word = ''
    sum_of_weights = 0
    for entry in histogram:
        sum_of_weights += entry[1]
    random_weight = random.randrange(sum_of_weights)
    index = 0
    while random_weight >= 0:
        random_word = histogram[index][0]
        random_weight -= histogram[index][1]
        index += 1
    return random_word

def test_randomness(histogram):
    test_words = ''
    for i in range(10000):
        test_words += ' ' + weighted_random_word(histogram = histogram)
    test_histogram = frequency.histogram_counts(test_words)
    num_top_words = 25
    index = len(test_histogram) - 1
    while num_top_words > 0 and index >= 0:
        # our 'inverse' histogram has entries like so: (650, [apple, orange]) etc.
        for entry in test_histogram[index][1]:
            if num_top_words > 0:
                printline = entry + ' = '
                printline += str(test_histogram[index][0])
                print(printline)
                num_top_words -= 1
        index -= 1
        


if __name__ == '__main__':
    source_path = sys.argv[1]
    with open(source_path, 'r') as file:
        source = file.read()
    source_histogram = frequency.histogram_tuples(source_text = source)
    word = weighted_random_word(histogram = source_histogram)
    print(word)
    print('-----------')
    test_randomness(source_histogram)