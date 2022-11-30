import os
print(os.listdir())
spisok = []
for file in os.listdir():
    if os.path.isfile(file):
        spisok.append(file)
print(spisok)

spisok = []
for file in os.listdir():
    if os.path.isdir(file):
        spisok.append(file)
print(spisok)