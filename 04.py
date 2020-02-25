import requests

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
index = "12345"
while True:
    r = requests.get(url+index)
    print(r.text)
    index = r.text.split('is ')[1]
    print(index)
