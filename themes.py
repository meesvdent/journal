#!/usr/bin/env python3


"""
Puts the test from different subjects into different text files

"""


def find_themes(day_text):
    """
    Makes a list of themes in the day files.

    """


    themes = []
    day_text = day_text.replace("\n", " ")
    words = day_text.split(" ")
    for i in range(0, len(words)):
        if words[i] == "##":
            themes.append(words[i+1])

    return themes


def gather_theme(theme):
    """
    Puts all the to do's and notes on the same theme from different files into
    one text file

    """
    pass





