


def main():
    # Open a file for writting and create if it dosen't exist
    file = open('textfile', 'w+') #w+ creates file if dosen't exist

    # Open the file for appending text to the end
    for x in range(10):
        file.write("This is line: "+ str(x) + "\r\n")

    # Write some lines of data into the file
    file = open('textfile', 'a') #a helps to append the data in file
    for y in range(11):
        file.write("Append the line :"+ str(y) +"\r\n")

    #close the file when done
    file.close()

    # Open the file backup and read the content
    file = open('textfile', 'r') #r is for reading the file content

    if file.mode == 'r':
        content = file.read()
        print(content)

        content = file.readlines()
        for line in content:
            print(line)

    
if __name__ == "__main__":
    main()
