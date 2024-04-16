
import os

path = "C://Users//Admin//Desktop//JS//318//Work"
dir_list = os.listdir(path)
print("Files and directories in '", path, "':")
# print(os.path.getsize(path) / 1024)
print(dir_list)
print(os.path.getsize(__file__))


