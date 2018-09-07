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
