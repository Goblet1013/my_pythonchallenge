import os
import zipfile

file = "C:\\Users\\goblet\\Desktop\\channel"
channel = r"‪C:\Users\goblet\Desktop\channel.zip"
index = "90052"
fzip = zipfile.ZipFile(channel,'r')

while True:
    with open(file+"\\"+index+".txt") as f:
        print(fzip.getinfo(index+".txt").comment,end="")
        index = f.read().split('nothing is ')[1]
