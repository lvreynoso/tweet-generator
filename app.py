#!/usr/bin/env python3
# app.py
# main script, uses other modules to generate sentences

import cleanup
import tokenate
import word_count
import sample

from flask import Flask 
app = Flask(__name__)

# setup
source = ''
source_path = 'crime_and_punishment.txt'
with open(source_path, 'r') as file:
    source = file.read()
clean_source = cleanup.alphanumericize(source_text=source)
tokens = tokenate.generate(source_text=clean_source)
source_map = sample.markov_path(token_list=tokens)

@app.route('/')
def index():
    sentence = sample.markov_walk(path=source_map, distance=10)
    return sentence

if __name__ == '__main__':
    # print('(X) ERROR\nThis program has performed an illegal operation and will be shut down.')
    # print('Do not move. Your IP has been traced and the Internet Police are on their way.')
    print(source_map)