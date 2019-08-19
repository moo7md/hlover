# this file start working reading file and building the main string


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
        file.seek(file.tell()-2)
    else:
        result += attr + '>' + body + '</' + tag + '>'

    return result


def start(file):
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
