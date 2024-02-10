import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "I am Saitoti",
    "price": 29.96
}
get_response = requests.post(endpoint, json=data) # http request

print(get_response.json())