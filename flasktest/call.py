import requests

url = 'http://127.0.0.1:5000/query'
data = {'query': 'What’s the weather today?'}

response = requests.post(url, json=data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Failed to send query. Status code: {response.status_code}")
