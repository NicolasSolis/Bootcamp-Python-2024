import os
dir = './folder'
old_file = os.path.join(dir, 'file.txt')
new_file = os.path.join(dir, 'new_file.txt') #renombrar archivos, directorios y subdirectorios
os.rename(old_file, new_file)

import shutil
shutil.move('./folder/file.txt', './folder/new_file.txt')