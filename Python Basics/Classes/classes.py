

class FirstClass():
    def function1(self):
        print('this is function1') 

    def function2(self, secondParam):
        print("this is function2 ", secondParam)
    
class SecondClass(FirstClass): #inheritance
    def function1(self):
        FirstClass.function1(self)
        print('this is Second Class function1')
    def funciton2(self, secondParam):
        print('this is Second Class function2') 

def main():
    c1 = FirstClass()
    c1.function1()
    c1.function2('Hello')

    c2 = SecondClass()
    c2.function1()
    c2.function2('Hi')

if __name__ == "__main__":
    main()
