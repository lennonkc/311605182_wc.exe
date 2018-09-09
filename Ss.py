
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
