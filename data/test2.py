import os
import sys
import unittest

from optparse import OptionParser
usage = "myprog[ -f <filename>][-s <xyz>] arg1[,arg2..]"
parser=OptionParser(usage)

parser.print_help()

parser.add_option("-s", action='store', type='string', dest='keyword',help="you must use '-p' to define a file path first,for example: -p -s c:\\usr\\bin Keyword")
parser.add_option("-p", action='store', type='string', dest='path',help="define a path")
args = ["-p","O:\\software-Engineering\\311605182_wc.exe","-s", "1.txt"]
options, args = parser.parse_args(args)

def search_filename(path, word):
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        if os.path.isfile(fp) and word in filename:
            print (fp)
        elif os.path.isdir(fp):
            search_filename(fp, word)

#print(options)
#print (args)
#print (parser.print_help())

str=[options.path,options.keyword]
#print(options.keyword)
#print(options.path)
#search_filename(str[0],str[1])