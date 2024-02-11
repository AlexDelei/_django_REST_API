import requests

endpoint = "http://127.0.0.1:8000/api/products/13982347032640346034/"

get_response = requests.get(endpoint) # http request

print(get_response.json())