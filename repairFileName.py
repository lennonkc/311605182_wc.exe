
import re

name = '][[1.txt][]\'\''
print(name)
#name = name.replace(']',' ')
#name = re.sub("\d+","www",name)
#name = name.replace("[","")
#name = name.replace("]","")
#name = name.replace("\'","")


def clear_filename(string):
    clearBox = "[!@#$%^&*()_=[]\'"
    for i in clearBox:
        string = string.replace(i,"")
    return string

name = clear_filename(name)
print(name)