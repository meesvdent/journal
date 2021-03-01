#!/usr/bin/env python3


"""
Puts the test from different subjects into different text files

"""


import os
import re
from helpers import open_file, dump_into_file


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
        themesplit = re.split('\n| ', themetext, 1)
        theme_dict[themesplit[0]] = themesplit[1]

    return theme_dict




def collect_theme_content(themes_dict, date, theme_folder):
    """
    Puts all the to do's and notes on the same theme from different files into
    one text file

    """


    for theme, content in themes_dict.items():
        filename = theme_folder + "/" + theme + ".md"
        if not os.path.exists(filename):
            open(filename, 'a').close()
        with open(filename, 'a') as cfile:
            cfile.write("# "+date+"\n")
            cfile.write(content)
            cfile.write("\n")



if __name__ == "__main__":
    entry_folder = "/Users/meesvdent/Journal/journal_entries"
    theme_folder = "/Users/meesvdent/Journal/themes"
    for theme_file in os.listdir(theme_folder):
        theme_path = theme_folder + "/" + theme_file
        os.remove(theme_path)
    for filename in os.listdir("/Users/meesvdent/Journal/journal_entries"):
        if filename.endswith(".md"):
            file_path = entry_folder + '/'  + filename
            day_text = open_file(file_path)
            themes = find_themes(day_text)
            themes_dict = split_themes(day_text)
            date = filename.split(".", 1)[0]
            collect_theme_content(themes_dict, date, theme_folder)







