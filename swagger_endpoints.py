import requests
import json

# URL of the Swagger JSON
swagger_url = "http://petstore.swagger.io/v2/swagger.json"

# Fetch the Swagger JSON
response = requests.get(swagger_url)

if response.status_code == 200:
    swagger_data = json.loads(response.text)

    # Extract and list all endpoints
    paths = swagger_data.get("paths", {})
    endpoints = list(paths.keys())

    # Print the endpoints
    print("Endpoints:")
    for endpoint in endpoints:
        print(endpoint)
else:
    print("Failed to fetch Swagger JSON. Status code:", response.status_code)



