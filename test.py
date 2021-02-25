from journal.helpers import open_file
from journal.themes import find_themes, collect_theme_content

def test_open_file(filename):
    content = open_file(filename)
    return(content)

def test_find_themes(day_text):
    themes = find_themes(day_text)
    print(themes)

def test_collect_theme_content(day_text):
    collect_theme_content(day_text)


if __name__ == "__main__":
    filename = './test.md'
    day_text = test_open_file(filename)
    themes = test_find_themes(day_text)
    test_collect_theme_content(day_text)
