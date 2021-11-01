
def main():
    # num1, num2 = 10, 20 #if
    # num1, num2 = 100, 20 #else
    num1, num2 = 10, 20 #elif

    #conditional flow uses if, elif, else
    if (num1 < num2):
        result = "num1 is less then num2"
    elif (num1 == num2):
        result = "both are equal"
    else:
        result = "num2 is less then num1"
    print(result)

    #Conditional statements let you see a if b else c
    result = "num1 is less then num2" if (num1 < num2) else "Both are equal"
    print(result)

if __name__ == "__main__":
    main()