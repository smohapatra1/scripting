#!/usr/bin/python
#Copy or remove files
import os

def main():
    f = open("test.txt", "w+")
    os.rename("test.txt", "test2.txt")
    os.remove("test2.txt")

if __name__ == "__main__":
    main()
