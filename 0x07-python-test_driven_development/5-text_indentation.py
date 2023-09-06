#!/usr/bin/python3
"""Define text_indentation module"""


def text_indentation(text):
    """text_identation function"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    characters = ['.', '?', ':']
    new_text = ""

    for i in range(len(text)):
        if text[i] == ' ' and text[i - 1] in characters:
            continue
        try:
            if text[i] in characters and (text[i + 1] == ' ' or text[i + 1] == '\n'):
                new_text += text[i] + '\n\n'
        except IndexError:
            pass
        else:
            new_text += text[i]

    lines = new_text.split("\n")
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    new_text = '\n'.join(lines)
    print(new_text, end="")
