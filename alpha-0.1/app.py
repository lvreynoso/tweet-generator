#!/usr/bin/env python3
# app.py
import sampling
import frequency

from flask import Flask 
app = Flask(__name__)

# setup
source_path = 'crime_and_punishment.txt'
with open(source_path, 'r') as file:
    source = file.read()
source_histogram = frequency.histogram_tuples(source_text = source)

@app.route('/')
def index():
    sentence = ''
    for i in range(10):
        sentence += ' ' + sampling.random_word(source_histogram)
    return sentence