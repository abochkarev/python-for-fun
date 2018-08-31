import sys


def wordwrap(file_name, str_len):
    with open(file_name) as f:
        for l in f:
            string = ''
            for c in l:
                if c == '\n':
                    yield string
                string += c
                if len(string) >= str_len - 1:
                    if c == ' ':
                        yield string
                        string = ''
                else:
                    continue


if __name__ == '__main__':
    for w in wordwrap(sys.argv[1], int(sys.argv[2])):
        print(w)
