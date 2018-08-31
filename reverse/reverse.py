import os
import sys


class Reverser:
    """A class for reversing text from a file"""

    def __init__(self, file_name):
        self._file_name = file_name

    def reverse(self):
        with open(self._file_name) as f:
            position = f.seek(0, os.SEEK_END)
            string = ''
            while position >= 0:
                f.seek(position)
                char = f.read(1)
                if char == '\n':
                    yield string[::-1]
                    string = ''
                else:
                    string += char
                f.seek(position)
                position -= 1
            yield string[::-1]


if __name__ == '__main__':
    reverser = Reverser(sys.argv[0])
    for l in reverser.reverse():
        print(l)
