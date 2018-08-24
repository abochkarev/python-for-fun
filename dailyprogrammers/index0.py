import pprint
import sys
import re

PATH = 'about.txt'

WORD_RE = re.compile('\w+')

d = {}
with open(PATH) as f:
    for index, line in enumerate(f, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            t = (index, match.start() + 1)
            d.setdefault(word, []).append(t) 
pprint.pprint(d)

