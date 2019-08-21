#!/usr/bin/env python

# This project is created to make HTML coding much easier and simpler
# Author: Mohammed Alsharaf
# Date: 8/18/2019

# The structuer is simple. You feed this app your .hl file and then you get out .html file

import os.path
import sys
import re


# constants for !doctype
doctypes = {"html5": '<!DOCTYPE html>',
            "html4s": '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">',
            "html4t": '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" '
                      '"http://www.w3.org/TR/html4/loose.dtd">',
            "html4f": '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" '
                      '"http://www.w3.org/TR/html4/frameset.dtd">',
            "xhtml1s": '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" '
                       '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> ',
            "xhtml1t": '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" '
                       '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> ',
            "xhtml1f": '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN" '
                       '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd"> ',
            "xhtml1.1": '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" '
                        '"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">'}
# memory to hold classes and variables
mem = {}


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


def mirge_attr(attr, inherit_attr):
    # construct the new attr. Checks if there are overriding is happening
    new_attr = ''
    attr = re.sub(r'\s*(=)\s*', ' ', attr.strip())  # remove all whitespace between =
    attr = re.sub(r'(")\s+', '" ', attr.strip())  # remove all whitespace in between attr
    a_array = re.split(r'(\s\")|(\"\s)', attr)  # split the string
    a_array = list(filter(lambda a: a != None and a != ' "' and a != '" ', a_array))

    inherit_attr = re.sub(r'\s*(=)\s*', ' ', inherit_attr.strip())  # remove all whitespace between =
    inherit_attr = re.sub(r'(")\s+', '" ', inherit_attr.strip())  # remove all whitespace in between attr
    i_array = re.split(r'(\s\")|(\"\s)', inherit_attr)  # split the string
    i_array = list(filter(lambda a: a != None and a != ' "' and a != '" ', i_array))
    for string in a_array:
        if i_array.__contains__(string):
            i_array.pop(i_array.index(string) + 1)
            i_array.remove(string)
    i = 0
    while i < len(a_array):
        if i == len(a_array) - 1:
            new_attr += a_array[i] + ' '
            i += 2
        else:
            if a_array[i + 1].count('"') == 1:
                new_attr += a_array[i] + '=' + '"' + a_array[i + 1] + ' '
            else:
                new_attr += a_array[i] + '=' + '"' + a_array[i + 1] + '" '
            i += 2
    i = 0
    while i < len(i_array):
        if i == len(i_array) - 1:
            new_attr += i_array[i] + ' '
            i += 2
        else:
            if i_array[i + 1].count('"') == 1:
                new_attr += i_array[i] + '=' + '"' + i_array[i + 1] + ' '
            else:
                new_attr += i_array[i] + '=' + '"' + i_array[i + 1] + '" '
            i += 2

    return new_attr


def add_class(sub_tag, char, file, inherit_attr):
    class_id = re.sub(r'class\s*:\s*', '', sub_tag).strip()
    body = re.sub(r'<.*' + sub_tag + '.*>|</.*' + sub_tag + '.*>', '',
                  do_element(file, char, sub_tag, inherit_attr)).strip()
    mem.update({class_id: body})


def loop_element(class_id, char, file, inherit_attr):
    times = int(re.sub(r'loop\s+', '', class_id).strip())
    class_body = re.sub(r'<\s*' + class_id + r'\s*>', '',
                        do_element(file, char, class_id, inherit_attr).strip())
    class_body = re.sub(r'</\s*' + class_id + r'\s*>', '',
                        class_body).strip()
    body = ''
    for i in range(0, times):
        body += class_body
    return body


def do_element(file, char, tag, inherit_attr):
    result = '<' + tag
    attr = ''
    body = ''
    if char == '(':
        # save inherit attr for sub-tags
        char = file.read(1)
        temp_inherit = ''
        while char != ')' and char != '':
            temp_inherit += char
            char = file.read(1)
        char = file.read(1)
        inherit_attr = mirge_attr(temp_inherit, inherit_attr) if inherit_attr != '' else temp_inherit
        while char == ' ' and char != '':
            char = file.read(1)
    if char == '[':
        result += ' '
        char = file.read(1)
        while char != ']' and char != '':
            attr += char
            char = file.read(1)
        char = file.read(1)
        while char == ' ' and char != '':
            char = file.read(1)
    else:
        attr = inherit_attr

    if char == '{':
        char = file.read(1)
        if char == '}':
            body = ' '
        while char != '}' and char != '':
            if char == '!':
                ignore_attr = False
                sub_tag = ''
                char = file.read(1)
                while char != '[' and char != '{' and char != '' and char != '(' and char != '!':
                    if char == '*':
                        ignore_attr = True
                        char = file.read(1)
                        continue
                    sub_tag += char
                    char = file.read(1)
                if sub_tag.__contains__('class'):
                    add_class(sub_tag, char, file, inherit_attr)
                    char = file.read(1)
                elif sub_tag.__contains__('loop'):
                    body += loop_element(sub_tag, char, file, inherit_attr)
                    char = file.read(1)
                else:
                    sub_body = do_element(file, char, sub_tag, '' if ignore_attr else inherit_attr)
                    body += sub_body
                    char = file.read(1)
            elif char == '$':
                class_id = ''
                char = file.read(1)
                while char != '' and char != ' ' and char != '\n' and char != '}' and char != '!' and char != '$':
                    class_id += char
                    char = file.read(1)
                if mem.__contains__(class_id):
                    body += mem[class_id]
            elif char == '\\':
                body += file.read(1)
                char = file.read(1)
            elif tag == 'script' or tag == 'style' or tag == '!--':
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
        if result[len(result) - 1] != ' ':
            result += ' '
        result += (attr if inherit_attr == '' or attr == inherit_attr else mirge_attr(attr,
                                                                                      inherit_attr)) + '>' + body + '</' + tag + '>'

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
                token = ''
            if (char == '[') or (char == '{') or (char == '('):
                new_str = do_element(f, char, token, '')
                print(new_str)
                token = ''
            if (char != ' ') and (char != '[') and (char != '{') and (char != '\n') and (char != '}') and (char != '('):
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
    else:
        print("Error: unsupported file type")


def start_working(filename):
    if os.path.isfile(filename):
        start(filename)
    else:
        print("Error: file does not exists")
        sys.exit(-1)


main()
