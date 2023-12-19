import requests
import json 




def process_data():
    url = 'http://192.168.30.56:3333/api/fs/list' 
    url2 = 'http://192.168.30.56:3333/api/fs/remove'
    getAuthUrl = 'http://192.168.30.56:3333/api/auth/login'

    authHeaders = {
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json'
    }
    authdata = {
        "username": "admin",
        "password": "Yzyyzy360681"
    }
    authResponse = requests.post(getAuthUrl,headers=authHeaders,json=authdata)
    Authorization = json.loads(authResponse.text).get("data").get("token")
    
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate', 
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'Authorization': Authorization,
    'Connection': 'keep-alive',
    'Content-Length': '72', 
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': '_CrPoSt=cHJvdG9jb2w9aHR0cDo7IHBvcnQ9MTk4ODg7IHBhdGhuYW1lPS87; _SSID=Cv29Xh5HYFeEc40LjGrWcGL7oZYKe6ijRKUrvZXqznI; did=6ok8SS86NaEE59NorBqU3qpxn4jxQZuFquwTuF5QB9Kn7C18I619pTK2ksrCo0-NiYdwDbJndFn2GnBTKHW9ug; stay_login=1; UserId=d0bf9b22-5e2f-4c82-9d7d-b6aa4a316321; dark=true; Jackett=CfDJ8MRfuCejeRhPrY8dD4KxqlznJdQBIBd7J5yelxfXpcAauan1bjlP0tK1GiztvKRbCv7TPJAng0Ap2qazZlsuGuBwrzlbLiHQoO-r8iLqJUAV4nM7m3I0PZbkUtXILlbgjHpf14U_2ucc6X1HWuAr3i7QT0vA3TLjuK8ZKpGVRG5pkTsX676Vs15Uyl41bl_rulecqH0OJyzPjHnWBHuuTASxlsWCqTrIvaZXtXeGDh79-4pMBu6xTqJthtY8zob1V__zAm1LAlOvZbqDLqAHhWC7xR1HViJTwif6Rk10agiBt0dK1sqs3g-XzQ-HV3jD9b020BOuVvQAmnvjROSIi7s; session=.eJw9zjsOwyAMANC7MHcwBmOcy0QGG7VDo4okU9W79zN0f8N7hnVM369hOebpl7DeLCxhSKqjABeDWjtkRzAiaVapICK3CLGXxKl8BTfixCZFa0yCMLQbWmeM0SoToTKxZzTJBTtIFxUZOlquGmMZXA2ag5MSpgSaLXwiD5933Xw7_rVz9_n7wesNNh40Fg.ZWORnA.szeGlpWYJt1lPEgYiBdJeh6p-cY; id=MH6w3-iJgF8XF5K1TFK6RS-PK3Y1XhAGKg141BGHiVAi1ddAQOo_bZ15OZpDE3mbrxRlP7IFWgwyDQJxLZGuQI; Authorization=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoxLCJ1c2VyX25hbWUiOiIiLCJ1c2VyX2lkIjoiZDBiZjliMjItNWUyZi00YzgyLTlkN2QtYjZhYTRhMzE2MzIxIiwidXNlcl9lbWFpbCI6IjMyMDgwMDY2NDJAcXEuY29tIiwidXNlcl9wYXNzd29yZCI6IiIsImlzX2FkbWluIjp0cnVlLCJpc19sb2NrIjpmYWxzZSwiY3JlYXRlZF9hdCI6IjIwMjMtMTEtMjNUMDM6MDI6MzguNzI5OTI2ODcyKzA4OjAwIiwidXBkYXRlZF9hdCI6IjIwMjMtMTEtMjNUMDM6MDI6MzguNzI5OTI5MjQ3KzA4OjAwIn0sImV4cCI6MTcwMTc3MDcyMCwiaXNzIjoiQWxmcmVkbyBNZW5kb3phIn0.JwitfKmGDdRIkHIW6sPzcoGsourTN8KnnvdPH-UY2ug; is_admin=true; io=2HexD49moHxeFkqpAAAT',
    'DNT': '1',
    # 'Host': '192.168.30.56:3333',
    # 'Origin': 'http://192.168.30.56:3333',
    # 'Referer': 'http://192.168.30.56:3333/pan/ali4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76'
    }

    data = {
        "path":"/pan/ali4", 
        "password":"",
        "page":1,
        "per_page":0,
        "refresh":False
    }

    data2 = {
        "dir":"/pan/ali4",
        "names":[] 
    }

    response = requests.post(url, headers=headers, json=data)
    dict_json1 = json.loads(response.text)
    datatest = dict_json1.get("data")

    if datatest.get("content") is  None:
        return
    
    arr = datatest.get("content") 

    for content in arr:
        name = content.get("name")
        data2.get("names").append(name)
    
    if len(data2.get("names")) != 0:
        response2 = requests.post(url2, headers=headers, json=data2)
        # 处理response2

def main():
    process_data()

if __name__ == '__main__':
    main()