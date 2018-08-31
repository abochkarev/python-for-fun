import contextlib
import os
import sys


def wrap(file_name, str_len):
    with open(file_name) as f:
        for l in f:
            string = ''
            for i in l:
                if i == '\n':
                    yield string
                    continue
                string += i
                if len(string) == str_len:
                    yield string
                    string = ''


if __name__ == '__main__':
    for l in wrap(sys.argv[1], int(sys.argv[2])):
        print(l)
