#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

import sys


# 遍历文件对象，并统计行数
def lineCount(f):
    n = 0
    for i in f:
        n += 1
    return n


input = sys.stdin
lineCount(input)
print(input)