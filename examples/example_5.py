#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # open the newfile.txt in read mode. causes error if no such file exists.
    fileptr = open("newfile.txt", "x")
    print(fileptr)

    if fileptr:
        print("File created successfully")

    # closes the opened file
    fileptr.close()

    # open the newfile.txt in read mode. causes error if no such file exists.
    with open("newfile2.txt", "x") as fileptr:
        print(fileptr)

    if fileptr:
        print("File created successfully")
