# in this it will make the text file in the given folder


import os

for i in range(11,47):
    newpath = f'F:\\NK HEDGE SCHOOL\\{i}'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        print("Completed")