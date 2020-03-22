# Fun python tools

## 1. change background tool

![](./changeBackGround/changeBackgroundEffect.gif)

### How to use:
1. download the [python file](./changeBackGround/changeBackGround.py) at  `your_images_folder`, `your_images_folder` can contain other `image_folder`
2. open terminal, cd `your_images_folder`
3. run `python3 changeBackGround.py` in your terminal

[Code](./changeBackGround/changeBackGround.py)
### Custom setting:
1. to change target folders, change line `target_dirs = []`
2. to set interval , change line `interval_in_seconds = 1`
3. to set total times you wnat to change the background, change line `total_change_times`
4. for particular image formats you want to use, change line `support_image_formats = ['jpg', 'jpeg', 'png']`



## 2. delete empty folders tool
![](./deleteEmptyFolders/deleteEmptyFoldersEffect.gif)

### How to use:
1. download the [python file](./deleteEmptyFolders/deleteEmptyFolders.py) at  `target_folder`, `your_images_folder` can contain other `target_folder`
2. open terminal, cd `target_folder`
3. run `python3 deleteEmptyFolders.py` in your terminal

### Custom setting:
1. to change target folders, change line `target_dirs = []`


## 3. reverse a text file
![](./reverseTextFile/reverseTextFileEffect.gif)

### How to use:
1. download the [python file](./reverseTextFile/reverseTextFile.py) in a `folder`
2. open terminal, cd the `folder`
3. run `python3 reverseTextFile.py target_text_file` or `python3 reverseTextFile.py target_text_file start_line end_line`, example 'python3 reverseTextFile.py README.md 5 50'


## 4. fileReplacement, replace targetStrings to purposeStrings in a folder

![](./fileReplacement/fileReplacementEffect.gif)

### How to use:
1. download the [python file](./fileReplacement/fileReplacement.py) and the [replaceDic.txt](./fileReplacement/replaceDic.txt) in a `folder`
2. edit the `replaceDic.txt` to suit your goal
3. open terminal, cd the `folder`
4. run `python3 fileReplacement.py target_folder`, example `python3 fileReplacement.py sample`
