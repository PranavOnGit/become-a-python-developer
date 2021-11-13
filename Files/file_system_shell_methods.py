
# Import necessary modules
import os
from os import path
import time
import shutil
from shutil import make_archive
import zipfile
from zipfile import ZipFile

def main():
    # Make a duplicate of the exisiting file
    open('testfile.txt', 'w+')
    if path.exists('testfile.txt'):
        # Get the path to the file in the current directory 
        src = path.realpath('testfile.txt')
        # print(src)

        # Lets make a backup copy by appending ".bkp" to the name
        dst = src + ".bak"

        # Copy over the modification time, permission and othe info 
        shutil.copy(src, dst)
        shutil.copystat(dst, src)

        file1 = time.ctime(path.getmtime('testfile.txt'))
        file2 = time.ctime(path.getmtime('testfile.txt.bak'))

        if file2 == file1:
            print('Modificaton time matched for both files')

        # Rename the origional file 
        # os.renames("testfile.txt", "new_testfile.txt")

        # Now put things into ZIP archive 
        root_dir, tails = path.split(src)
        shutil.make_archive('Archive', "zip", root_dir)
        
        # More fine-grinded control over ZIP files 
        with ZipFile("testzip.zip", 'w') as newzip:
            newzip.write("textfile")
            newzip.write("testfile.txt")


if __name__ == "__main__":
    main()