

def main():
    x = 0
    #define a while loop
    while (x < 10):
        print(x)
        x = x+1

    #define a for loop
    for x in range(5, 10):
        print(x)

    #use a for loop over a collection
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    for d in days:
        print(d)

    #use the break and continue statements
    for x in range (5, 10):
        # if (x == 7): break
        # print(x)

        if(x % 2 == 0): continue
        print(x)

    #using the enumrate function to get index
    users = ['Pranav', 'Kedar', 'Harsh', 'Aadita']
    for i,x in enumerate(users):
        if(x == 'Harsh'):
            print(i, x)        


if __name__ == "__main__":
    main()