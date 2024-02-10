import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, json={"title_1": "I am Alex"}) # http request
#print(get_response.text)
#print(get_response.json())
# print()
# print(get_response.status_code)
# print()
print(get_response.json())
# print()
#print(get_response.status_code)