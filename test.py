#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
import sys
name = raw_input("Please input your name: ")
print (name)

import sys
print("please")
name = sys.stdin.readline()
print(name)


import sys
import time

for i in range(10):
    sys.stdout.write('>') #当然这里加上\n就会一个一个输出，因为sys.stdout是正行正行输出（加\n,就类似于print了）
    sys.stdout.flush() #强制i刷新到stdout中去
    time.sleep(1)
"""



"""

#成功统计行数 词数 字符数
#!/usr/bin/env python
import sys
data = sys.stdin.read()
chars = len(data)
words = len(data.split())
lines = data.count('\n')
print('%s %s %s ' % (lines,words,chars))
#print('%(lines)s %(words)s %(chars)s' % locals()) #高级用法，%(key)s,表示格式化关键字替换，后面就需要以字典的方式传入对应的key值，而locals（)，表示当前环境下所有的变量和值的字典，所以这里可以进行替换
 #这种方法和上面利用locals的方式是一样的，只不过locals的变量更多而已words

"""
"""
fo=open("1.txt","r+")
print("文件名",fo.name)
print("是否已关闭",fo.closed)
print("访问模式：",fo.mode)
#fo.write("www.google.com")
str=fo.read()
print(str)
fo.close()
print("是否已关闭",fo.closed)
"""

"""
lineN = 0
wordN = 0
charN = 0
for str in fo.read():
    if (str == ' '):
        wordN = wordN+1
    else:
        wordN = wordN

fo=open("1.txt","r+")
for line in fo.readlines():
 #   line=line.strip()
    lineN = lineN+1

fo=open("1.txt","r+")
for stc in fo.read():
    charN = charN + 1

print(lineN,wordN,charN)

fo.close()
"""

"""
#测试成功
def file_word():
    file = open("2.txt", "r+")
    wordN = 1
    for str in file.read():
        if(str == ' '):
            wordN = wordN + 1
    print("文档的单词数是:",wordN)

def file_line():
    file = open("2.txt","r+")
    lineN = 1
    for i in file.read():
        if(i == '\n'):
            lineN = lineN + 1
    print("文档的行数是:",lineN)

def file_char():
    file = open("2.txt","r+")
    charN = 0
    for stc in file.read():
        if(stc == '\n'):
            charN
        else:
            charN = charN + 1
    print("文档的字符数是:", charN)

file_line()
file_char()
file_word()
"""

import sys
from optparse import OptionParser
parser = OptionParser()
parser.add_option('-w','--word',dest='words',action='store_true',default=False,help='only user to count words')
options,args = parser.parse_args()

def file_word(fname):
    file = open(fname, "r+")
    wordN = 1
    for str in file.read():
        if(str == ' '):
            wordN = wordN + 1
    print("文档的单词数是:",wordN)

file_word(args)