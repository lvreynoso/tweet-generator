#!/usr/bin/env python3
# dictwords.py
# generate a random selection of words from the dictionary

import random
import sys
import linecache

def random_words(num_words):
    words = ''

    # get our lucky numbers
    lucky_numbers = []
    for i in range(num_words):
        lucky_numbers.append(random.randint(0, 235886))

    # dictionary = open('/usr/share/dict/words', 'r')
    line_num = 0

    # read through the dictionary
    for number in lucky_numbers:
        words += linecache.getline('/usr/share/dict/words', number)

    return words

if __name__ == '__main__':
    num_words = int(sys.argv[1])
    output = random_words(num_words=num_words)
    output = output.replace('\n', ' ')
    print(output)