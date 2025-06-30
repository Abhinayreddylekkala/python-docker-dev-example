import requests

url = "http://localhost:8000"
data = {"id": 1, "name": "test", "second_name": "test2", "age": 20}

try:
    response = requests.post(url, json=data)
    print("Status Code:", response.status_code)
    print("JSON Response:", response.json())
except Exception as e:
    print("❌ Error:", e)
