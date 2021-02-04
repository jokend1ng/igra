print ("Добро пожаловать в страну сказок странник, выбери своего героя: ")
class human:
    __x="мужчина"
    __y="женщина"
    def __init__(self,x,y):
        self.__x =x
        self.__y=y
    def getX(self):
        return self.__x
    def getY(self):
         return self.__y
    def setX(self,x):
        self.__x = x
    def setY(self,y):
        self.__y=y

class elf:
    __x = "мужчина"
    __y = "женщина"

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y
class orc:
    __x = "мужчина"
    __y = "женщина"

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y
class gnome:
    __x = "мужчина"
    __y = "женщина"

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y
class man_crusaders:
    __x = "мужчина"

    def __init__(self, x):
            self.__x = x

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x


class women_crusaders:
    __y = "женщина"

    def __init__(self,y):
        self.__y = y

    def getY(self):
        return self.__y

    def setY(self, y):
        self.__y = y
class man_rogue:
    __x = "мужчина"

    def __init__(self, x):
        self.__x = x

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x
class women_rogue:
    __y = "женщина"

    def __init__(self, y):
        self.__y = y

    def getY(self):
         return self.__y

    def setY(self, y):
        self.__y = y
class man_wizard:
    __x = "мужчина"

    def __init__(self, x):
        self.__x = x

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x

class women_wizard:
    __y = "женщина"

    def __init__(self, y):
         self.__y = y

    def getY(self):
        return self.__y

    def setY(self, y):
         self.__y = y
class man_healer:
    __x = "мужчина"

    def __init__(self, x):
        self.__x = x

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x
class woman_healer:
    __y = "женщина"

    def __init__(self, y):
        self.__y = y

    def getY(self):
        return self.__y

    def setY(self, y):
        self.__y = y
class man_warior:
    __x = "мужчина"

    def __init__(self, x):
         self.__x = x

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x
class woman_warrior:
    __y = "женщина"

    def __init__(self, y):
        self.__y = y

    def getY(self):
        return self.__y

    def setY(self, y):
        self.__y = y
h = human("мужчину","женщину")
m= h.getX()
w= h.getY()
b=input("Введите m для выбора мужчины и w для выбора женщины  и нажммите ENTER:")
while True :
    b = input("Введите m для выбора мужчины и w для выбора женщины  и нажммите ENTER:")
    if b == "m":
        print ("Вы выбрали: "+ m )
        break
    elif b== "w":
        print ("Вы выбрали: "+w)
        break
    else:
        print("Попробуйте еще раз")
    continue
e = elf("Эльф", "Эльфийка")
o= orc("Орк","Орчиха")
g= gnome("Гном","Гномиха")
b1=input("На первый раз хорошо, а теперь попробуйте выбрать рассу, всего их 4:эльфы(e),орки(o),люди(h) и гномы(g) и нажмите ENTER:")
b1=0
while True:
    b1 = input("На первый раз хорошо, а теперь попробуйте выбрать рассу, всего их 4:эльфы(e),орки(o),люди(h) и гномы(g) и нажмите ENTER:")
    if b == "m" and b1 == "e":
        print("Эльф Вам отлично подходит!")
        break
    elif b =="w" and b1 == "e":
        print("ммм Эльфийка, класс!")
        break
    if b == "m" and b1 == "o":
        print("Чем шире наше морды - тем теснее наши ряды")
        break
    elif b =="w" and b1 == "o":
        print("Ты сюда пришел командовать, или щелкать?")
        break
    if b == "m" and b1 == "g":
        print("Кто к нам с мечем придет, тех проще застрелить!")
        break
    elif b =="w" and b1 == "g":
        print(" Быстро и дешево выполню любую халтуру!")
        break
    if b == "m" and b1 == "h":
        print("Я бью два раза: один — по голове, второй — по крышке гроба!")
        break
    elif b =="w" and b1 == "h":
        print(" Если хочешь миром править, нужно четкий план составить!")
        break
    else:
        print("Однажды тьма призвала меня... но я был занят. Однажды я призвал тьму... но там был автоответчик. Так мы и не встретились.")
        continue


