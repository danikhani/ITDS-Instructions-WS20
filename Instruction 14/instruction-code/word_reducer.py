#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
for kv_pair in sys.stdin:
    # remove whitespace
    kv_pair = kv_pair.strip()
    # parse the input (word,count) we got from mapper.py
    word, count = kv_pair.split('\t', 1)
    # convert count (currently a string) to int
    count = int(count)
    # shuflling is done by Hadoop
    if current_word!=word:
        if current_word:
            # write result to STDOUT
            print('%s\t%s' % (current_word, current_count))
        current_word = word
        current_count = count
    else:
        current_count += count

# output the last word
if current_word == word:
    print('%s\t%s' % (current_word, current_count))