import requests
from requests.auth import HTTPDigestAuth

# URL of the protected page or API endpoint
url = 'https://httpbin.org/digest-auth/auth/users/pass'  

# Prompt the user to enter their username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Sending a GET request with Basic Authentication
response = requests.get(url, auth=HTTPDigestAuth(username, password))

# Check the status of the response
if response.status_code == 200:
    print("Access granted!")
    
else:
    print(f"Access denied. Status code: {response.status_code}")
