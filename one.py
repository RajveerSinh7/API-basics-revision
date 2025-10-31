import requests
import json

response = requests.get('https://api.github.com/users/Rajveersinh7')
#the hyperlink used inside is api  (github api the return user info)
#endpoint(route): /users/Rajveersinh7

print(response) #status code

data = response.json()
print(json.dumps(data, indent=4))
print(response.json()['bio'])