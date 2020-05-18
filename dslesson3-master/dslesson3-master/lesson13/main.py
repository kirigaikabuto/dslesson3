# Чертеж дома - Класс,class
# Дом - объект,object,reference,ссылка
class Home:
    #constructor конструктор -> создают свойства
    def __init__(self,a,b,c):
        self.address = a
        self.width= b
        self.height= c

# 1 класс но может быть много объектов
#home1 -> object
#Home() -> создание класса
print("HOME1")
home1 = Home("address1",100,200)
print(home1.address)
print(home1.width)
print(home1.height)
print("HOME2")
home2 = Home("address2",300,400)
print(home2.address)
print(home2.width)
print(home2.height)