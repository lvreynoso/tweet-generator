#!/usr/bin/env python3
# word_count.py
# module for generating histograms from a list of tokens

import dictogram

def generate(token_list):
    histogram = dictogram.Dictogram(token_list)
    return histogram