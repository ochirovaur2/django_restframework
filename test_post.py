import requests

 
url = 'http://127.0.0.1:8000/article_api/v1/1'
r = requests.delete(url=url, json={'title': 'asd', 'author': 'aiur', 'email': 'aiur@a.a'})

print(r.text)