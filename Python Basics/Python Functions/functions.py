

#define function 
def sayHello():
    print("Hello Pranav!")


#passing parameters to function
def sayHello1(name):
    print('Hello, ', name)


#return value from functions
def findCube(num):
    return num*num*num


#function with default value of argument 
def sayHello2(name='XYZ', age = 1):
    print('Hello, ', name)
    print('Age is, ', age)


#function with variable number of argument 
def func_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result




######## :: EXECUTION 

# sayHello()

# sayHello1('Pranav')

# print(sayHello1())

# print(findCube(10))

# print(sayHello2())
# print(sayHello2('Pranav'))
# print(sayHello2(age = 11 , name = 'Pranav'))

print(func_add(1, 2, 3, 4, 7))