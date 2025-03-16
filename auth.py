import requests
from requests.auth import HTTPBasicAuth

url = 'https://httpbin.org/basic-auth/users/pass'  
username = input("Enter your username: ")
password = input("Enter your password: ")
response = requests.get(url, auth=HTTPBasicAuth(username, password))
if response.status_code == 200:
    print("Access granted!")
    
else:
    print(f"Access denied. Status code: {response.status_code}")
