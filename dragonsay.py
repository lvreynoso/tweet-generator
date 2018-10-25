#!/usr/bin/env python3
# wow much dragon many say
# ASCII art from https://asciiart.website/index.php?art=creatures/dragons
# Accessed October 23, 2018

import sys
import string

def format_forty(input_quote):

    split_quote = input_quote.splitlines()
    format_quote = ''

    # take out all the newline chars in the quote
    for index in range(0, len(split_quote)):
        format_quote += split_quote[index]
        if index != len(split_quote) - 1:
            format_quote += ' '

    space_indices = []
    newline_indices = []
    output_quote = ''

    # find all the spaces in the quote
    for index in range(0, len(format_quote)):
        if format_quote[index] == ' ':
            space_indices.append(index)

    # the number of newlines we will need
    # should be 'good enough'
    lines = int(len(format_quote) / 35)

    # choose the spaces to insert newline characters in.
    for num in range(1, lines + 1):
        target = num * 35
        newline_index = 0
        for index in range (0, len(space_indices) - 1):
            # just assign every index below the target to the newline index.
            # the last one that meets our criteria will be what ends up
            # getting pushed, and it's what we want anyways.
            if space_indices[index] < target:
                newline_index = space_indices[index]
        newline_indices.append(newline_index)

    # insert the newline characters
    for index in range(0, len(format_quote)):
        output_quote += format_quote[index]
        for number in newline_indices:
            if number == index:
                output_quote += '\n'

    # replace tabs with newline characters
    output_quote = output_quote.replace('\t\t', '\n\n')
    output_quote = output_quote.replace('\t', '\n')
    return output_quote

def speech_bubble(input_array):

    output_string = ''
    output_string += ' ' + ('_' * 42) + ' \n'
    lines = len(input_array)

    if lines == 1:
        output_string += '< ' + input_array[0] + (' ' * (40 - len(input_array[0]))) + ' >\n'
    elif lines >= 1:
        output_string += '/ ' + input_array[0] + (' ' * (40 - len(input_array[0]))) + ' \\\n'
        for index in range(1, len(input_array) - 1):
            output_string += '| ' + input_array[index] + (' ' * (40 - len(input_array[index]))) + ' |\n'
        output_string += '\\ ' + input_array[len(input_array) - 1] + (' ' * (40 - len(input_array[len(input_array) - 1]))) + ' /\n'

    output_string += ' ' + ('¯' * 42) + ' '
    return output_string


quote = ''

if len(sys.argv) < 2:
    for line in sys.stdin:
        quote += line
else:
    for index in range(1, len(sys.argv)):
        quote += sys.argv[index]
        if index != len(sys.argv) - 1:
            quote += ' '

quote = format_forty(input_quote=quote)
quote_array = quote.splitlines()

offset = ' ' * 20

bubble = speech_bubble(input_array=quote_array)

print(bubble)

print(offset + '|            /           /')
print(offset + '|           /\' .,,,,  ./')
print(offset + '|          /\';\'     ,/')
print(offset + '|         / /   ,,//,`\'`')
print(offset + '|        ( ,, \'_,  ,,,\' ``')
print(offset + '|        |    /@  ,,, ;" `')
print(offset + '\\       /    .   ,''/\' `,``')
print(offset + ' \\     /   .     ./, `,, ` ;')
print(offset + '  \\ ,./  .   ,-,\',` ,,/\'\'\\,\'')
print(offset + '   |   /; ./,,\'`,,\'\' |   |')
print(offset + '   |     /   \',\'    /    |')
print(offset + '    \\___/\'   \'     |     |')
print(offset + '      `,,\'  |      /     `')
print(offset + '           /      |        ~')
print(offset + '          \'       (')
print(offset + '         :')
print(offset + '        ; .         \\--')
print(offset + '      :   \\         ;            ')