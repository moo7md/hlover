#!/usr/bin/env python

# This project is created to make HTML coding much easier and simpler
# Author: Mohammed Alsharaf
# Date: 8/18/2019

# The structuer is simple. You feed this app your .hl file and then you get out .html file

import os.path
import sys

# constants for !doctype
doctypes = {"html5": '<!DOCTYPE html>',
            "html4s": '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">',
            "html4t": '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">',
            "html4f": '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd">',
            "xhtml1s": '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" '
                       '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> ',
            "xhtml1t": '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" '
                       '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> ',
            "xhtml1f": '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN" '
                       '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd"> ',
            "xhtml1.1": '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">'}


def get_string(char, file):
    # handles strings in JavaScript
    string = char
    char = file.read(1)
    counter = 0 if char == '"' else 1
    while counter != 0 and char != '':
        if char == '\\':
            string += char
            string += file.read(1)
        elif char == '"' or '\'':
            counter -= 1
            string += char
            break
        else:
            string += char
        char = file.read(1)
    else:
        string += char
    return string


def writeScriptBody(char, file):
    # only write the body of <script>
    body = ''
    counter = 0 if char == '}' else 1
    while char != '' and counter != 0:
        if char == '{':
            body += char
            counter += 1
        elif char == '}':
            if counter == 1:
                counter -= 1
            else:
                body += char
                counter -= 1
        elif char == '\'' or char == '"':
            body += get_string(char, file)
        else:
            body += char
        char = file.read(1)
    # file.seek(file.tell()-1)
    if counter > 0:
        char = body[len(body) - 1]
        while char == "}" or char == ' ' or char == '\n':
            body = body[:-1]
            char = body[len(body) - 1]
    return body


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
            elif char == '\\':
                body += file.read(1)
                char = file.read(1)
            elif tag == 'script':
                body += writeScriptBody(char, file)
                break
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


def is_doctype(token):
    token = token.lower()
    return token == 'html5' or token == 'html4s' or token == 'html4t' or token == 'html4f' or token == 'xhtml1s' or token == 'xhtml1t' or token == 'xhtml1f' or token == 'xhtml1.1'


def start(file):
    # add <DOCTYPE! HTML> later
    with open(file, 'r') as f:
        char = f.read(1)
        token = ''
        while char != '':
            if is_doctype(token):
                print(doctypes[token])
            if (char == '[') or (char == '{'):
                # if token.__contains__('p'):
                new_str = do_element(f, char, token)
                print(new_str)
                token = ''
            if (char != '[') and (char != '{') and (char != '\n') and (char != '}'):
                token += char
            char = f.read(1)
        # in case doctype was the only thing in the file
        if is_doctype(token):
            print(doctypes[token])


def main():
    if len(sys.argv) == 1:
        print("Error: no input files")
    elif str(sys.argv[1]).endswith('.hl'):
        start_working(sys.argv[1])


# else:
#     print("Error: unsupported file type")


def start_working(filename):
    if os.path.isfile(filename):
        start(filename)
    else:
        print("Error: file does not exists")
        sys.exit(-1)


main()
