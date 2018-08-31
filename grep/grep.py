import sys


def grep(file_name, string):
    with open(file_name) as f:
        for l in f:
            if string in l:
                yield l.replace('\n', '').strip()


if __name__ == '__main__':
    for i in grep(sys.argv[1], sys.argv[2]):
        print(i)
