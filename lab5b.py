#!/usr/bin/env python3
# Author ID: sbhujel2

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"File {file_name} not found."
    except Exception as e:
        return str(e)

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # returns its entire contents as a list of lines without new-line characters
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return f"File {file_name} not found."
    except Exception as e:
        return str(e)

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    try:
        with open(file_name, 'a') as file:
            file.write(string_of_lines)
    except Exception as e:
        return str(e)

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    try:
        with open(file_name, 'w') as file:
            for line in list_of_lines:
                file.write(line + '\n')
    except Exception as e:
        return str(e)

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    try:
        with open(file_name_read, 'r') as file_read:
            lines = file_read.readlines()
        with open(file_name_write, 'w') as file_write:
            for index, line in enumerate(lines, start=1):
                file_write.write(f"{index}:{line}")
    except FileNotFoundError:
        return f"File {file_name_read} not found."
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    append_file_string(file1, string1)
    append_file_string(file1, string1)  # Append again to see the effect

    print(read_file_string(file1))
    # Expected output:
    # 'First Line\nSecond Line\nThird Line\nFirst Line\nSecond Line\nThird Line\n'

    write_file_list(file2, list1)

    print(read_file_string(file2))
    # Expected output:
    # 'Line 1\nLine 2\nLine 3\n'

    copy_file_add_line_numbers(file2, file3)

    print(read_file_string(file3))
    # Expected output:
    # '1:Line 1\n2:Line 2\n3:Line 3\n'

