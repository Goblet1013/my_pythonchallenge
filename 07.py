import sys
from PIL import Image

image_path = "C:\\Users\\a\\Desktop\\oxygen.png"

image = Image.open(image_path)
x_size = image.size[0]
y_size = image.size[1]
result = []
for i in range(0, x_size):
    rgb = image.getpixel((i, y_size/2))
    if i % 7 == 0:
        result.append(rgb)
for i in result:
    print(chr(i[0]), end='')
print()
result = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for i in result:
    print(chr(i), end='')