# #!/usr/bin/env python3
# rearrange words

import random
import sys


def rearrange_words(sampler):
    indices_used = []  # to track indices used
    random_arrangement = ''
    for i in range(len(sampler)):
        random_index = 0
        unique_random = False
        # get a random index, then check if it unisque
        while unique_random == False:
            random_index = random.randrange(len(sampler))
            unique_random = random_index not in indices_used
        indices_used.append(random_index)
        random_arrangement += sampler[random_index] + ' '
    return random_arrangement

if __name__ == '__main__':
    args = sys.argv[1:]
    print(rearrange_words(args))
