
#declaring variable
var = 11
print(var)

#redeclariang variable
var = 'String Test'
print(var)

#ERROR: concating incompatible variables
str = var + str(123)
print(str)

#Global vs Local Variables
def calculate():
    # global var
    var = 10
    print(var)

calculate()
print(var)


del var #deleteing var value from memory
print(var) #Erron will occur
