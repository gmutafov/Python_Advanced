import os
# try:
#     path = os.path.join('file_writer', 'my_first_file.txt')
#     os.remove(path)
#
# except FileNotFoundError:
#     print('File is already deleted!')
#

path = os.path.join('file_writer', 'my_first_file.txt')

if os.path.exists(path):
    os.remove(path)
else:
    print("File is already deleted!")