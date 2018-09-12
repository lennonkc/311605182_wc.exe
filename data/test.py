import sys
import os

file = open("1.txt", "r+")
str = file.read()
print(str)
charN = len(str)
print(charN)
for i in str:
  if (str == ' ' or str == '\n'):
      print(i)
