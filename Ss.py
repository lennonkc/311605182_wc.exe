import sys
import os

from optparse import OptionParser
usage = "myprog[ -h <lcspa>] filename"
parser = OptionParser(usage)
parser.print_help()
parser.add_option("-w", action='store', type='string', dest='words',help="Count the numbers of WORDS in a file")
parser.add_option("-l", action='store', type='string', dest='lines',help="Count the numbers of LINES in a file")
parser.add_option("-c", action='store', type='string', dest='chars',help="Count the numbers of CHARS in a file")
parser.add_option("-s", action='store', type='string', dest='keyword',help="you must use '-p' to define a file path first,for example: -p -s c:\\usr\\bin Keyword")
parser.add_option("-p", action='store', type='string', dest='path',help="define a path,use this first and then use -s")
parser.add_option("-a", action='store', type='string', dest='special',help="Count the Special lines in a file")
options,args = parser.parse_args()

def file_word(filename):
    file = open(filename, "r+")
    wordN = 0
    str = file.read()
    wordN = len(str.split())
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
#Cause when using the args to deliver, some unexpected chars occured in the filename , so use the clear_filename to repair filename
def clear_filename(string):
    clearBox = "[]\'"
    for i in clearBox:
        string = string.replace(i,"")
    return string
def search_filename(path, word):
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        if os.path.isfile(fp) and word in filename:
            print (fp)
            return fp
        elif os.path.isdir(fp):
            search_filename(fp, word)

def special_line(filename):
    file = open(filename,"r+")
    BlankLines = 0
    CommentLines = 0
    CodeLines = 0
    for line in file.readlines():
        line = line.strip()
        if not len(line):
            BlankLines = BlankLines + 1
        if line.startswith('#') or line.startswith('\\'):
            CommentLines = CommentLines + 1
        else:
            CodeLines = CodeLines + 1
    print"The number of BlankLines is:", BlankLines
    print"The number of CodeLines is:", CodeLines
    print"The number of CommentLines is:", CommentLines
 #  for MultiLineconmment in file.readline():


name = str(args)
name = clear_filename(name)
if not ((options.chars or options.words or options.lines or options.keyword or options.special)):
    file_line(name)
    file_word(name)
    file_char(name)
    special_line(name)

if options.chars:
    file_char(options.chars)
if options.words:
    file_word(options.words)
if options.lines:
    file_line(options.lines)
if options.special:
    special_line(options.special)
if (options.path and options.keyword ):
    str = [options.path,options.keyword]
    fp = search_filename(str[0],str[1])
    file_word(fp)
    file_char(fp)
    file_line(fp)
    special_line(fp)
if not (options.path )and options.keyword:
    print "Please use -p to define a path first"

"""

-p O:\software-Engineering\311605182_wc.exe -s 1.txt
O:\\
"""