#!/usr/bin/python
import os
import shutil
import sys

# global_variable
replaceDic = {}
replace_dic_text_file_path = "replaceDic.txt"
target_path = "sample"
result_path = "output"
log_path = "log.txt"
log_lines = ["log_type: \n[R]: replace folder\n[r]: replace file\n[s]: skip file\n\n"]


def read_text_file_to_lines(filePath):
    file_obj = open(filePath, "r")
    lines = file_obj.readlines()
    file_obj.close()
    return lines


def read_dic(file_path):
    lines = read_text_file_to_lines(file_path)
    for line in lines:
        pair = line.split(":=")
        if pair[1][-1:] == "\n":
            pair[1] = pair[1][:-1]
        if pair[1] != pair[0]:
            replaceDic[pair[0]] = pair[1]


def string_replace_with_substring_dic(string, dic):
    newString = string
    for dicItem in dic:
        if dicItem in newString:
            newString = newString.replace(dicItem, dic[dicItem])
    if string != newString:
        log_lines.append("")
    return newString


def replace_folder(old_path, new_path, prefix):
    new_prefix = prefix if old_path == target_path else prefix + "\t"
    log_lines.append("\n" + prefix + "[R]\"" + old_path + "\" \t to \"" + new_path + "\"\n")
    if os.path.exists(new_path):
        shutil.rmtree(new_path)
    os.mkdir(new_path)
    lists = os.listdir(old_path)
    lists.sort()
    lists2 = []
    # using two loops make log.txt looks better
    for item in lists:
        full_path = os.path.join(old_path, item)
        newName = string_replace_with_substring_dic(item, replaceDic)
        temp_new_path = os.path.join(new_path, newName)
        if os.path.isfile(full_path):
            if item == ".DS_Store":
                log_lines.append(prefix + "\t[s]:skip file \"" + full_path + "\"\n")
            else:
                replace_file(full_path, temp_new_path, new_prefix)
        else:
            lists2.append(item)
    for item in lists2:
        newName = string_replace_with_substring_dic(item, replaceDic)
        replace_folder(os.path.join(old_path, item), os.path.join(new_path, newName), new_prefix)
    log_lines.append("\n")


def replace_file(old_path, new_path, prefix):
    log_lines.append(prefix + "[r]\"" + old_path + "\" to \"" + new_path + "\"\n")
    lines = read_text_file_to_lines(old_path)
    for i in range(len(lines)):
        lines[i] = string_replace_with_substring_dic(lines[i], replaceDic)
    file_obj = open(new_path, "w")
    file_obj.writelines(lines)
    file_obj.close()


# read dic
read_dic(replace_dic_text_file_path)
print(replaceDic)
if len(sys.argv) >= 2:
    target_path = sys.argv[1]

info = "process " + target_path + "\n"
log_lines.append(info)
print(info)

result_path = target_path + "_replacement"
if os.path.isdir(target_path):
    replace_folder(target_path, result_path, "")
else:
    replace_file(target_path, result_path, "")

# write log
file_obj = open(log_path, "w")
file_obj.writelines(log_lines)
file_obj.close()
