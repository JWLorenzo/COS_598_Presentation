import requests

headers = {
    "Authorization": "Bearer your_token_here",
}

payload = {"username": "jacob", "password": "secure123"}

rp = requests.post("https://httpbin.org/post", headers=headers, data=payload)

print("rp text", rp.text)
with open("headers.txt", "w") as headers:
    headers.write(rp.text)
    headers.write("\n\nResponse Headers:\n")
    for key, value in rp.headers.items():
        headers.write(f"{key}: {value}\n")
