import requests

API_URL = "https://www.stack-inference.com/run_deployed_flow?flow_id=6527f3d8335f24d98ce48294&org=4f68ac5e-29b8-4b19-b356-136071f22b50"
headers = {
    'Authorization': 'Bearer 3bbf8154-2844-4f7c-9c61-3ed5fa7bc128',
    'Content-Type': 'application/json'
}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload, timeout=300)
    return response.json()


print("Querying Stack AI...")

output = query({})

print("Stack AI response:")
print(output)
