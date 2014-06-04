#!/usr/bin/env python

from urllib import urlopen
from string import ascii_lowercase
import re
import sys


suggestURL = "http://google.com/complete/search?output=toolbar&q="

def grabSuggestions(key):
    
    keywords = []

    for char in ascii_lowercase:
        webpage = urlopen(suggestURL+key+" "+char).read()
        keywords.extend(re.findall(r'data="(\w*\s*\w*\s*\w*\s*)"', webpage))

    return keywords



if __name__ == "__main__":

    #usage should be along lines of
    #cat test.txt | python grabGoogleAutoSuggest.py

    for key in sys.stdin.readlines():
        key = key.strip()
        keywords = grabSuggestions(key)

        for word in keywords:
            print word

