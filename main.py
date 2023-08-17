# imports
import requests
import argparse

from api import gather_rating

# argument parser definition
parser = argparse.ArgumentParser(
    prog='Lichess ranking bot',
    description='Lichess bot providing information about progress/regress in chess.',
    add_help=False,
)

# parsing function arguments
parser.add_argument('nickname', type=str, help='Your lichess nickname')
parser.add_argument('-a', '--address', metavar='\b', type=str, help='Your phone number or email')
parser.add_argument('-t', '--type', metavar='\b', type=str, default='all', nargs='+', help='Type of rating')
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='Show this help message and exit.')
parser.add_argument('-w', '--way', metavar='\b', type=str, choices=['email', 'sms'], default='email',
                    help='Way of delivering the rating message')

# argument parser function call
args = parser.parse_args()
print(args)
print(args.nickname, args.address, args.type, args.way)

user_nick = args.nickname
rating_type = args.type
print(rating_type)

api_response = requests.get(f"https://lichess.org/api/user/{user_nick}")

# function to check api response
gather_rating(api_response, rating_type)