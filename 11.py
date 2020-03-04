from PIL import Image

cave = r'C:\Users\aaa\Desktop\cave.jpg'

img = Image.open(cave)
img_v = img.load()
new = Image.new('RGB',(320,240))
new_v = new.load()
for i in range(0,320):
    for j in range(0,240):
        new_v[i,j] = img_v[2*i,2*j]
new.show()
