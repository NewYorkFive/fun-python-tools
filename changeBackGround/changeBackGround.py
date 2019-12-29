import os
import re
import time
from random import randrange

'''
1.put your dir path in this array, default will be current dir

2.  be careful if you copy the path from the terminal, you need to process '\ ' to ' ', for example:
    '/Users/Now/untitled\ folder' to '/Users/Now/untitled folder'
'''

target_dirs = []

# the interval of changing pictures, default is 1 second
interval_in_seconds = 1
# total times you want change the background
total_change_times = 60 * 60
# support image formats
support_image_formats = ['jpg', 'jpeg', 'png']

if len(target_dirs) == 0:
    target_dirs.append(os.getcwd())
print("target_dirs {}".format(target_dirs))
print("--- process strat ---")

image_paths = []


def add_picture_from_path(path):
    print("add picture from {}".format(path))
    files = os.listdir(path)
    for file in files:
        new_path = os.path.join(path, file)
        if os.path.isdir(new_path):
            add_picture_from_path(new_path)
        else:
            match = re.match(".*\.(?P<format>.*)", new_path)
            if match:
                file_format = match["format"]
                if file_format in support_image_formats:
                    image_paths.append(new_path)
                    # print("add {}".format(file))


for target_dir in target_dirs:
    add_picture_from_path(target_dir)

image_paths_len = len(image_paths)
if image_paths_len == 0:
    print("no picture load, exit")
    exit()
if image_paths_len == 1:
    commands = ''' 
        osascript -e 'tell application "Finder" to set desktop picture to POSIX file "{}"'
        '''.format(image_paths[0])
    print("only picture load, exit")
    os.system(commands)        
    exit()

for i in range(0, total_change_times):
    test_image_path = image_paths[randrange(image_paths_len)]
    # test_image_path = image_paths[i]
    print(test_image_path)
    commands = ''' 
        osascript -e 'tell application "Finder" to set desktop picture to POSIX file "{}"'
        '''.format(test_image_path)
    # print(commands)
    os.system(commands)
    time.sleep(interval_in_seconds)
