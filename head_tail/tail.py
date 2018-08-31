import os
import sys


def tail(file_name, lines_count=10):
    with open(file_name) as f:
        position = f.seek(0, os.SEEK_END)
        string = ''
        count = 0
        while position >= 0 and lines_count >= count:
            f.seek(position)
            char = f.read(1)
            if char == '\n':
                yield string[::-1]
                string = ''
                count += 1
            else:
                string += char
            position -= 1
        yield string[::-1]


if __name__ == '__main__':
    for i in reversed(list(tail(sys.argv[1], int(sys.argv[2])))):
        print(i)
