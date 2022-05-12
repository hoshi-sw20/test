str01 = "Hello,Python!!!"
lis02 = ["HOSHI","MUNETA","HONDA"]

num=2
print(num)
print(type(num))

print(str01)

print(lis02[0])
print(lis02[1])
print(lis02[2])



for i in range (5):  
    if i ==3:
        break
    print(i)

print()

class Student:
    def __init__(self,name):#初期化
        self.name = name
    def avg(self,math,english):
        print((math + english) /2)

a001 = Student("HOSHI")
#a001.name = "HOSHI"
print(a001.name)
a001.avg(30,70)

a002 = Student("HIDEYUKI")
print(a002.name)
a002.avg(80,70)