import requests

 
# url = 'http://127.0.0.1:8000/articles_api/v1/'
# r = requests.post(url=url, json={'title': 'new', 'author': 'aiur', 'email': 'aiur@a.a'})

# print(r.text)

# url = 'http://127.0.0.1:8000/article_api/v1/4'
# r = requests.delete(url=url, json={'title': 'fff', 'author': 'aiur', 'email': 'aiur@a.a'})

# print(r.text)

 
url = 'http://127.0.0.1:8000/list_of_users_api/v1/'
r = requests.get(url=url, json={'title': 'new', 'author': 'aiur', 'email': 'aiur@a.a'}, headers={"Authorization": "Token e5c809152e66ba0105c785f7132e9bb0a7b1b487"})

print(r.text)
