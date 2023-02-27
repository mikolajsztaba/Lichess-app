import requests

# asking about username
# username = input('Provide your username:\n')

# api request
# response = requests.get(f"https://lichess.org/api/user/{username}")
response = requests.get(f"https://lichess.org/api/user/PAPOR123")

# return code
print(response)
json_return = response.json()
print(json_return)
print(json_return['id'])
# print(response.json())