#!/usr/bin/env python3
# cleanup.py
# module for cleaning up source text

import string

def alphanumericize(source_text):
    source = source_text.lower()
    source = source.replace('-', ' ') # because Dostoevsky loves his dashes
    
    # I think this is backwards - I should instead filter all but alphanumerics. But Crime & Punishment has
    # an expanded character set due to its use of phrases in other languages, and digraphs.
    translate_table = str.maketrans(dict.fromkeys(string.punctuation + '\u201c\u201d\u2018\u2019'))
    text = source.translate(translate_table)
    
    return text