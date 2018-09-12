"""
def func(year):
    return year%400==0 or (year%4==0 and year%100!=0)

print(func(1900))

class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'

summer = Bird()
print(summer.have_feather)
"""
"""

summer = Bird()
summer.move(3,4)
print(summer.move(3,4))
print ('after move:',summer.move(5,8))

"""
"""
class Human(object):
    laugh = 'hahahaha'
    def show_laugh(self):
        print (self.laugh)
    def laugh_100th(self,a):
        for i in range(a):
            self.show_laugh()

li_lei = Human()
li_lei.laugh_100th(6)
"""
"""
class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
    def move(self, dx, dy):
        position = [0,0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position


class happyBird(Bird):
    def a(self,more_words):
        print ('We are happy birds.',more_words)

summer = happyBird()
summer.a('qwe')
"""
"""
class Human(object):
    def __init__(self, input_gender):
        self.gender = input_gender
    def printGender(self):
        print (self.gender)

li_lei = Human('male') # 这里，'male'作为参数传递给__init__()方法的input_gender变量。
print (li_lei.gender)
li_lei.printGender()
"""

"""
n1 = list()
n1 = [1,2,1,2,3,4,5]
#print(n1.count(2))
class superList(list):
    def __sub__(self, b):
        a = self[:]     # 这里，self是supeList的对象。由于superList继承于list，它可以利用和list[:]相同的引用方法来表示整个对象。
        b = b[:]
        while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a
print(n1.pop())
print(n1.remove(2),n1.remove(2))
print(n1)
print (superList([1,2,3,4]) - superList([3,4]))
"""
"""
dic = {'tom':11, 'sma':55,'lll':100}
print(dic)
print(dic['tom'])
dic['ililiiil'] = 99
print(dic)
for key in dic:
    print(dic[key])
"""
"""
def file_line_num(fnames):
    # 计算多个文件的行数之和 
    total_sum = 0
    for fname in fnames:
        sum = 0
        with open(fname) as f:
            for line in f:
                sum = sum +1
        total_sum = total_sum + sum
    return total_sum
fns = ['1.txt', '2.txt']
print (file_line_num(fns))
"""

import os
import sys
from optparse import OptionParser


def opt():
    parser = OptionParser()

    parser.add_option("-c", "--chars",
                      dest="chars",
                      action="store_true",
                      default=False,
                      help="only count chars.")
    parser.add_option("-w", "--words",
                      dest="words",
                      action="store_true",
                      default=False,
                      help="only count words.")
    parser.add_option("-l", "--lines",
                      dest="lines",
                      action="store_true",
                      default=False,
                      help="only count lines.")
    parser.add_option("-n", "--nototal",
                      dest="nototal",
                      action="store_true",
                      default=False,
                      help="not print total count.")
    options, args = parser.parse_args()

    return options, args


def get_Count(data):
    chars = len(data)
    words = len(data.split())
    lines = data.count('\n')
    return lines, words, chars


def print_wc(options, lines, words, chars, fn):
    if options.lines:
        print
        lines,
    if options.words:
        print
        words,
    if options.chars:
        print
        chars,
    print
    fn


def main():
    options, args = opt()
    if not (options.chars or options.words or options.lines):
        options.chars, options.words, options.lines = True, True, True
    if args:
        total_lines, total_words, total_chars = 0, 0, 0
        for fn in args:
            if os.path.isfile(fn):
                with open(fn) as fd:
                    data = fd.read()
                    lines, words, chars = get_Count(data)
                    print_wc(options, lines, words, chars, fn)
                    total_lines += lines
                    total_words += words
                    total_chars += chars
            elif os.path.isdir(fn):
                print >> sys.stderr, "%s: is a directory." % fn
            else:
                sys.stderr.write("%s: No such file or directory.\n" % fn)
        if len(args) > 1:
            if not options.total:
                print_wc(options, total_lines, total_words, total_chars, 'total')

    else:
        data = sys.stdin.read()
        fn = ""
        lines, words, chars = get_Count(data)
        print_wc(options, lines, words, chars, fn)


if __name__ == '__main__':
    main()