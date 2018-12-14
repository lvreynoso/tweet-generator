#!/usr/bin/env python3
# cleanup.py
# module for cleaning up source text

import string

def alphanumericize(source_text, start_stop_tokens):
    START_TOKEN = start_stop_tokens[0]
    STOP_TOKEN = start_stop_tokens[1]
    source = source_text.lower()
    # because Dostoevsky loves his dashes
    source = source.replace('-', ' ')
    source = START_TOKEN + ' ' + source.replace('.', ' ' + STOP_TOKEN + ' ' + START_TOKEN + ' ')
    
    # I think this is backwards - I should instead filter all but alphanumerics. But Crime & Punishment has
    # an expanded character set due to its use of phrases in other languages, and digraphs.
    translate_table = str.maketrans(dict.fromkeys(string.punctuation + '\u201c\u201d\u2018\u2019'))
    text = source.translate(translate_table)
    
    return text