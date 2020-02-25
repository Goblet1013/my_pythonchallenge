import requests
import pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"

r = requests.get(url)
result = pickle.loads(r.content)
for i in result:
    for j in i:
        for times in range(0,j[1]):
            print(j[0],end='')
