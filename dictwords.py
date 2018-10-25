#!/usr/bin/env python3
# dictwords.py
# generate a random selection of words from the dictionary

import random
import sys

def random_words(num_words):
    words = ''

    # get our lucky numbers
    lucky_numbers = []
    for i in range(num_words):
        lucky_numbers.append(random.randint(0, 235886))

    dictionary = open('/usr/share/dict/words', 'r')
    line_num = 0

    # read through the dictionary
    lucky_numbers.sort()
    for number in lucky_numbers:
        found = False
        while found != True:
            if number == line_num:
                words += dictionary.readline()
                found = True
            else:
                dictionary.readline()
            line_num += 1
        

    return words

if __name__ == '__main__':
    num_words = int(sys.argv[1])
    output = random_words(num_words=num_words)
    output = output.replace('\n', ' ')
    print(output)

    import timeit
    setup = 'from __main__ import random_words'
    print(timeit.timeit('random_words(num_words=10)', setup=setup, number=100))