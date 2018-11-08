#!/usr/bin/env python3
# app.py
# main script, uses other modules to generate sentences

import cleanup
import tokenize
import word_count
import sample

from flask import Flask 
app = Flask(__name__)

# setup
source_path = 'crime_and_punishment.txt'
with open(source_path, 'r') as file:
    source = file.read()
clean_source = cleanup.alphanumericize(source)
tokens = tokenize.generate(clean_source)
histogram = word_count.generate(tokens)

@app.route('/')
def index():
    sentence = ''
    for i in range(10):
        sentence += ' ' + sample.word(histogram)
    return sentence

if __name__ == '__main__':
    print('(X) ERROR\nThis program has performed an illegal operation and will be shut down.')
    print('Do not move. Your IP has been traced and the Internet Police are on their way.')