import requests

endpoint = "http://127.0.0.1:8000/api/products/"

get_response = requests.get(endpoint) # http request

print(get_response.json())
