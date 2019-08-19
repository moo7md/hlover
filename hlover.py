#!/usr/bin/env python

# This project is created to make HTML coding much easier and simpler
# Author: Mohammed Alsharaf
# Date: 8/18/2019

# The structuer is simple. You feed this app your .hl file and then you get out .html file

import os.path
import sys


def do_element(file, char, tag):
    result = '<' + tag
    attr = ''
    body = ''
    if char == '[':
        result += ' '
        char = file.read(1)
        while char != ']' and char != '':
            attr += char
            char = file.read(1)
        char = file.read(1)
        while char == ' ':
            char = file.read(1)
    if char == '{':
        char = file.read(1)
        if char == '}':
            body = ' '
        while char != '}' and char != '':
            if char == '!':
                sub_tag = ''
                char = file.read(1)
                while char != '[' and char != '{':
                    sub_tag += char
                    char = file.read(1)
                sub_body = do_element(file, char, sub_tag)
                body += sub_body
                char = file.read(1)
            else:
                if char != ']':
                    body += char
                char = file.read(1)
    if body == '':
        result += attr + '>'
        file.seek(file.tell() - 2)
    else:
        result += attr + '>' + body + '</' + tag + '>'

    return result


def start(file):
    # add <DOCTYPE! HTML> later
    with open(file, 'r') as f:
        char = f.read(1)
        token = char
        while char != '':
            if (char == '[') or (char == '{'):
                # if token.__contains__('p'):
                new_str = do_element(f, char, token)
                print(new_str)
                token = ''
            char = f.read(1)
            if (char != ' ') and (char != '[') and (char != '{') and (char != '\n') and (char != '}'):
                token += char


def main():
    if len(sys.argv) == 1:
        print("Error: no input files")
    elif str(sys.argv[1]).endswith('.hl'):
        start_working(sys.argv[1])
    else:
        print("Error: unsupported file type")


def start_working(filename):
    if os.path.isfile(filename):
        start(filename)
    else:
        print("Error: file does not exists")
        sys.exit(-1)


main()
