#!/usr/bin/env python3
# Author ID: sbhujel2

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try:
        result = int(number1) + int(number2)
        return result
    except Exception:
        return 'error: could not add numbers'

def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
    except Exception:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                    # 15
    print(add('10', 5))                  # 15
    print(add('abc', 5))                 # error: could not add numbers

    print(read_file('seneca2.txt'))      # ['Line 1\n', 'Line 2\n', 'Line 3\n']
    print(read_file('file10000.txt'))    # error: could not read file

