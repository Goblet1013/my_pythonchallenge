import os
import zipfile

folder = "C:\\Users\\goblet\\Desktop\\channel"
channel = r"C:\Users\goblet\Desktop\channel.zip"
index = "90052"
fzip = zipfile.ZipFile(channel,'r')

while True:
    with open(folder + "\\" + index + ".txt") as f:
        temp = fzip.getinfo(index+".txt").comment.decode('utf-8')
        if temp == '\n':
            print()
        else:
            print(temp, end='')
        index = f.read().split('nothing is ')[1]
