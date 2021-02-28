import os
from journal.helpers import open_file, dump_into_file
from journal.themes import find_themes, split_themes, collect_theme_content

def test_open_file(filename):
    content = open_file(filename)
    return(content)

def test_find_themes(day_text):
    themes = find_themes(day_text)

def test_collect_theme_content(day_text):
    collect_theme_content(day_text)

def test_dump_themes_into_file(themes_dict, date, theme_folder):
    collect_theme_content(themes_dict, date, theme_folder)

if __name__ == "__main__":
    filename = './test.md'
    theme_folder = './tests/themes'
    day_text = test_open_file(filename)
    themes = test_find_themes(day_text)
    themes_dict = split_themes(day_text)
    test_dump_themes_into_file(themes_dict, "01_01_2021", theme_folder)
