import sys


from optparse import OptionParser
parser = OptionParser()
parser.add_option("-w", action='store', type='string', dest='words')
parser.add_option("-l", action='store', type='string', dest='lines')
parser.add_option("-c", action='store', type='string', dest='chars')
#parser.add_option("-A", action='store', type='string', dest='filename')
#(values,args) = parser.parse_args()
#name = values.words
#print("the file name is",name)
options,args = parser.parse_args()

def file_word(filename):
    file = open(filename, "r+")
    wordN = 1
    for str in file.read():
        if(str == ' '):
            wordN = wordN + 1
    print "The number of words in this document is:",wordN

def file_line(filename):
    file = open(filename,"r+")
    lineN = 1
    for i in file.read():
        if(i == '\n'):
            lineN = lineN + 1
    print "The number of lines in this document is:",lineN

def file_char(filename):
    file = open(filename,"r+")
    charN = 0
    for stc in file.read():
        if(stc == '\n'):
            charN
        else:
            charN = charN + 1
    print "The number of chars in this document is:",charN

#Cause some unexpected chars occured in the filename , so use the clear_filename to repair filename

def clear_filename(string):
    clearBox = "[]\'"
    for i in clearBox:
        string = string.replace(i,"")
    return string

name = str(args)
name = clear_filename(name)
if not (options.chars or options.words or options.lines):

    file_line(name)
    file_word(name)
    file_char(name)

if options.chars:
    file_char(name)
if options.words:
    file_word(name)
if options.lines:
    file_line(name)

"""
file_line(name)
file_word(name)
file_char(name)
"""