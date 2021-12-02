import requests
'''
url = "http://localhost:3000/books"
payload = "id=3&title=接口测试&author=于涌"
headers = {
    'Content-Type':"application/x-www-form-urlencoded"
}
response = requests.request("POST",url,data=payload.encode(encoding='utf-8'),headers=headers)
print(response.text)



#查询所有图书
url = "http://localhost:3000/books"
headers = {
    'Content-Type':"application/x-www-form-urlencoded"
}
response = requests.request("GET",url,headers=headers)
print(response.text)

#查询《精通移动App测试实战》
url = "http://localhost:3000/books?title=精通移动App测试实战"
headers = {
    'Content-Type':"application/x-www-form-urlencoded"
}
response = requests.request("GET",url,headers=headers)
print(response.text)


url = "http://localhost:3000/books?title_like=精通移动App测试实战"
headers = {
    'Content-Type':"application/x-www-form-urlencoded"
}
response = requests.request("GET",url,headers=headers)
print(response.text)


#查看JSON文件中所有数据
url = "http://localhost:3000/db"
headers = {
    'Content-Type':"application/x-www-form-urlencoded"
}
response = requests.request("GET",url,headers=headers)
print(response.text)
'''

#删除《接口测试》这本图书
url = "http://localhost:3000/books/3"
headers = {
    'Content-Type':"application/x-www-form-urlencoded"
}
response = requests.request("DELETE",url,headers=headers)
print(response.text)
