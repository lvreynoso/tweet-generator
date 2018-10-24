#!/usr/bin/env python3
# wow much dragon many say
# ASCII art from https://asciiart.website/index.php?art=creatures/dragons
# Accessed October 23, 2018

import sys

def format_forty(input_quote):
    split_quote = input_quote.splitlines()
    format_quote = ''
    for index in range(0, len(split_quote)):
        format_quote += split_quote[index]
        if index != len(split_quote) - 1:
            format_quote += ' '
    space_indices = []
    newline_indices = []
    output_quote = ''
    for index in range(0, len(format_quote)):
        if format_quote[index] == ' ':
            space_indices.append(index)
    lines = int(space_indices[len(space_indices) - 1] / 40)
    for num in range(1, lines + 1):
        found = False
        for index in range(0, len(space_indices)):
            if space_indices[index] > num * 40 and found == False:
                newline_indices.append(space_indices[index - 1])
                found = True
    for index in range(0, len(format_quote)):
        output_quote += format_quote[index]
        for number in newline_indices:
            if number == index:
                output_quote += '\n'
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