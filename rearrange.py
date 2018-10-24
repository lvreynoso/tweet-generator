# #!/usr/bin/env python3
# rearrange words

import random
import sys


def rearrange_words():
    sampler = sys.argv[1:len(sys.argv)]
    indices = []
    random_arrangement = []
    for i in range(0, len(sampler) - 1):
        random_index = 0
        unique_random = False
        while unique_random == False:
            random_index = random.randint(0, len(sampler) - 1)
            unique_random = True
            for index in indices:
                if index == random_index:
                    unique_random = False
        indices.append(random_index)
        random_arrangement.append(sampler[random_index])
    # the easy way
    # random_arrangement = random.sample(sampler, k=len(sampler))
    return random_arrangement

if __name__ == '__main__':
    shuffled = rearrange_words()
    print(shuffled)
