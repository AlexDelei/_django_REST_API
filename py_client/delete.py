import requests

product_id = input("What product id do you want to user? \n")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} is not a valid id')

if product_id:
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"

    get_response = requests.delete(endpoint) # http request

    print(get_response.status_code)