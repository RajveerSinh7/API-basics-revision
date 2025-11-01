#http request usage with/without api call

import requests

# 1) sending an http request with no api
response = requests.get("https://www.google.com")
print("----------------------NO API----------------------\n")
print(response.text) #this prints raw html (not structured)

# 2) API-styled HTTP request
url = "https://api.github.com/users/RajveerSinh7"
response = requests.get(url)

print("\n----------------------WITH API----------------------\n")
print(response.json())
