from helpers import open_file
from themes import find_themes



def test_open_file():
    filename = "./journal_entries/22_02_2021.md"
    content = open_file(filename)
    return(content)

def test_find_themes():
    content = test_open_file()
    themes = find_themes(content)
    print(themes)


if __name__ == "__main__":
    test_open_file()
    test_find_themes()
