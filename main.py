# imports
import requests
import argparse

# argument parser definition
parser = argparse.ArgumentParser(
    prog='Lichess ranking bot',
    description='Lichess bot providing information about progress/regress in chess.',
)

# parsing function arguments
parser.add_argument('--nickname', type=str, help='your lichess nickname')
parser.add_argument('--phone_number', type=str, help='your phone number')

# argument parser function call
args = parser.parse_args()
print(args)
print(args.nickname, args.phone_number)

user_nick = args.nickname

api_response = requests.get(f"https://lichess.org/api/user/{user_nick}")

print(api_response)
print(api_response.status_code)

if api_response.status_code == 200:
    print("OK")
    json_return = api_response.json()
    print(json_return)
    print(json_return['id'])
else:
    print("NIE OK")
