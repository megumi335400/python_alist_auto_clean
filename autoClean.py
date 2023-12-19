import requests

import json

def process_data():

    url = 'http://192.168.30.56:xxxx/api/fs/list'
			# http://192.168.30.56:xxxx 前面的地址和端口号填入自己的alist的地址

    url2 = 'http://192.168.30.56:xxxx/api/fs/remove'

    getAuthUrl = 'http://192.168.30.56:xxxx/api/auth/login'



    authHeaders = {

        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',

        'Content-Type': 'application/json'

    }

    authdata = {

        "username": "axxxx",

      #username 里面填入自己的alist 账号  示例: "username": "zhangsan"

        "password": "xxxxxx1"
		#password 里面填入自己的alist 账号对应的密码  示例: "password": "123123"
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

    'Cookie': '_CrPoSt=cHJvdG9jb2w9aHR0cDFK6RS-PK3Y1XhAGKg141BGHiVAi1ddAQxxxxxxxxxxxUyZi00YzgyLTlkN2QtYjZhYTRhMzE2MzIxxxxlbWFpbCI6IjMyiaxxxoiQWxmcmVkbyBNZxxx',

      # Cookie 需要在浏览器中获取  后面贴图说明


    'DNT': '1',


    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76'

    }



    data = {

        "path":"/pan/ali4",
			# path 为 本地alist 挂载阿里云盘的路径
        "password":"",

        "page":1,

        "per_page":0,

        "refresh":False

    }



    data2 = {

        "dir":"/pan/ali4",
		# dir 为 本地alist 挂载阿里云盘的路径
        "names":[]

    }



    response = requests.post(url, headers=headers, json=data)

    dict_json1 = json.loads(response.text)

    datatest = dict_json1.get("data")



    if datatest.get("content") is  None:

        return arr = datatest.get("content")

    for content in arr:

        name = content.get("name")

        data2.get("names").append(name)

    if len(data2.get("names")) != 0:

        response2 = requests.post(url2, headers=headers, json=data2)


def main():

    process_data()


if __name__ == '__main__':

    main() 作者：就爱买破烂 https://www.bilibili.com/read/cv28501448/ 出处：bilibili
