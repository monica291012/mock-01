import argparse
import requests

parser = argparse.ArgumentParser(
    description="Fetch users from a REST API"
)

parser.add_argument(
    "--limit",
    type=int,
    default=None,
    help="Maximum number of users to display"
)

args = parser.parse_args()

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    users = response.json()

    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be a positive integer")

    for user in users[:args.limit]:
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print()

except requests.exceptions.RequestException as error:
    print(f"API request failed: {error}")