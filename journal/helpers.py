"""
Helper functions

"""

import os

def open_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
        return text


def dump_into_file(filename, header, text):
    print("created ", filename, "\n")
    if not os.path.exists(filename):
        print("filename doesn't exist")
        open(filename, 'a').close()
    with open(filename, 'a') as cfile:
        cfile.write(header)
        cfile.write('\n')
        cfile.write(text)
