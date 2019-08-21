class Class:
    def __init__(self, tag, attr, body):
        self.tag = tag
        self.attr = attr
        self.body = body

    def translate(self):
        string = '<' + self.tag
        string += '>' if self.attr == '' else self.attr + '>'
        string += '' if self.body == '' else self.body + '</' + self.tag + '>'
        return string
