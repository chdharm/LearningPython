class Item:
    def __init__(self,id=-1,name='NA',price=-1):
        self.id=id
        self.name=name
        self.price=price
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price
