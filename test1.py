import requests

#方法一
'''
url = "http://localhost:3000/Languages"
headers = {
    'Content-Type':"application/x-www-form-urlencoded"
}
response = requests.request("GET",url,headers=headers)
print(response.text)

#方法二
url = "http://localhost:3000/Languages?name_like=语"
headers = {
    'Content-Type':"application/x-www-form-urlencoded"
}
response = requests.request("GET",url,headers=headers)
print(response.text)
'''
#
url = "http://localhost:3000/Languages/1"
headers = {
    'Content-Type':"application/x-www-form-urlencoded"
}
response = requests.request("DELETE",url,headers=headers)
url = "http://localhost:3000/Languages"
response = requests.request("GET",url,headers=headers)
print(response.text)
