# Чертеж дома - Класс,class
# Дом - объект,object,reference,ссылка
class Home:
    #constructor конструктор -> создают свойства
    def __init__(self,address,width,height):
        self.address = address
        self.width= width
        self.height= height
    #method
    def print_info(self):
        print(self.address,self.width,self.height)

    def getArea(self):
        s = self.width * self.height
        return s
# 1 класс но может быть много объектов
#home1 -> object
#Home() -> создание класса
print("HOME1")
home1 = Home("address1",100,200)
home1.print_info()
area1 = home1.getArea()
print(area1)
print("HOME2")
home2 = Home("address2",300,400)
home2.print_info()
area2 = home2.getArea()
print(area2)