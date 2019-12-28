import os

'''
1.put your dir path in this array, default will be current dir

2.  be careful if you copy the path from the terminal, you need to process '\ ' to ' ', for example:
    '/Users/Now/untitled\ folder' to '/Users/Now/untitled folder'
'''
target_dirs = []


if len(target_dirs) == 0:
    target_dirs.append(os.getcwd())
print("target_dirs {}".format(target_dirs))
print("--- process strat ---")


def del_dir(dir_path):
    listOfFiles = os.listdir(dir_path)
    for item in listOfFiles:
        new_dir_path = os.path.join(dir_path, item)
        if os.path.isdir(new_dir_path):
            if len(os.listdir(new_dir_path)) == 0:
                # command = "rm -rf {}".format(new_dir_path)
                # print(command)
                os.rmdir(new_dir_path)
                print("delete {}".format(new_dir_path))
            else:
                del_dir(new_dir_path)

    if (len(os.listdir(dir_path))) == 0:
        os.rmdir(dir_path)
        print("delete {}".format(dir_path))


for target_dir in target_dirs:
    del_dir(target_dir)

print("--- process end ---")
