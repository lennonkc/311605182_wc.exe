# _*_ coding:UTF-8 _*_
"""
import sys
from optparse import OptionParser
usage="show something usefull -- for example: how to use this program"
parser = OptionParser(usage) #带参的话会把参数变量的内容作为帮助信息输出
parser.add_option("-f","--file",dest="filename",help="read picture from File",metavar="FILE",action = "store",type="string")
parser.add_option("-s","--save",dest="save_mold",help="save image to file or not",default = True)
(options,args)=parser.parse_args()
print (options.filename)
print (options.save_mold)
"""
# !/usr/bin/env python

import os, sys
from optparse import OptionParser
###############

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

###############
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



def main():
    'main functions'
    option, args = opt()
    if not (option.chars or option.words or option.lines):
        option.chars, option.words, option.lines = True, True, True
    if args:
        total_lines, total_words, total_chars = 0, 0, 0
        for filename in args:
            if os.path.isfile(filename):
                with open(filename) as fd:
                    data = fd.read()
                    lines, words, chars = get_count(data)
                    print_wc(option, lines, words, chars, filename)
                    total_lines += lines
                    total_words += words
                    total_chars += chars
            elif os.path.isdir(filename):
                print >> sys.stderr, '%s is a directory' % filename  # 利用print写入到文件中去，注意这里仅仅适用于Python 2.x，python3是不支持的（可以用print(i,file=sys.stdout) 或者sys.stdout.write()）
            else:
                sys.exit('%s : No such file or Directory' % filename)
        if len(args) > 1:
            print_wc(option, total_lines, total_words, total_chars, 'total')
    else:
        data = sys.stdin.read()
        filename = ''
        lines, words, chars = get_count(data)
        print_wc(option, lines, words, chars, filename)


if __name__ == '__main__':
    main()