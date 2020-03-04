
file = r'C:\Users\goblet\Desktop\evil2.gfx'

with open(file,'rb') as f:
    content = f.read()

for i in range(0,5):
    with open(r'C:\Users\goblet\Desktop\%d.jpg'% i,'wb') as f:
        f.write(content[i::5])
