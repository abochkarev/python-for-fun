import os
import sys

def center_align(file_name):
    with open(file_name) as f:
        for l in f:
            print("{:^60}".format(l.replace('\n', '')))

if __name__ == '__main__':
    center_align(sys.argv[1])
