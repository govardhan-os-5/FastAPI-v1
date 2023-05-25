import requests
url = 'http://127.0.0.1:8000/profile'
data = ''
response = requests.get(url, data=data)
print("Response",response.text)