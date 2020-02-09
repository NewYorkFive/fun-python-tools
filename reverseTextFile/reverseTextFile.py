#!/usr/bin/python

import sys

def reverse_file(filename, output_filename):
    reverse_file_with_line_number(filename, output_filename, 1, sys.maxsize)

def reverse_file_with_line_number(filename, output_filename, beginline, endline):
    f_in = open(filename, "r")
    lines = f_in.readlines()

    if endline == sys.maxsize:
        endline = len(lines)

    if len(lines) < endline:
        print ("endline exceed the file, no need to reverse, exit")
        f_in.close()
        return
    if len(lines) < beginline:
        print ("beginline exceed the file, no need to reverse, exit")
        f_in.close()
        return
    f_out = open(output_filename, "w")

    for i in range(beginline - 1):
        f_out.write(lines[i])
    for i in reversed(range(beginline - 1, endline)):
        f_out.write(lines[i])
    for i in range(endline, len(lines)):
        f_out.write(lines[i])
    f_in.close()
    f_out.close()
    return

exit_reason = '''
parameter invalid,
please try command "python3 reverseTextFile.py `file_path` ",
or "python3 reverseTextFile.py `file_path` `start_line` `end_line` "
example: "python3 reverseTextFile.py README.md 5 50" 
'''

filename = "README.md"
len_argv = len(sys.argv)
if len_argv == 2 or len_argv == 4:
    target_path = sys.argv[1]
    filename = target_path.split('/')
    filename = filename[len(filename) - 1]
    result_path = target_path.replace(filename, "reverse_" + filename)
    if len_argv == 2:
        reverse_file(target_path, result_path)
    else:
        start_line = int(sys.argv[2])
        end_line = int(sys.argv[3])
        reverse_file_with_line_number(target_path, result_path, start_line, end_line)
else:
    print(exit_reason)