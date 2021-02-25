"""
Helper functions

"""

def open_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
        return text

