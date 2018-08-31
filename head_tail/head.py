import os
import sys

def head(file_name, lines_count=10):
    with open(file_name) as f:
        for num, line in enumerate(f, 1):
            if num > lines_count:
                break
            else:
                yield line.replace('\n', '')

if __name__ == '__main__':
    for i in head(sys.argv[1], 3):
        print(i)
