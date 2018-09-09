import sys


from optparse import OptionParser
parser = OptionParser()
parser.add_option("-f", action='store', type='string', dest='filename')

(values,args) = parser.parse_args()
name = values.filename
print("the file name is",name)
def file_word(filename):
    file = open(filename, "r+")
    wordN = 1
    for str in file.read():
        if(str == ' '):
            wordN = wordN + 1
    print("The number of words in this document is:",wordN )

def file_line(filename):
    file = open(filename,"r+")
    lineN = 1
    for i in file.read():
        if(i == '\n'):
            lineN = lineN + 1
    print("The number of lines in this document is:",lineN )

def file_char(filename):
    file = open(filename,"r+")
    charN = 0
    for stc in file.read():
        if(stc == '\n'):
            charN
        else:
            charN = charN + 1
    print("The number of chars in this document is:",charN )

file_line(name)
file_word(name)
file_char(name)
