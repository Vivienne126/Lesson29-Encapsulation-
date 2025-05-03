class Myclass:
    __private="Hello"
    def __Bye(self):
        print("I am inside the class")
    def hello(self):
        print(Myclass.__private)
obj=Myclass()
obj.hello()
obj.__Bye