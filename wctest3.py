#!/usr/bin/env python
# _*_ coding:UTF-8 _*_


import os, sys
from optparse import OptionParser

def file_word():
    file = open("2.txt", "r+")
    wordN = 1
    for str in file.read():
        if(str == ' '):
            wordN = wordN + 1
    print("文档的单词数是:",wordN)
    return wordN

def file_line():
    file = open("2.txt","r+")
    lineN = 1
    for i in file.read():
        if(i == '\n'):
            lineN = lineN + 1
    print("文档的行数是:",lineN)
    return lineN

def file_char():
    file = open("2.txt","r+")
    charN = 0
    for stc in file.read():
        if(stc == '\n'):
            charN
        else:
            charN = charN + 1
    print("文档的字符数是:", charN)
    return charN

	
def opt():
    'Get Command line parser'
    parser = OptionParser()
    parser.add_option('-c', '--char', dest='chars', action='store_true', default=False, help='used to count chars')
    parser.add_option('-w', '--word', dest='words', action='store_true', default=False, help='used to count words')
    parser.add_option('-l', '--line', dest='lines', action='store_true', default=False, help='used to count lines')
    option, args = parser.parse_args()
    return option, args

def get_count(data):
    'count for lines ,words or chars'
    chars = file_char(data)
    words = file_word(data)
    lines = file_line(data)
    return lines, words, chars

def print_wc(option, lines, words, chars, filename):
    'print lines,words or chars'
    if option.lines:
        print (lines)
    if option.words:
        print (words)
    if option.chars:
        print (chars)
    print(filename)


option, args = opt()
if not (option.chars or option.words or option.lines):
    option.chars, option.words, option.lines = True, True, True
for filename in args:

