class computer:
    def __init__(self):
        self.__max_prise=900
    def sell(self):
        print("selling prise is :" , self.__max_prise)
    def setmaxPrise(self,prise):
        self.__max_prise=prise
c=computer()
c.sell()
c.__max_prise=1000
c.sell()
c.setmaxPrise(1000)
c.sell()