import requests

url = 'http://gyelejin.ru:4444/'

for i in range(100):
    print(i)
    print(requests.get(url=url).text)
    print(requests.get(url=url+'/chats').text)
    print(requests.get(url=url+'/notes').text)
    print(requests.post(url=url+'/Login').text)