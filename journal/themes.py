#!/usr/bin/env python3


"""
Puts the test from different subjects into different text files

"""


import os


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


def split_themes(day_text):
    """
    Splits a note into a list of markdown for eacht theme
    for now hardcoded theme charecteristic " ## " or "\n## "

    """
    theme_contents = day_text.replace('\n## ', ' ## ').split(" ## ")
    theme_dict = {}
    for themetext in theme_contents:
        themesplit = themetext.split(' ', 1)
        theme_dict[themesplit[0]] = themesplit[1]

    return theme_dict




def collect_theme_content(day_text):
    """
    Puts all the to do's and notes on the same theme from different files into
    one text file

    """

    themefolder = "./themes"

    if not os.path.exists(themefolder):
        os.makedirs(themefolder)

    split_text = split_themes(day_text)

    for theme, text in split_text.items():
        print(theme, '\n', text)










