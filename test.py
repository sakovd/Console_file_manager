import os
print(os.listdir())

with open('listdir.txt', 'w') as f:
    spisok_files = []
    spisok_folders = []
    for file in os.listdir():
        if os.path.isfile(file):
            spisok_files.append(file)
        elif os.path.isdir(file):
            spisok_folders.append(file)
    f.write(f'files: {spisok_files}')
    f.write(f'\nfolders: {spisok_folders}')


print(spisok_files)
print(spisok_folders)

# spisok_folders = []
# for file in os.listdir():
#     if os.path.isdir(file):
#         spisok_folders.append(file)
# print(spisok_folders)