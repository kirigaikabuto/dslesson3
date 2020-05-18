class Home:
    def __init__(self,address,width,height):
        self.address = address
        self.width= width
        self.height= height
    
    def setAddress(self,address):
        self.address = address
    def print_info(self):
        print(self.address,self.width,self.height)

    def getArea(self):
        s = self.width * self.height
        return s
    
    def __str__(self):
        st=f"Address:{self.address},Width:{self.width},Height:{self.height}"
        return st