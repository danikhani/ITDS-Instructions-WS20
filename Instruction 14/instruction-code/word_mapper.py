#!/usr/bin/env python

import sys

# input comes from STDIN
for sentence in sys.stdin:
    # remove whitespace
    sentence = sentence.strip()
    # split the sentence into words
    words = sentence.split()
    # increase counters
    for word in words:
        # write the results to STDOUT;
        # key: word, value: 1 (count of the word)
        print('%s\t%s' % (word, 1))